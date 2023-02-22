#
# @test_image_flip.py Copyright (c) 2023 Jalasoft.
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
from CONVERTER.src.com.jalasoft.converter.model.image.image_flip import ImageFlip

class TestImageFlip(unittest.TestCase):
    """Defines unit tests for image_flip.py module"""
    def test_image_flip_valid_data(self):
        """Test the happy path"""
        image_flip = ImageFlip(r'E:\Users\Leo\AT\Programming\AT19_CONVERTER\AT19_CONVERTER\AT19_CONVERTER_UT\AT19_CONVERTER\CONVERTER\test\com\resources\Image.jpg', r'../../../resources/Image.jpg')
        expected = r'magick E:\Users\Leo\AT\Programming\AT19_CONVERTER\AT19_CONVERTER\AT19_CONVERTER_UT\AT19_CONVERTER\CONVERTER\test\com\resources\Image.jpg -flip ../../../resources/Image.jpg'
        self.assertEqual(expected, image_flip.convert())

    def test_image_flip_none_input(self):
        """Test when input is None"""
        image_flip = ImageFlip(None, r'..\..\..\resources\Image.jpg')
        with self.assertRaises(InvalidInputException):
            image_flip.convert()

    def test_image_flip_none_output(self):
        """Test when output is None"""
        image_flip = ImageFlip(r'..\..\..\resources\Image.png', None)
        with self.assertRaises(InvalidInputException):
            image_flip.convert()

    def test_image_flip_null_input(self):
        """Test when input is null"""
        image_flip = ImageFlip('', r'..\..\..\resources\Image.jpg')
        with self.assertRaises(InvalidInputException):
            image_flip.convert()

    def test_image_flip_null_output(self):
        """Test when output is null"""
        image_flip = ImageFlip(r'..\..\..\resources\Image.png', '')
        with self.assertRaises(InvalidInputException):
            image_flip.convert()

    def test_image_flip_no_str_output(self):
        """Test when output is not str"""
        image_flip = ImageFlip(r'..\..\..\resources\Image.png', False)
        with self.assertRaises(InvalidInputException):
            image_flip.convert()

    def test_image_flip_no_str_input(self):
        """Test when input is not a str"""
        image_flip = ImageFlip(2, r'..\..\..\resources\Image.jpg')
        with self.assertRaises(InvalidInputException):
            image_flip.convert()

    def test_image_flip_no_file(self):
        """Test when input has not file"""
        image_flip = ImageFlip(r'..\..\..\resources\ ', r'..\..\..\resources\Image.jpg')
        with self.assertRaises(InvalidInputException):
            image_flip.convert()

    def test_image_flip_invalid_extension_input(self):
        """Test when input is an invalid extension"""
        image_flip = ImageFlip(r'..\..\..\resources\navidad.mp3', r'..\..\..\resources\Image.jpg')
        with self.assertRaises(InvalidInputException):
            image_flip.convert()

    def test_image_flip_invalid_extension_output(self):
        """Test when output is an invalid extension"""
        image_flip = ImageFlip(r'..\..\..\resources\Image.png', r'..\..\..\resources\navidad.mp3')
        with self.assertRaises(InvalidInputException):
            image_flip.convert()

    def test_image_flip_invalid_output_path(self):
        """Test whe the output path is not valid"""
        image_flip = ImageFlip(r'..\..\..\resources\Image.png', r'..\..\..\rerces\Image.jpg')
        with self.assertRaises(InvalidInputException):
            image_flip.convert()

    def test_image_flip_invalid_input_path(self):
        """Test when input path does not exist"""
        image_flip = ImageFlip(r'..\..\..\resourrrcceess\Image.jpg', r'..\..\..\resources\Image.jpg')
        with self.assertRaises(InvalidInputException):
            image_flip.convert()
