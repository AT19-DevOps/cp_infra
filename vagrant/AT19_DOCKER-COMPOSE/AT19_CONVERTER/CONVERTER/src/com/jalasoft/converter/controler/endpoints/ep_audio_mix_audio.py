#
# @ep_audio_mix_audio.py Copyright (c) 2023 Jalasoft.
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

import os
from flask import request
from flask_restful import Resource
from werkzeug.utils import secure_filename
from common.command_line import Command
from common.exception.convert_exception import ConvertException
from config import UPLOAD_FOLDER
from config import RESPONSE_FOLDER
from config import DOWNLOAD_DIR
from controler.mange_request import ManageData
from model.audio.audio_mix_audio import MixAudio


class AudioMixAudio(Resource):
    """Defines audio mix audio class"""

    def post(self):
        """Mixes two audios"""
        try:
            files, checksum = ManageData().generate_path('audMixaud-')

            if files:
                file_in, file_in_2, file_out, url = files[0], files[1], files[2], files[3]
                Command(MixAudio([file_in, file_in_2], file_out).convert()).run_cmd()
                response = {'download_URL': url}
                return response, 200
            else:
                response = {'error message': 'File is corrupted',
                            'checksum': checksum}
                return response, 400
        except ConvertException as error:
            response = {'error_message': error.get_message()}
            return response, 400
