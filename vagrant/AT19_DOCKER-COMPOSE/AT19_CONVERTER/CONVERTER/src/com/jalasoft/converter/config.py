#
# config.py Copyright (c) 2023 Jalasoft.
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

import os
from flask_swagger_ui import get_swaggerui_blueprint

PATH = os.path.realpath(os.path.dirname(__file__))
PATH = os.path.join(PATH, 'workdir')
UPLOAD_FOLDER = os.path.join(PATH, 'uploads')
RESPONSE_FOLDER = os.path.join(PATH, 'responses')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESPONSE_FOLDER, exist_ok=True)

"""Server configuration"""
SERVER = '192.168.33.60'
PORT = '5000'
DOWNLOAD_DIR = 'http://' + SERVER + ':' + PORT + '/download?file_name='

SWAGGER_URL = '/openapi'
API_URL = '/static/openapi.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Converter"
    }
)
