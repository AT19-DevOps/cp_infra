#
# @test_audio_mix.py Copyright (c) 2023 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# # All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

import unittest
from CONVERTER.src.com.jalasoft.converter.common.exception.input_exception import InvalidInputException
from CONVERTER.src.com.jalasoft.converter.model.audio.audio_mix_audio import MixAudio

class TestAudioMix(unittest.TestCase):
    """Defines unit tests for image_flip.py module"""

    def test_audio_mix_valid_data(self):
        """Test the happy path"""
        audio_mix = MixAudio([r'E:\Users\Leo\AT\Programming\AT19_CONVERTER\AT19_CONVERTER\AT19_CONVERTER_UT\AT19_CONVERTER\CONVERTER\test\com\resources\notification.wav', r'E:\Users\Leo\AT\Programming\AT19_CONVERTER\AT19_CONVERTER\AT19_CONVERTER_UT\AT19_CONVERTER\CONVERTER\test\com\resources\navidad.mp3'],
                                 r'../../../resources/notification.mp3')
        expected = r'ffmpeg -i E:\Users\Leo\AT\Programming\AT19_CONVERTER\AT19_CONVERTER\AT19_CONVERTER_UT\AT19_CONVERTER\CONVERTER\test\com\resources\notification.wav -i E:\Users\Leo\AT\Programming\AT19_CONVERTER\AT19_CONVERTER\AT19_CONVERTER_UT\AT19_CONVERTER\CONVERTER\test\com\resources\navidad.mp3 -filter_complex amerge ../../../resources/notification.mp3'
        self.assertEqual(expected, audio_mix.convert())

    def test_audio_mix_none_input_1(self):
        """Test when input is None"""
        audio_mix = MixAudio([None, r'..\..\..\resources\navidad.mp3'],
                                 r'..\..\..\resources\notification.mp3')
        with self.assertRaises(InvalidInputException):
            audio_mix.convert()

    def test_audio_mix_none_input_2(self):
        """Test when input is None"""
        audio_mix = MixAudio([r'..\..\..\resources\navidad.mp3', None],
                                 r'..\..\..\resources\notification.mp3')
        with self.assertRaises(InvalidInputException):
            audio_mix.convert()

    def test_audio_mix_none_output(self):
        """Test when output is None"""
        audio_mix = MixAudio([r'..\..\..\resources\notification.wav', r'..\..\..\resources\navidad.mp3'], None)
        with self.assertRaises(InvalidInputException):
            audio_mix.convert()

    def test_audio_mix_null_input_1(self):
        """Test when input is null"""
        audio_mix = MixAudio(['', r'..\..\..\resources\navidad.mp3'],
                                 r'..\..\..\resources\notification.mp3')
        with self.assertRaises(InvalidInputException):
            audio_mix.convert()

    def test_audio_mix_null_input_2(self):
        """Test when input is null"""
        audio_mix = MixAudio([r'..\..\..\resources\navidad.mp3', ''], r'..\..\..\resources\notification.mp3')
        with self.assertRaises(InvalidInputException):
            audio_mix.convert()

    def test_audio_mix_null_output(self):
        """Test when output is null"""
        audio_mix = MixAudio([r'..\..\..\resources\notification.wav', r'..\..\..\resources\navidad.mp3'], '')
        with self.assertRaises(InvalidInputException):
            audio_mix.convert()

    def test_audio_mix_no_str_output(self):
        """Test when output is not str"""
        audio_mix = MixAudio([r'..\..\..\resources\notification.wav', r'..\..\..\resources\navidad.mp3'], False)
        with self.assertRaises(InvalidInputException):
            audio_mix.convert()

    def test_audio_mix_no_str_input_1(self):
        """Test when input is not a str"""
        audio_mix = MixAudio([False, r'..\..\..\resources\navidad.mp3'], r'..\..\..\resources\notification.mp3')
        with self.assertRaises(InvalidInputException):
            audio_mix.convert()

    def test_audio_mix_no_str_input_2(self):
        """Test when input is not a str"""
        audio_mix = MixAudio([r'..\..\..\resources\navidad.mp3', True], r'..\..\..\resources\notification.mp3')
        with self.assertRaises(InvalidInputException):
            audio_mix.convert()

    def test_audio_mix_no_file_1(self):
        """Test when input has not file"""
        audio_mix = MixAudio([r'..\..\..\resources\ ', r'..\..\..\resources\navidad.mp3'],
                                 r'..\..\..\resources\notification.mp3')
        with self.assertRaises(InvalidInputException):
            audio_mix.convert()

    def test_audio_mix_no_file_2(self):
        """Test when input has not file"""
        audio_mix = MixAudio([r'..\..\..\resources\navidad.mp3', r'..\..\..\resources\ '],
                                 r'..\..\..\resources\notification.mp3')
        with self.assertRaises(InvalidInputException):
            audio_mix.convert()

    def test_audio_mix_invalid_extension_input_1(self):
        """Test when input is an invalid extension"""
        audio_mix = MixAudio([r'..\..\..\resources\Image.jpg', r'..\..\..\resources\navidad.mp3'],
                                 r'..\..\..\resources\notification.mp3')
        with self.assertRaises(InvalidInputException):
            audio_mix.convert()

    def test_audio_mix_invalid_extension_input_2(self):
        """Test when input is an invalid extension"""
        audio_mix = MixAudio([r'..\..\..\resources\navidad.mp3', r'..\..\..\resources\Image.jpg'],
                                 r'..\..\..\resources\notification.mp3')
        with self.assertRaises(InvalidInputException):
            audio_mix.convert()

    def test_audio_mix_invalid_extension_output(self):
        """Test when output is an invalid extension"""
        audio_mix = MixAudio([r'..\..\..\resources\notification.wav', r'..\..\..\resources\navidad.mp3'],
                                 r'..\..\..\resources\notification.jpg')
        with self.assertRaises(InvalidInputException):
            audio_mix.convert()

    def test_audio_mix_invalid_output_path(self):
        """Test whe the output path is not valid"""
        audio_mix = MixAudio([r'..\..\..\resources\notification.wav', r'..\..\..\resources\navidad.mp3'],
                                 r'..\..\..\resourcess\notification.mp3')
        with self.assertRaises(InvalidInputException):
            audio_mix.convert()

    def test_audio_mix_invalid_input_path_1(self):
        """Test when input path does not exist"""
        audio_mix = MixAudio([r'..\..\..\resourcess\notification.wav', r'..\..\..\resources\navidad.mp3'],
                                 r'..\..\..\resources\notification.mp3')
        with self.assertRaises(InvalidInputException):
            audio_mix.convert()

    def test_audio_mix_invalid_input_path_2(self):
        """Test when input path does not exist"""
        audio_mix = MixAudio([r'..\..\..\resources\notification.wav', r'..\..\..\resourcess\navidad.mp3'],
                                 r'..\..\..\resources\notification.mp3')
        with self.assertRaises(InvalidInputException):
            audio_mix.convert()