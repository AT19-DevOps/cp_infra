#
# @test_imagebw.py Copyright (c) 2023 Jalasoft.
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

from CONVERTER.src.com.jalasoft.converter.model.image.image_bw import ImageBW
from CONVERTER.src.com.jalasoft.converter.common.exception.input_exception import InvalidInputException


class TestImageBw(unittest.TestCase):
    """Defines unit tests for image_bw.py module"""
    def test_image_bw_valid_data(self):
        """Test the happy path"""
        image_bw = ImageBW(r'E:\Users\Leo\AT\Programming\AT19_CONVERTER\AT19_CONVERTER\AT19_CONVERTER_UT\AT19_CONVERTER\CONVERTER\test\com\resources\Image.png', '../../../resources/Image.jpg').convert()
        expected = r"magick E:\Users\Leo\AT\Programming\AT19_CONVERTER\AT19_CONVERTER\AT19_CONVERTER_UT\AT19_CONVERTER\CONVERTER\test\com\resources\Image.png -monochrome ../../../resources/Image.jpg"
        self.assertEqual(expected, image_bw)

    def test_image_bw_invalid_extension_correct_mime_type_input(self):
        """Test when an input file has a wrong extension but its mimetype is correct"""
        image_bw = ImageBW(r"E:\Users\Leo\AT\Programming\AT19_CONVERTER\AT19_CONVERTER\AT19_CONVERTER_UT\AT19_CONVERTER\CONVERTER\test\com\resources\type_image_wrong_extension.txt", "../../../resources/type_image_wrong_extension.jpg").convert()
        expected = r"magick E:\Users\Leo\AT\Programming\AT19_CONVERTER\AT19_CONVERTER\AT19_CONVERTER_UT\AT19_CONVERTER\CONVERTER\test\com\resources\type_image_wrong_extension.txt -monochrome ../../../resources/type_image_wrong_extension.jpg"
        self.assertEqual(expected, image_bw)

    def test_image_bw_null_input(self):
        """Test when input is null"""
        image_bw = ImageBW("", r"..\..\..\resources\Image.jpg")
        with self.assertRaises(InvalidInputException):
            image_bw.convert()

    def test_image_bw_null_output(self):
        """Test when output is null"""
        image_bw = ImageBW(r"..\..\..\resources\Image.jpg", "")
        with self.assertRaises(InvalidInputException):
            image_bw.convert()

    def test_image_bw_None_input(self):
        """Test when input is None"""
        image_bw = ImageBW(None, r"..\..\..\resources\Image.jpg")
        with self.assertRaises(InvalidInputException):
            image_bw.convert()

    def test_image_bw_None_output(self):
        """Test when output is None"""
        image_bw = ImageBW(r"..\..\..\resources\Image.jpg", None)
        with self.assertRaises(InvalidInputException):
            image_bw.convert()

    def test_image_bw_no_str_input(self):
        """Test when input is not a str"""
        image_bw = ImageBW(222, r"..\..\..\resources\Image.jpg")
        with self.assertRaises(InvalidInputException):
            image_bw.convert()

    def test_image_bw_no_str_output(self):
        """Test when output is not str"""
        image_bw = ImageBW(r"..\..\..\resources\Image.jpg", 2222)
        with self.assertRaises(InvalidInputException):
            image_bw.convert()

    def test_image_bw_invalid_extension_output(self):
        """Test when output is an invalid extension"""
        image_bw = ImageBW(r"..\..\..\resources\Image.jpg", r"..\..\..\resources\Image.mp3")
        with self.assertRaises(InvalidInputException):
            image_bw.convert()

    def test_image_bw_invalid_invalid_output_path(self):
        """Test when output path does not exist"""
        image_to_pdf = ImageBW(r'..\..\..\resources\Image.jpg', r'..\..\..\resour\Image.jpg')
        with self.assertRaises(InvalidInputException):
            image_to_pdf.convert()

    def test_image_bw_invalid_invalid_input_path(self):
        """Test when input path does not exist"""
        image_to_pdf = ImageBW(r'..\..\..\resourrrcceess\Image.jpg', r'..\..\..\resources\Image.jpg')
        with self.assertRaises(InvalidInputException):
            image_to_pdf.convert()
