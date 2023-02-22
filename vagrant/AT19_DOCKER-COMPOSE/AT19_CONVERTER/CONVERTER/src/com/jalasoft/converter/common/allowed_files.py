#
# @allowed_files.py Copyright (c) 2023 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#
from common.exception.input_exception import InvalidInputException


class AllowedExtensions:
    """Defines Allowed extensions criteria"""

    def validate_extension(self, file_name):
        """Check if the input is empty"""
        if file_name is None:
            raise InvalidInputException("Invalid input: the input should not be None type")
        if not file_name:
            raise InvalidInputException("Invalid input: the input is empty")
        if type(file_name) != str:
            raise InvalidInputException("Invalid input: the input must be string ")
        return True
