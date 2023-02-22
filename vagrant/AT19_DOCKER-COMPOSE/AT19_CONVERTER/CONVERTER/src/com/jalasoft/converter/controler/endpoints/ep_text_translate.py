#
# @ep_text_translate.py Copyright (c) 2023 Jalasoft.
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

from common.exception.convert_exception import ConvertException
from model.text.text_translate import TextTranslator


class TextTranslate(Resource):
    """Translate a text class"""
    def post(self):
        """Translate text into a given language endpoint"""
        input_file = request.form["text"]
        output_file = request.form['language']
        try:
            translation = TextTranslator(input_file, output_file).convert()
            return {"translation": translation}
        except ConvertException as error:
            response = {'error_message': error.get_message()}
            return response, 400
