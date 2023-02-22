#
# @pdf_to_image.py Copyright (c) 2023 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# # All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from model.converter import Converter


class PdfImage(Converter):
    """Inherits Converter criteria"""

    def __init__(self, input_file, output_file, quality):
        super().__init__(input_file, output_file)
        self.quality = quality

    def convert(self) -> str:
        """Converts all pages of PDF to images, return the command line"""
        command_line = ['convert', '-density', '150', '-antialias', f'{self.input_file}', '-resize', '1024x',
                        '-quality', f'{self.quality}', f'{self.output_file}']
        return " ".join(command_line)

