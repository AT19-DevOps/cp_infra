#
# @test_audio_extract_audio.py Copyright (c) 2023 Jalasoft.
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
from CONVERTER.src.com.jalasoft.converter.model.audio.audio_extract_audio import ExtractAudio

class TestAudioExtract(unittest.TestCase):
    """Defines unit tests for image_flip.py module"""

    def test_audio_extract_valid_data(self):
        """Test the happy path"""
        audio_extract = ExtractAudio(r'E:\Users\Leo\AT\Programming\AT19_CONVERTER\AT19_CONVERTER\AT19_CONVERTER_UT\AT19_CONVERTER\CONVERTER\test\com\resources\Whats.mp4', r'../../../resources/Whats.mp3')
        expected = r'ffmpeg -i E:\Users\Leo\AT\Programming\AT19_CONVERTER\AT19_CONVERTER\AT19_CONVERTER_UT\AT19_CONVERTER\CONVERTER\test\com\resources\Whats.mp4 -vn ../../../resources/Whats.mp3'
        self.assertEqual(expected, audio_extract.convert())

    def test_audio_extract_none_input(self):
        """Test when input is None"""
        audio_extract = ExtractAudio(None, r'..\..\..\resources\Whats.mp3')
        with self.assertRaises(InvalidInputException):
            audio_extract.convert()

    def test_audio_extract_none_output(self):
        """Test when output is None"""
        audio_extract = ExtractAudio(r'..\..\..\resources\Whats.mp4', None)
        with self.assertRaises(InvalidInputException):
            audio_extract.convert()

    def test_audio_extract_null_input(self):
        """Test when input is null"""
        audio_extract = ExtractAudio('', r'..\..\..\resources\Whats.mp3')
        with self.assertRaises(InvalidInputException):
            audio_extract.convert()

    def test_audio_convert_null_output(self):
        """Test when output is null"""
        audio_extract = ExtractAudio(r'..\..\..\resources\Whats.mp4', '')
        with self.assertRaises(InvalidInputException):
            audio_extract.convert()

    def test_audio_extract_no_str_output(self):
        """Test when output is not str"""
        audio_extract = ExtractAudio(r'..\..\..\resources\Whats.mp4', False)
        with self.assertRaises(InvalidInputException):
            audio_extract.convert()

    def test_audio_extract_no_str_input(self):
        """Test when input is not a str"""
        audio_extract = ExtractAudio(2, r'..\..\..\resources\Whats.mp3')
        with self.assertRaises(InvalidInputException):
            audio_extract.convert()

    def test_audio_extract_no_file(self):
        """Test when input has not file"""
        audio_extract = ExtractAudio(r'..\..\..\resources\ ', r'..\..\..\resources\Whats.mp3')
        with self.assertRaises(InvalidInputException):
            audio_extract.convert()

    def test_audio_extract_invalid_extension_input(self):
        """Test when input is an invalid extension"""
        audio_extract = ExtractAudio(r'..\..\..\resources\Image.jpg', r'..\..\..\resources\Whats.mp3')
        with self.assertRaises(InvalidInputException):
            audio_extract.convert()

    def test_audio_convert_invalid_extension_output(self):
        """Test when output is an invalid extension"""
        audio_extract = ExtractAudio(r'..\..\..\resources\Whats.mp4', r'..\..\..\resources\Image.jpg')
        with self.assertRaises(InvalidInputException):
            audio_extract.convert()

    def test_audio_extract_invalid_output_path(self):
        """Test whe the output path is not valid"""
        audio_extract = ExtractAudio(r'..\..\..\resources\Whats.mp4', r'..\..\..\resourrces\Whats.mp3')
        with self.assertRaises(InvalidInputException):
            audio_extract.convert()

    def test_audio_cextract_invalid_input_path(self):
        """Test when input path does not exist"""
        audio_extract = ExtractAudio(r'..\..\..\resourcess\Whats.mp4', r'..\..\..\resources\Whats.mp3')
        with self.assertRaises(InvalidInputException):
            audio_extract.convert()
