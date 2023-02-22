#
# @ep_login.py Copyright (c) 2023 Jalasoft.
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

from flask import request
from flask_restful import Resource
from database.validate_user import ValidateUser


class Login(Resource):
    """Defines user login"""
    def post(self):
        """Verify user"""
        user_name = request.form["username"]
        password = request.form["password"]
        response = ValidateUser(user_name, password).compare()
        return response
