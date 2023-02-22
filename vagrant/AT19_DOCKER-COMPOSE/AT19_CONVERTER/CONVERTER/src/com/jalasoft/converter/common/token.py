#
# @token.py Copyright (c) 2023 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from jwt import encode
from jwt import decode
from jwt import exceptions
from flask import jsonify
from os import getenv
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from database.login_crud import UserCRUD


class Token:
    """Process the token"""

    def __init__(self):
        self.time = 1

    def expire_date(self):
        """Defines the expiration date of the token"""
        now = datetime.now(tz=timezone.utc)
        new_date = now + timedelta(days=self.time)
        return new_date

    def write_token(self, data: dict):
        """Writes the token"""
        token = encode(payload={**data, "exp": self.expire_date()},
                   key=getenv("SECRET"), algorithm="HS256")
        return token.encode("UTF-8")

    def validate_token(self, token):
        """Defines validation of the token"""
        try:
            data = decode(token, key = getenv("SECRET"),algorithms = ["HS256"])
            db_user = UserCRUD().read(data["user_name"])
            if db_user != None:
                return True
            else:
                return False
        except exceptions.DecodeError:
            response = jsonify({"message": "Invalid Token"})
            response.status_code = 401
            return False
        except (exceptions.ExpiredSignatureError) as e:
            response = jsonify({"message": "Token Expired"})
            response.status_code = 401
            return False
