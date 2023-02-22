#
# @image_flip.py Copyright (c) 2023 Jalasoft.
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
from common.exception.converter_exception import ConverterException
from common.valid_data import Validations


class ImageFlip(Converter):
    """ Inherits Converter criteria"""
    def __init__(self, input_file, output_file):
        super().__init__(input_file, output_file)

    def convert(self) -> str:
        """Flips image horizontally, returns the command line"""
        Validations().validate_directory(self.input_file, 'imaFlima-')
        Validations().validate_input(self.input_file, 'imaFlima-')
        Validations().validate_output(self.output_file, 'imaFlima-')
        Validations().validate_directory(self.output_file, 'imaFlima-')
        try:
            command_line = ['magick', f'{self.input_file}', '-flip', f'{self.output_file}']
            return " ".join(command_line)
        except Exception as error:
            raise ConverterException('Create Image Flip command error')
