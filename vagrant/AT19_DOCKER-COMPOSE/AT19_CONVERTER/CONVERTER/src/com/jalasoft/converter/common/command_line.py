#
# @command_line.py Copyright (c) 2023 Jalasoft.
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

import subprocess
import platform
from common.exception.command_exception import CommandException


class Command:
    """Defines Command class criteria"""

    def __init__(self, cmd):
        self.cmd = cmd

    def run_cmd(self):
        """Executes the command given"""
        try:
            cmd_line = self.cmd
            if platform.system() == 'Linux':
                cmd_line = str(cmd_line).replace('magick', 'convert')
            run = subprocess.check_output(cmd_line, shell=True)
            return run
        except Exception as error:
            raise CommandException('Error executing the command in console')
