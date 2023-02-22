#
# @image_rotate.py Copyright (c) 2023 Jalasoft.
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


class ImageRotate(Converter):
    """ Inherits Converter criteria"""
    def __init__(self, input_file, output_file, grades):
        super().__init__(input_file, output_file)
        self.grades = grades

    def convert(self) -> list:
        """Rotates image clockwise for a given value, returns the command line"""
        Validations().validate_directory(self.input_file, 'imaRoima-')
        Validations().validate_input(self.input_file, 'imaRoima-')
        Validations().validate_output(self.output_file, 'imaRoima-')
        Validations().validate_multiplier_str(self.grades, 'imaRoima-')
        Validations().validate_directory(self.output_file, 'imaRoima-')
        try:
            command_line = ['magick', f'{self.input_file}', '-rotate', f'{self.grades}', f'{self.output_file}']
            return " ".join(command_line)
        except Exception as error:
            raise ConverterException('Create Image Rotate command error')
