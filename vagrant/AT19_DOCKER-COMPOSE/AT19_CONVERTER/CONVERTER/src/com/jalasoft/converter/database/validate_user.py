#
# @validate_user.py Copyright (c) 2023 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
#
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from common.token import Token
from flask import jsonify
from database.login_crud import UserCRUD


class ValidateUser:
    """Validates user"""
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def process_password(self, password_hash):
        """TO DO: Process password"""
        return password_hash

    def compare(self):
        """Compares password"""
        try:
            password_hash = self.process_password(self.password)
            user = UserCRUD().read(self.user_name)
            if user.password == password_hash:
                data = {"user_name": self.user_name}
                token = Token().write_token(data)
                token_filtered = str(token)[2:-1]
                response = jsonify({"token": token_filtered})
                response.status_code = 200
                return response
            else:
                response = jsonify({"message": "invalid user or password"})
                response.status_code = 404
                return response
        except:
            response = jsonify({"message": "invalid user or password"})
            response.status_code = 404
            return response
