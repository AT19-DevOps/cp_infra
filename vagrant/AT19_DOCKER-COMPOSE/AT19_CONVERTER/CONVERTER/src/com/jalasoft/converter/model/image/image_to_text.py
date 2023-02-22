#
# @image_to_text.py Copyright (c) 2023 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# # All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from common.exception.converter_exception import ConverterException
from common.valid_data import Validations
from model.converter import Converter

class ImageToTextConvert(Converter):
    """ Inherits Converter criteria"""

    def __init__(self, input_file, output_file, lang, output_extension):
        super().__init__(input_file, output_file)
        self.lang = lang
        self.output_extension = output_extension

    def convert(self) -> str:
        """Converts an image with text in a pdf or txt file"""
        Validations().validate_directory(self.input_file, 'imaPdftex-')
        Validations().validate_input(self.input_file, 'imaPdftex-')
        Validations().validate_output(self.output_extension, 'imaPdftex-')
        Validations().validate_lang(self.lang, 'imaPdflan-')
        Validations().validate_directory(self.output_file, 'imaPdftex-')
        try:
            command_line = ['tesseract', f'{self.input_file}', f'{self.output_file}', '-l', self.lang, self.output_extension]
            return " ".join(command_line)
        except Exception as error:
            raise ConverterException('Create Image to text command error')
