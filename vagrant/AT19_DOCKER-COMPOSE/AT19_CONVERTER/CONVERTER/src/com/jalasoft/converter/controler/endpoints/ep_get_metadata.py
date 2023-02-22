#
# @ep_get_metadata.py Copyright (c) 2023 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#
import os
from dotenv import load_dotenv
from flask import request
from flask_restful import Resource
from werkzeug.utils import secure_filename
from common.command_line import Command
from common.exception.convert_exception import ConvertException
from common.get_metadata import MetadataGetter
from config import UPLOAD_FOLDER, RESPONSE_FOLDER

load_dotenv()


class GetMetadata(Resource):
    """Get Metadata class"""

    def post(self):
        """Get Metadata from a file"""
        try:
            file_prefix = 'getMeta-'
            input_file = request.files["input_file"]
            if input_file:
                filename = secure_filename(input_file.filename)
                input_file.save(os.path.join(UPLOAD_FOLDER, filename))
                in_file = os.path.join(UPLOAD_FOLDER, filename)
                out_file = os.path.join(RESPONSE_FOLDER, file_prefix + filename.split('.')[0] + '.json')
                port = os.getenv("CONVERTER_PORT")
                url = os.getenv("CONVERTER_HOST")
                download_url = f"{url}:{port}/download?file_name={os.path.basename(out_file)}"
                Command(MetadataGetter(in_file, out_file).convert()).run_cmd()
                return {'download_URL': download_url}
            else:
                response = {'error message': 'File is corrupted'}
                return response, 400
        except ConvertException as error:
            response = {'error_message': error.get_message()}
            return response, 400
