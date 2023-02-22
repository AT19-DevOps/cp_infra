#
# @zip_file.py Copyright (c) 2023 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft
#

import shutil
import os


class ZipFiles:
    """Defines ZipFiles criteria"""
    def __init__(self, name_of_zip, folder_to_zip, destination):
        self.name_of_zip = name_of_zip
        self.folder_to_zip = folder_to_zip
        self.destination = destination
    
    def compress(self):
        """Defines compress method"""
        shutil.make_archive(self.name_of_zip, 'zip', self.folder_to_zip)
        name = self.name_of_zip + '.zip'
        shutil.move(name, os.path.join(self.destination, os.path.basename(name)))
        return name
