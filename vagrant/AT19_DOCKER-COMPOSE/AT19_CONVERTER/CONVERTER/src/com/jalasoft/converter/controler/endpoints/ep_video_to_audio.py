#
# @ep_video_to_audio.py Copyright (c) 2023 Jalasoft.
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

from flask_restful import Resource
from common.command_line import Command
from common.exception.convert_exception import ConvertException
from controler.mange_request import ManageData
from model.audio.audio_extract_audio import ExtractAudio


class VideoToAudio(Resource):
    """Defines video to audio class"""
    def post(self):
        """Extracts the audio from the video"""
        try:
            files, checksum = ManageData().generate_path('vidToaud-')
            if files:
                file_in, file_out, url = files[0], files[1], files[2]
                Command(ExtractAudio(file_in, file_out).convert()).run_cmd()
                return {'download_URL': url}
            else:
                response = {'error message': 'File is corrupted',
                            'checksum': checksum}
                return response, 400
        except ConvertException as error:
            response = {'error_message': error.get_message()}
            return response, 400
