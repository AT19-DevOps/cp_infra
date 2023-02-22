#
# @test_image_to_image.py Copyright (c) 2023 Jalasoft.
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
from CONVERTER.src.com.jalasoft.converter.model.image.image_to_images import ImageConverter


class TestImageConverter(unittest.TestCase):
    """Defines unit tests for image_to_images.py module"""
    def test_image_to_image_valid_data(self):
        """Test the happy path"""
        image_converter = ImageConverter(r'E:\Users\Leo\AT\Programming\AT19_CONVERTER\AT19_CONVERTER\AT19_CONVERTER_UT\AT19_CONVERTER\CONVERTER\test\com\resources\Image.jpg', r'../../../resources/Image.jpg')
        expected = r'magick E:\Users\Leo\AT\Programming\AT19_CONVERTER\AT19_CONVERTER\AT19_CONVERTER_UT\AT19_CONVERTER\CONVERTER\test\com\resources\Image.jpg ../../../resources/Image.jpg'
        self.assertEqual(expected, image_converter.convert())

    def test_image_to_image_none_input(self):
        """Test when input is None"""
        image_converter = ImageConverter(None, r'..\..\..\resources\Image.jpg')
        with self.assertRaises(InvalidInputException):
            image_converter.convert()

    def test_image_to_image_none_output(self):
        """Test when output is None"""
        image_converter = ImageConverter(r'..\..\..\resources\Image.png', None)
        with self.assertRaises(InvalidInputException):
            image_converter.convert()

    def test_image_to_image_null_input(self):
        """Test when input is null"""
        image_converter = ImageConverter('', r'..\..\..\resources\Image.jpg')
        with self.assertRaises(InvalidInputException):
            image_converter.convert()

    def test_image_to_image_null_output(self):
        """Test when output is null"""
        image_converter = ImageConverter(r'..\..\..\resources\Image.png', '')
        with self.assertRaises(InvalidInputException):
            image_converter.convert()

    def test_image_to_image_no_str_output(self):
        """Test when output is not str"""
        image_converter = ImageConverter(r'..\..\..\resources\Image.png', False)
        with self.assertRaises(InvalidInputException):
            image_converter.convert()

    def test_image_to_image_no_str_input(self):
        """Test when input is not a str"""
        image_converter = ImageConverter(2, r'..\..\..\resources\Image.jpg')
        with self.assertRaises(InvalidInputException):
            image_converter.convert()

    def test_image_to_image_no_file(self):
        """Test when input has not file"""
        image_converter = ImageConverter(r'..\..\..\resources\ ', r'..\..\..\resources\Image.jpg')
        with self.assertRaises(InvalidInputException):
            image_converter.convert()

    def test_image_to_image_invalid_extension_input(self):
        """Test when input is an invalid extension"""
        image_converter = ImageConverter(r'..\..\..\resources\navidad.mp3', r'..\..\..\resources\Image.jpg')
        with self.assertRaises(InvalidInputException):
            image_converter.convert()

    def test_image_to_image_invalid_extension_output(self):
        """Test when output is an invalid extension"""
        image_converter = ImageConverter(r'..\..\..\resources\Image.png', r'..\..\..\resources\navidad.mp3')
        with self.assertRaises(InvalidInputException):
            image_converter.convert()

    def test_image_to_image_invalid_output_path(self):
        """Test whe the output path is not valid"""
        image_converter = ImageConverter(r'..\..\..\resources\Image.png', r'..\..\..\resces\Image.jpg')
        with self.assertRaises(InvalidInputException):
            image_converter.convert()

    def test_image_to_image_invalid_input_path(self):
        """Test whe the input path is not valid"""
        image_converter = ImageConverter(r'..\..\..\res\Image.png', r'..\..\..\resources\Image.jpg')
        with self.assertRaises(InvalidInputException):
            image_converter.convert()
