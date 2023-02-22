#
# @text_translate.py Copyright (c) 2023 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

import googletrans
from googletrans import Translator
from model.converter import Converter


class TextTranslator(Converter):
    """Inherits Converter criteria"""

    def __init__(self, input_file: str, output_file: str):
        super().__init__(input_file, output_file)

    def convert(self) -> dict:
        """Translates text into a language given"""
        languages: dict = googletrans.LANGUAGES
        translator = Translator()
        translated: TextTranslator = translator.translate(self.input_file, dest=self.output_file)
        translation: dict = {
            "Source language": languages[str(translated.src)].capitalize(),
            "Translation": str(translated.text),
            "Pronunciation": str(translated.extra_data['origin_pronunciation'])
        }
        return translation
