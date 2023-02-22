#
# @test_image_to_text.py Copyright (c) 2023 Jalasoft.
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
from CONVERTER.src.com.jalasoft.converter.model.image.image_to_text import ImageToTextConvert
from CONVERTER.src.com.jalasoft.converter.common.exception.input_exception import InvalidInputException


class TestImageToPdf(unittest.TestCase):
    """Defines unit tests for image_to_text.py module"""
    def test_image_to_pdf_valid_data(self):
        """Test the happy path"""
        image_to_pdf = ImageToTextConvert(r'E:\Users\Leo\AT\Programming\AT19_CONVERTER\AT19_CONVERTER\AT19_CONVERTER_UT\AT19_CONVERTER\CONVERTER\test\com\resources\Image_imaTotex.jpg', r'../../../resources/Image_imaTotex', 'eng', 'txt')
        expected = r'tesseract E:\Users\Leo\AT\Programming\AT19_CONVERTER\AT19_CONVERTER\AT19_CONVERTER_UT\AT19_CONVERTER\CONVERTER\test\com\resources\Image_imaTotex.jpg ../../../resources/Image_imaTotex -l eng txt'
        self.assertEqual(expected, image_to_pdf.convert())

    def test_image_to_pdf_none_input(self):
        """Test when input is None"""
        image_to_pdf = ImageToTextConvert(None, r'..\..\..\resources\Image_imaTotex',
                                         'eng', 'pdf')
        with self.assertRaises(InvalidInputException):
            image_to_pdf.convert()

    def test_image_to_pdf_null_input(self):
        """Test when input is null"""
        image_to_pdf = ImageToTextConvert('', r'..\..\..\resources\Image_imaTotex',
                                         'eng', 'pdf')
        with self.assertRaises(InvalidInputException):
            image_to_pdf.convert()

    def test_image_to_pdf_no_str_input(self):
        """Test when input is not a str"""
        image_to_pdf = ImageToTextConvert(222, r'..\..\..\resources\Image_imaTotex',
                                         'eng', 'pdf')
        with self.assertRaises(InvalidInputException):
            image_to_pdf.convert()

    def test_image_to_pdf_invalid_extension_input(self):
        """Test when input is an invalid extension"""
        image_to_pdf = ImageToTextConvert(r'..\..\..\resources\Image_imaTotex.mp3', r'..\..\..\resources\Image_imaTotex',
                                         'eng', 'pdf')
        with self.assertRaises(InvalidInputException):
            image_to_pdf.convert()

    def test_image_to_pdf_none_output_extension(self):
        """Test when output extension is none"""
        image_to_pdf = ImageToTextConvert(r'..\..\..\resources\Image_imaTotex.jpg', r'..\..\..\resources\Image_imaTotex',
                                         'eng', None)
        with self.assertRaises(InvalidInputException):
            image_to_pdf.convert()

    def test_image_to_pdf_null_output_extension(self):
        """Test when output extension is null"""
        image_to_pdf = ImageToTextConvert(r'..\..\..\resources\Image_imaTotex.jpg', r'..\..\..\resources\Image_imaTotex',
                                         'eng', '')
        with self.assertRaises(InvalidInputException):
            image_to_pdf.convert()

    def test_image_to_pdf_no_str_output_extension(self):
        """Test when output extension is not str"""
        image_to_pdf = ImageToTextConvert(r'..\..\..\resources\Image_imaTotex.jpg', r'..\..\..\resources\Image_imaTotex',
                                         'eng', '')
        with self.assertRaises(InvalidInputException):
            image_to_pdf.convert()

    def test_image_to_pdf_invalid_output_extension(self):
        """Test when output extension is invalid"""
        image_to_pdf = ImageToTextConvert(r'..\..\..\resources\Image_imaTotex.jpg', r'..\..\..\resources\Image_imaTotex',
                                         'eng', 'gif')
        with self.assertRaises(InvalidInputException):
            image_to_pdf.convert()

    def test_image_to_pdf_none_lang_parameter(self):
        """Test when language is none"""
        image_to_pdf = ImageToTextConvert(r'..\..\..\resources\Image_imaTotex.jpg', r'..\..\..\resources\Image_imaTotex',
                                          None, 'pdf')
        with self.assertRaises(InvalidInputException):
            image_to_pdf.convert()

    def test_image_to_pdf_null_lang_parameter(self):
        """Test when language is null"""
        image_to_pdf = ImageToTextConvert(r'..\..\..\resources\Image_imaTotex.jpg', r'..\..\..\resources\Image_imaTotex',
                                         '', 'pdf')
        with self.assertRaises(InvalidInputException):
            image_to_pdf.convert()

    def test_image_to_pdf_no_str_lang_parameter(self):
        """Test when language is not str"""
        image_to_pdf = ImageToTextConvert(r'..\..\..\resources\Image_imaTotex.jpg', r'..\..\..\resources\Image_imaTotex',
                                          True, 'pdf')
        with self.assertRaises(InvalidInputException):
            image_to_pdf.convert()

    def test_image_to_pdf_invalid_lang_parameter(self):
        """Test when language is invalid"""
        image_to_pdf = ImageToTextConvert(r'..\..\..\resources\Image_imaTotex.jpg', r'..\..\..\resources\Image_imaTotex',
                                         'rus', 'pdf')
        with self.assertRaises(InvalidInputException):
            image_to_pdf.convert()

    def test_image_to_pdf_none_output(self):
        """Test when output is None"""
        image_to_pdf = ImageToTextConvert(r'..\..\..\resources\Image_imaTotex.jpg', None,
                                         'eng', 'pdf')
        with self.assertRaises(InvalidInputException):
            image_to_pdf.convert()

    def test_image_to_pdf_null_output(self):
        """Test when output is null"""
        image_to_pdf = ImageToTextConvert(r'..\..\..\resources\Image_imaTotex.jpg', '',
                                         'eng', 'pdf')
        with self.assertRaises(InvalidInputException):
            image_to_pdf.convert()

    def test_image_to_pdf_invalid_output_path(self):
        """Test whe the output path is not valid"""
        image_to_pdf = ImageToTextConvert(r'..\..\..\resources\Image_imaTotex.jpg', r'..\..\..\resour\imagess',
                                         'eng', 'pdf')
        with self.assertRaises(InvalidInputException):
            image_to_pdf.convert()

    def test_image_to_pdf_invalid_input_path(self):
        """Test whe the input path is not valid"""
        image_to_pdf = ImageToTextConvert(r'..\..\..\resourrrcceess\Image_imaTotex.jpg', r'..\..\..\resources\Image_imaTotex',
                                         'eng', 'pdf')
        with self.assertRaises(InvalidInputException):
            image_to_pdf.convert()
