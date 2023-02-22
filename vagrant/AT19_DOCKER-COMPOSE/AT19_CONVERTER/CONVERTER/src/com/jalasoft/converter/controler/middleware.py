#
# @middleware.py Copyright (c) 2023 Jalasoft.
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
from flask import jsonify
from common.token import Token

class Middleware:
    @staticmethod
    def before_request():
        """Verifies users before process request"""
        if request.path != '/login':
            if request.method == 'POST':
                try:
                    autentification = request.headers.get("Authorization")
                    token = autentification.split(" ")[1]
                    valid = Token().validate_token(token)
                    if valid == False:
                        response = jsonify({"message": "You aren't authorized"})
                        response.status_code = 401
                        return response
                except:
                    response = jsonify({"message": "Bad request"})
                    response.status_code = 400
                    return response
