#
# @audio_mix_audio.py Copyright (c) 2023 Jalasoft.
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
from common.exception.converter_exception import ConverterException
from common.valid_data import Validations


class MixAudio(Converter):
    """Inherits Converter criteria"""
    def __init__(self, input_file, output_file):
        super().__init__(input_file, output_file)

    def convert(self):
        Validations().validate_output(self.output_file, 'audMixaud-')
        Validations().validate_directory(self.output_file, 'audMixaud-')
        list = ['ffmpeg']
        for element in self.input_file:
            Validations().validate_directory(element, 'audMixaud-')
            Validations().validate_input(element, 'audMixaud-')
            list.append(' -i ' + element)
        list.append(' -filter_complex amerge ' + self.output_file)
        try:
            cmd = ''.join(list)
            return cmd
        except Exception as error:
            raise ConverterException('Create Audio Convert command error')
