#
# @test_video_converter.py Copyright (c) 2023 Jalasoft.
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
from CONVERTER.src.com.jalasoft.converter.model.video.vconverter import VideoToImages


class TestImageResize(unittest.TestCase):
    """Defines unit tests for image_resize.py module"""
    def test_video_converter_valid_data(self):
        """Test the happy path"""
        video_converter = VideoToImages(r'E:\Users\Leo\AT\Programming\AT19_CONVERTER\AT19_CONVERTER\AT19_CONVERTER_UT\AT19_CONVERTER\CONVERTER\test\com\resources\Whats.mp4', r'../../../resources/Whats.jpg', '2')
        expected = r'ffmpeg -i E:\Users\Leo\AT\Programming\AT19_CONVERTER\AT19_CONVERTER\AT19_CONVERTER_UT\AT19_CONVERTER\CONVERTER\test\com\resources\Whats.mp4 -r 2 ../../../resources/Whats.jpg'
        self.assertEqual(expected, video_converter.convert())

    def test_video_converter_none_input(self):
        """Test when input is None"""
        video_converter = VideoToImages(None, r'..\..\..\resources\Whats.jpg', '1')
        with self.assertRaises(InvalidInputException):
            video_converter.convert()

    def test_video_converter_none_output(self):
        """Test when output is None"""
        video_converter = VideoToImages(r'..\..\..\resources\Whats.mp4', None, '1')
        with self.assertRaises(InvalidInputException):
            video_converter.convert()

    def test_video_converter_null_input(self):
        """Test when input is null"""
        video_converter = VideoToImages('', r'..\..\..\resources\Whats.jpg', '1')
        with self.assertRaises(InvalidInputException):
            video_converter.convert()

    def test_video_converter_null_output(self):
        """Test when output is null"""
        video_converter = VideoToImages(r'..\..\..\resources\Whats.mp4', '', '1')
        with self.assertRaises(InvalidInputException):
            video_converter.convert()

    def test_video_converter_no_str_output(self):
        """Test when output is not str"""
        video_converter = VideoToImages(r'..\..\..\resources\Whats.mp4', 3, '1')
        with self.assertRaises(InvalidInputException):
            video_converter.convert()

    def test_video_converter_no_str_input(self):
        """Test when input is not a str"""
        video_converter = VideoToImages(False, r'..\..\..\resources\Whats.jpg', '1')
        with self.assertRaises(InvalidInputException):
            video_converter.convert()

    def test_video_converter_no_file(self):
        """Test when input has not file"""
        video_converter = VideoToImages(r'..\..\..\resources\ ', r'..\..\..\resources\Whats.jpg', '1')
        with self.assertRaises(InvalidInputException):
            video_converter.convert()

    def test_video_converter_invalid_extension_input(self):
        """Test when input is an invalid extension"""
        video_converter = VideoToImages(r'..\..\..\resources\Image.jpg', r'..\..\..\resources\Whats.jpg', '1')
        with self.assertRaises(InvalidInputException):
            video_converter.convert()

    def test_video_converter_invalid_extension_output(self):
        """Test when output is an invalid extension"""
        video_converter = VideoToImages(r'..\..\..\resources\Whats.mp4', r'..\..\..\resources\Whats.mp3', '1')
        with self.assertRaises(InvalidInputException):
            video_converter.convert()

    def test_video_converter_none_fps(self):
        """Test when multiplier is None"""
        video_converter = VideoToImages(r'..\..\..\resources\Whats.mp4', r'..\..\..\resources\Whats.jpg', None)
        with self.assertRaises(InvalidInputException):
            video_converter.convert()

    def test_video_converter_null_fps(self):
        """Test when multiplier is null"""
        video_converter = VideoToImages(r'..\..\..\resources\Whats.mp4', r'..\..\..\resources\Whats.jpg', '')
        with self.assertRaises(InvalidInputException):
            video_converter.convert()

    def test_video_converter_no_str_fps(self):
        """Test when multiplier is not str"""
        video_converter = VideoToImages(r'..\..\..\resources\Whats.mp4', r'..\..\..\resources\Whats.jpg', True)
        with self.assertRaises(InvalidInputException):
            video_converter.convert()

    def test_video_converter_no_num_multiplier(self):
        """Test when multiplier is not numeric str"""
        video_converter = VideoToImages(r'..\..\..\resources\Whats.mp4', r'..\..\..\resources\Whats.jpg', 'p')
        with self.assertRaises(InvalidInputException):
            video_converter.convert()

    def test_video_converter_invalid_output_path(self):
        """Test whe the output path is not valid"""
        image_resize = VideoToImages(r'..\..\..\resources\Whats.mp4', r'..\..\..\resourcess\Whats.jpg', '1')
        with self.assertRaises(InvalidInputException):
            image_resize.convert()

    def test_video_converter_invalid_input_path(self):
        """Test when input path does not exist"""
        video_converter = VideoToImages(r'..\..\..\resourcess\Whats.mp4', r'..\..\..\resources\Whats.jpg', '1')
        with self.assertRaises(InvalidInputException):
            video_converter.convert()
