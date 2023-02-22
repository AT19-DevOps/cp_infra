#
# @test_image_resize.py Copyright (c) 2023 Jalasoft.
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
from CONVERTER.src.com.jalasoft.converter.model.image.image_resize import ImageResize


class TestImageResize(unittest.TestCase):
    """Defines unit tests for image_resize.py module"""
    def test_image_resize_valid_data(self):
        """Test the happy path"""
        image_resize = ImageResize(r'E:\Users\Leo\AT\Programming\AT19_CONVERTER\AT19_CONVERTER\AT19_CONVERTER_UT\AT19_CONVERTER\CONVERTER\test\com\resources\Image.png', r'../../../resources/Image.jpg', '50')
        expected = r'magick E:\Users\Leo\AT\Programming\AT19_CONVERTER\AT19_CONVERTER\AT19_CONVERTER_UT\AT19_CONVERTER\CONVERTER\test\com\resources\Image.png -resize 50 ../../../resources/Image.jpg'
        self.assertEqual(expected, image_resize.convert())

    def test_image_resize_none_input(self):
        """Test when input is None"""
        image_resize = ImageResize(None, r'..\..\..\resources\Image.jpg', '50')
        with self.assertRaises(InvalidInputException):
            image_resize.convert()

    def test_image_resize_none_output(self):
        """Test when output is None"""
        image_resize = ImageResize(r'..\..\..\resources\Image.png', None, '50')
        with self.assertRaises(InvalidInputException):
            image_resize.convert()

    def test_image_resize_null_input(self):
        """Test when input is null"""
        image_resize = ImageResize('', r'..\..\..\resources\Image.jpg', '50')
        with self.assertRaises(InvalidInputException):
            image_resize.convert()

    def test_image_resize_null_output(self):
        """Test when output is null"""
        image_resize = ImageResize(r'..\..\..\resources\Image.png', '', '50')
        with self.assertRaises(InvalidInputException):
            image_resize.convert()

    def test_image_resize_no_str_output(self):
        """Test when output is not str"""
        image_resize = ImageResize(r'..\..\..\resources\Image.png', False, '50')
        with self.assertRaises(InvalidInputException):
            image_resize.convert()

    def test_image_resize_no_str_input(self):
        """Test when input is not a str"""
        image_resize = ImageResize(2, r'..\..\..\resources\Image.jpg', '50')
        with self.assertRaises(InvalidInputException):
            image_resize.convert()

    def test_image_resize_no_file(self):
        """Test when input has not file"""
        image_resize = ImageResize(r'..\..\..\resources\ ', r'..\..\..\resources\Image.jpg', '50')
        with self.assertRaises(InvalidInputException):
            image_resize.convert()

    def test_image_resize_invalid_extension_input(self):
        """Test when input is an invalid extension"""
        image_resize = ImageResize(r'..\..\..\resources\navidad.mp3', r'..\..\..\resources\Image.jpg', '50')
        with self.assertRaises(InvalidInputException):
            image_resize.convert()

    def test_image_resize_invalid_extension_output(self):
        """Test when output is an invalid extension"""
        image_resize = ImageResize(r'..\..\..\resources\Image.png', r'..\..\..\resources\navidad.mp3', '50')
        with self.assertRaises(InvalidInputException):
            image_resize.convert()

    def test_image_resize_none_multiplier(self):
        """Test when multiplier is None"""
        image_resize = ImageResize(r'..\..\..\resources\Image.png', r'..\..\..\resources\Image.jpg', None)
        with self.assertRaises(InvalidInputException):
            image_resize.convert()

    def test_image_resize_null_multiplier(self):
        """Test when multiplier is null"""
        image_resize = ImageResize(r'..\..\..\resources\Image.png', r'..\..\..\resources\Image.jpg', '')
        with self.assertRaises(InvalidInputException):
            image_resize.convert()

    def test_image_resize_no_str_multiplier(self):
        """Test when multiplier is not str"""
        image_resize = ImageResize(r'..\..\..\resources\Image.png', r'..\..\..\resources\Image.jpg', 3)
        with self.assertRaises(InvalidInputException):
            image_resize.convert()

    def test_image_resize_no_num_multiplier(self):
        """Test when multiplier is not numeric str"""
        image_resize = ImageResize(r'..\..\..\resources\Image.png', r'..\..\..\resources\Image.jpg', 'dos')
        with self.assertRaises(InvalidInputException):
            image_resize.convert()

    def test_image_resize_invalid_output_path(self):
        """Test whe the output path is not valid"""
        image_resize = ImageResize(r'..\..\..\resources\Image.png', r'..\..\..\resoes\Image.jpg', '50')
        with self.assertRaises(InvalidInputException):
            image_resize.convert()

    def test_image_resize_invalid_input_path(self):
        """Test when input path does not exist"""
        image_resize = ImageResize(r'..\..\..\resdddources\Image.png', r'..\..\..\resources\Image.jpg', '50')
        with self.assertRaises(InvalidInputException):
            image_resize.convert()
