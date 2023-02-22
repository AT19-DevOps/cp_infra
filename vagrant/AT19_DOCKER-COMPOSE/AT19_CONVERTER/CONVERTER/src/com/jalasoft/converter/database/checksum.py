#
# @checksum.py Copyright (c) 2023 Jalasoft.
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

import hashlib
from database.db_commands import CRUD


def checksum_generator_md5(in_file):
    with open(in_file, 'rb') as opened_file:
        content = opened_file.read()
        md5 = hashlib.md5()
        md5.update(content)
        check = md5.hexdigest()
        print("checksum", check)
    return check


def compare_checksum(filename, in_file):
    try:
        check_md5 = checksum_generator_md5(in_file)
        column_check = CRUD.read_specific_data("SELECT checksum FROM media")
        if not any(val == check_md5 for val in column_check):
            CRUD.insert_data(filename, check_md5, in_file)
        path_upload = CRUD.read_specific_data(f"SELECT route FROM media WHERE checksum = '{check_md5}' ")
        return path_upload[0]
    except Exception as error:
        raise Exception("checksum failed")




