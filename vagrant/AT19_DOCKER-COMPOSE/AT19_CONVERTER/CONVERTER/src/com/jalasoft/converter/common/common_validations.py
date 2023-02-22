#
# @common_validations.py Copyright (c) 2023 Jalasoft.
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


class CommonValidator:
    """Defines validations for all endpoints"""
    def __init__(self, parameter, method):
        self.parameter = parameter
        self.method = method

    def common_validate(self):
        """Defines if the parameter is none, empty or no str"""
        if self.parameter is None:
            raise InvalidInputException("Invalid parameter: the parameter should not be None type - " + self.method)
        if not self.parameter:
            raise InvalidInputException("Invalid parameter: the parameter is empty -" + self.method)
        if type(self.parameter) != str:
            raise InvalidInputException(f"Invalid parameter: the parameter {self.parameter} type is not valid -"
                                        + self.method)

    def int_validate(self):
        """Defines if the parameter is none, empty or no int"""
        if self.parameter is None:
            raise InvalidInputException("Invalid parameter: the parameter should not be None type - " + self.method)
        if not self.parameter:
            raise InvalidInputException("Invalid parameter: the parameter is empty -" + self.method)
        if type(self.parameter) != int:
            raise InvalidInputException(f"Invalid parameter: the parameter {self.parameter} type is not valid -"
                                        + self.method)
