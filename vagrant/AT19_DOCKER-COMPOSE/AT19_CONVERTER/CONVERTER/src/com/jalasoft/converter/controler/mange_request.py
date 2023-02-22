#
# @mange_request.py Copyright (c) 2023 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#


from flask import request
from werkzeug.utils import secure_filename
import os
from common.exception.input_exception import InvalidInputException
from config import UPLOAD_FOLDER
from config import RESPONSE_FOLDER
from common.valid_data import Validations
from database.checksum import compare_checksum, checksum_generator_md5


class ManageData:
    """Manages the data received in the endpoint"""
    def __init__(self):
        self.filename = None
        self.filename_2 = None
        self.output_file_extension = None
        self.in_file = None
        self.input_file = None
        self.in_file_2 = None
        self.input_file_2 = None
        self.output_extension = None
        self.checksum_param = None

    def get_data(self, file_prefix):
        """Gets data from the form"""
        try:
            if file_prefix != 'audMixaud-':
                self.input_file = request.files["input_file"]
            else:
                self.input_file = request.files["input_file_1"]
                self.input_file_2 = request.files["input_file_2"]
            self.output_extension = request.form["output_file"]
            self.checksum_param = request.form["checksum_param"]
        except Exception as error:
            raise InvalidInputException("Invalid input: the input should not be None type -" + file_prefix)
        Validations().validate_file(self.input_file, file_prefix)
        Validations().validate_output(self.output_extension, file_prefix)
        if file_prefix == 'audMixaud-':
            Validations().validate_file(self.input_file_2, file_prefix)

    def manege_data(self, file_prefix):
        """Sets the format of the output file name"""
        self.get_data(file_prefix)
        if self.output_extension[0] != '.':
            self.output_extension = '.' + str(self.output_extension)
        self.filename = secure_filename(self.input_file.filename)
        if file_prefix == 'audMixaud-':
            self.filename_2 = secure_filename(self.input_file_2.filename)

    def save_data(self, file_prefix):
        """Saves the uploaded file in uploads folder"""
        self.input_file.save(os.path.join(UPLOAD_FOLDER, self.filename))
        self.in_file = os.path.join(UPLOAD_FOLDER, self.filename)
        if file_prefix == 'audMixaud-':
            self.input_file_2.save(os.path.join(UPLOAD_FOLDER, self.filename_2))
            self.in_file_2 = os.path.join(UPLOAD_FOLDER, self.filename_2)


    def generate_path(self, file_prefix):
        """Generates the input file path, the output file path, and the download file link"""
        self.manege_data(file_prefix)
        self.save_data(file_prefix)
        checksum = str(checksum_generator_md5(self.in_file))
        if self.checksum_param != str(checksum_generator_md5(self.in_file)):
            return None, checksum
        else:
            self.in_file = compare_checksum(self.filename, self.in_file)

        if file_prefix == 'pdfToima-':
            self.output_extension = file_prefix + self.filename.split('.')[0] + '-%4d' + str(self.output_extension)
        if file_prefix == 'vidToima-':
            new_folder = UPLOAD_FOLDER + os.sep + self.filename.split('.')[0] + os.sep + self.filename.split('.')[0] + os.sep
            os.makedirs(new_folder, exist_ok=True)
            self.output_extension = new_folder + '%06d.' + str(self.output_extension)
        else:
            self.output_extension = file_prefix + self.filename.split('.')[0] + str(self.output_extension)
        port = os.getenv("CONVERTER_PORT")
        url = os.getenv("CONVERTER_HOST")
        download_url = f"{url}{port}/download?file_name={os.path.basename(self.output_extension)}"
        self.output_extension = os.path.join(RESPONSE_FOLDER, self.output_extension)
        if file_prefix == 'audMixaud-':
            return [self.in_file, self.in_file_2, self.output_extension, download_url], checksum
        return [self.in_file, self.output_extension, download_url], checksum


