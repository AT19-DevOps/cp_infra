#
# @logger_.py Copyright (c) 2023 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from CONVERTER.src.com.jalasoft.converter.common.logger.Singleton import SingletonMeta
import logging
import logging.config


class LoggerManager(metaclass=SingletonMeta):
    """Wrappes Logger Method"""
    logging.config.fileConfig('logging.conf')

    def debug(self, message):
        """Writes logger debug level"""
        logging.debug(message)
    
    def info(self, message):
        """Writes logger info level"""
        logging.info(message)

    def warning(self, message):
        """Writes logger warning level"""
        logging.warning(message)

    def error(self, message):
        """Writes logger error level"""
        logging.error(message)

    def critical(self, message):
        """Writes logger critical level"""
        logging.critical(message)

    def enter_method(methodName):
        """Writes logger to enter a method"""
        logging.debug('Enter Method >' + str(methodName))

    def exit_method(methodName):
        """Writes logger to exit a method"""
        logging.debug('Exit Method >' + str(methodName))
