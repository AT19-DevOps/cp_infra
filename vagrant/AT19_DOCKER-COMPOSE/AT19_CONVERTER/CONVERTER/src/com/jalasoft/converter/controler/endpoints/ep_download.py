#
# @ep_download.py Copyright (c) 2023 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
#
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
from flask import send_from_directory
from config import RESPONSE_FOLDER


class Download(Resource):
    """Defines download file method --> url"""
    def get(self):
        """Download file"""
        file_name = request.args["file_name"]
        return send_from_directory(directory = RESPONSE_FOLDER, path = file_name, as_attachment = True)