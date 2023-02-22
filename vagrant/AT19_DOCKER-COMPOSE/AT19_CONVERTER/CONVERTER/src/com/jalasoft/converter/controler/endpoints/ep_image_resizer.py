#
# @ep_image_resizer.py Copyright (c) 2023 Jalasoft.
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
from flask_restful import Resource
from common.command_line import Command
from common.exception.convert_exception import ConvertException
from controler.mange_request import ManageData
from model.image.image_resize import ImageResize


class ImageResizer(Resource):
    """Defines image to black and white class"""
    def post(self):
        """Convert image to black and white image"""
        try:
            files, checksum = ManageData().generate_path('imaReima-')
            if files:
                file_in, file_out, url = files[0], files[1], files[2]
                new_size = request.form["new_size"]
                Command(ImageResize(file_in, file_out, new_size).convert()).run_cmd()
                response = {'download_URL': url}
                return response, 200
            else:
                response = {'error message': 'File is corrupted',
                            'checksum': checksum}
                return response, 400
        except ConvertException as error:
            response = {'error_message': error.get_message()}
            return response, 400

