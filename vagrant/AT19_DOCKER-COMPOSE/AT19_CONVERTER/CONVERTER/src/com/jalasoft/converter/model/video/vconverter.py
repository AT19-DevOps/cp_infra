#
# @vconverter.py Copyright (c) 2022 Jalasoft.
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

from model.converter import Converter
from common.exception.converter_exception import ConverterException
from common.valid_data import Validations


class VideoToImages(Converter):
    """Converts any video format to a set of any format images""" 
    def __init__(self, input_file, output_file, fps):

        super().__init__(input_file, output_file)
        self.fps = fps

    def convert(self) -> str:
        """Converts video to a set of images"""
        Validations().validate_directory(self.input_file, 'vidToima-')
        Validations().validate_input(self.input_file, 'vidToima-')
        Validations().validate_output(self.output_file, 'vidToima-')
        Validations().validate_directory(self.output_file, 'vidToima-')
        Validations().validate_multiplier_str(self.fps, 'vidToima-')
        try:
            cmd = " ".join(['ffmpeg', '-i', self.input_file, '-r', self.fps, self.output_file])
            return cmd
        except Exception as error:
            raise ConverterException('Create Audio Convert command error')

