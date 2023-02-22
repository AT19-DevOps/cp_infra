#
# @get_file_type.py Copyright (c) 2023 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# # All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from common.command_line import Command


class MimeTypeGetter:
    """ Inherits Converter criteria"""

    def __init__(self, input_file):
        self.input_file = input_file

    def mime_type_command(self) -> str:
        """Obtains the command for file MIME type"""
        command_line = ['exiftool', '-MIMEType', f'{self.input_file}']
        return " ".join(command_line)

    def get_mime_type(self) -> str:
        """Obtains the file MIME Type"""
        command = Command(self.mime_type_command()).run_cmd()
        mime_type = command.decode('utf-8').split(': ')[1].split('/')[0]
        return mime_type
