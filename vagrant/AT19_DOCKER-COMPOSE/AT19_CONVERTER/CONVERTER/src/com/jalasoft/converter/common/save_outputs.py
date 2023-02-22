#
# @save_outputs.py Copyright (c) 2023 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from model.converter import Converter


class SaveOutput(Converter):
    """Inherits Converter criteria"""
    def __init__(self, input_file, output_file):
        super().__init__(input_file, output_file)

    def convert(self):
        """Creates and executes command to save an audio file in a specific path"""
        cmd = f'MOVE "{self.input_file}" "{self.output_file}"'
        return cmd
