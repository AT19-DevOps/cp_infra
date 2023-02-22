#
# @valid_data.py Copyright (c) 2023 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#


from werkzeug.datastructures import FileStorage
from pathlib import Path
from common.common_validations import CommonValidator
from common.exception.input_exception import InvalidInputException
from common.get_file_type import MimeTypeGetter


class Validations:
    """Defines Allowed extensions criteria"""

    def __init__(self):
        self.extensions = {'ima': ['png', 'jpg', 'jpeg', 'gif'], 'vid': ['mp4', 'avi', 'mov'],
                           'aud': ['mp3', 'wav', 'opus'], 'tex': ['txt', 'pdf'],
                           'image': ['imaToima-', 'imaBWima-', 'imaFlima-', 'imaRoima-', 'imaReima-', 'imaPdftex-'],
                           'audio': ['audIncaud-', 'audToaud-', 'audMixaud-'],
                           'lan': ['eng', 'spa'],
                           'video': ['vidToaud-', 'vidToima-', 'vidTovid-'],
                           'application': ['pdfToima-']
                           }

    def validate_input(self, file_name, method):
        """Validates the converter input, is not none, is not empty, is str, is a file and has the correct mime type"""
        CommonValidator(file_name, method).common_validate()
        file_mime_type = MimeTypeGetter(file_name).get_mime_type()
        if not Path(file_name).is_file():
            raise InvalidInputException(f"Invalid input: is not a file - {method} - validate_input()")
        if not (method in self.extensions[file_mime_type]):
            raise InvalidInputException(f"Invalid input type - {method} - validate_input()")

    def validate_output(self, extension, method):
        """Validates the converter output, is not none, is not empty, is str, is a correct extension"""
        CommonValidator(extension, method).common_validate()
        extension_type = method[-4:-1]
        extension = extension[-3:]
        if not (extension in self.extensions[extension_type]):
            raise InvalidInputException(f"Invalid output extension -{method}")

    def validate_multiplier_str(self, multiplier, method):
        """Validates the converter multiplier, is not none, is not empty, is str, and is a numeric str"""
        CommonValidator(multiplier, method).common_validate()
        try:
            int(multiplier)
        except Exception as error:
            raise InvalidInputException("Invalid parameter: the parameter value is not valid -" + method)

    def validate_multiplier_int(self, multiplier, method):
        """Validates the converter multiplier, is not none, is not empty, is str, and is a numeric str"""
        CommonValidator(multiplier, method).int_validate()
        try:
            int(multiplier)
        except Exception as error:
            raise InvalidInputException("Invalid parameter: the parameter value is not valid -" + method)

    def validate_lang(self, lang, method):
        """Validates the converter selected language, is not none, is not empty, is str, and is a supported language"""
        CommonValidator(lang, method).common_validate()
        parameter_type = method[-4:-1]
        if not (lang in self.extensions[parameter_type]):
            raise InvalidInputException("Invalid parameter: language not supported -" + method)

    def validate_directory(self, path, method):
        """Validates the directory, is not none, is not empty, is str, and exist"""
        CommonValidator(path, method).common_validate()
        directory_path = path.split('\\')[0:-1]
        directory_path = "\\".join(directory_path)
        if not Path(directory_path).is_dir():
            raise InvalidInputException(f"Invalid path: the path {directory_path} does not exist - " + method)

    def validate_file(self, file_name, method):
        """Validates the endpoint file, is not none, is not empty and is a file"""
        if file_name is None:
            raise InvalidInputException("Invalid input: the input should not be None type - " + method)
        if not file_name:
            raise InvalidInputException("Invalid input: the input is empty" + method)
        if type(file_name) != FileStorage:
            raise InvalidInputException("Invalid input: the input type is not valid" + method)
        #try:
        #    method in self.extensions[file_name.mimetype.split('/')[0]]
        #except Exception as error:
        #    raise InvalidInputException(f"Invalid input type -{method}")
