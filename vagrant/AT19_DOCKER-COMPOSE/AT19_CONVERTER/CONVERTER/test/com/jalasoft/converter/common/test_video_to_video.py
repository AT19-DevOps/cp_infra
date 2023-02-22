#
# @test_video_to_video.py Copyright (c) 2023 Jalasoft.
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
from CONVERTER.src.com.jalasoft.converter.model.video.video_to_video import VideoToVideo

class TestVideoConvert(unittest.TestCase):
    """Defines unit tests for image_flip.py module"""

    def test_video_to_video_valid_data(self):
        """Test the happy path"""
        video_to_video = VideoToVideo(r'E:\Users\Leo\AT\Programming\AT19_CONVERTER\AT19_CONVERTER\AT19_CONVERTER_UT\AT19_CONVERTER\CONVERTER\test\com\resources\Whats.mp4', r'../../../resources/Whats.avi')
        expected = r'ffmpeg -i E:\Users\Leo\AT\Programming\AT19_CONVERTER\AT19_CONVERTER\AT19_CONVERTER_UT\AT19_CONVERTER\CONVERTER\test\com\resources\Whats.mp4 -c:v copy -c:a copy -y ../../../resources/Whats.avi'
        self.assertEqual(expected, video_to_video.convert())

    def test_video_to_video_none_input(self):
        """Test when input is None"""
        video_to_video = VideoToVideo(None, r'..\..\..\resources\Whats.avi')
        with self.assertRaises(InvalidInputException):
            video_to_video.convert()

    def test_video_to_video_none_output(self):
        """Test when output is None"""
        video_to_video = VideoToVideo(r'..\..\..\resources\Whats.mp4', None)
        with self.assertRaises(InvalidInputException):
            video_to_video.convert()

    def test_video_to_video_null_input(self):
        """Test when input is null"""
        video_to_video = VideoToVideo('', r'..\..\..\resources\Whats.avi')
        with self.assertRaises(InvalidInputException):
            video_to_video.convert()

    def test_video_to_video_null_output(self):
        """Test when output is null"""
        video_to_video = VideoToVideo(r'..\..\..\resources\Whats.mp4', '')
        with self.assertRaises(InvalidInputException):
            video_to_video.convert()

    def test_video_to_video_no_str_output(self):
        """Test when output is not str"""
        video_to_video = VideoToVideo(r'..\..\..\resources\Whats.mp4', 3)
        with self.assertRaises(InvalidInputException):
            video_to_video.convert()

    def test_video_to_video_no_str_input(self):
        """Test when input is not a str"""
        video_to_video = VideoToVideo(1, r'..\..\..\resources\Whats.avi')
        with self.assertRaises(InvalidInputException):
            video_to_video.convert()

    def test_video_to_video_no_file(self):
        """Test when input has not file"""
        video_to_video = VideoToVideo(r'..\..\..\resources\ ', r'..\..\..\resources\Whats.avi')
        with self.assertRaises(InvalidInputException):
            video_to_video.convert()

    def test_video_to_video_invalid_extension_input(self):
        """Test when input is an invalid extension"""
        video_to_video = VideoToVideo(r'..\..\..\resources\notification.wav', r'..\..\..\resources\Whats.avi')
        with self.assertRaises(InvalidInputException):
            video_to_video.convert()

    def test_video_to_video_invalid_extension_output(self):
        """Test when output is an invalid extension"""
        video_to_video= VideoToVideo(r'..\..\..\resources\Whats.mp4', r'..\..\..\resources\Whats.mp3')
        with self.assertRaises(InvalidInputException):
            video_to_video.convert()

    def test_video_to_video_invalid_output_path(self):
        """Test whe the output path is not valid"""
        video_to_video = VideoToVideo(r'..\..\..\resources\Whats.mp4', r'..\..\..\resourcess\Whats.avi')
        with self.assertRaises(InvalidInputException):
            video_to_video.convert()

    def test_video_to_video_invalid_input_path(self):
        """Test when input path does not exist"""
        video_to_video = VideoToVideo(r'..\..\..\resourcess\Whats.mp4', r'..\..\..\resources\Whats.avi')
        with self.assertRaises(InvalidInputException):
            video_to_video.convert()
