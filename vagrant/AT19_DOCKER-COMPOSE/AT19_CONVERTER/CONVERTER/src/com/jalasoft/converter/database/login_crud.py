#
# @login_crud.py Copyright (c) 2023 Jalasoft.
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

from os import getenv
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
db_user = getenv("DB_USER")
db_password = getenv("DB_PASSWORD")
db_host = getenv("DB_HOST")
db_port = getenv("DB_PORT")
db_name = getenv("DB_NAME")
class User(Base):
    """Defines user table"""
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(20), unique=True, nullable=False)
    password = Column(String(80), nullable=False)


engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
class UserCRUD():
    """Process CRUD"""
    def create(self):
        user_name = "converter_user"
        password = "1234"
        existing_user = session.query(User).filter_by(user_name = user_name).first()
        if not existing_user:
            user = User(user_name = user_name, password = password)
            session.add(user)
            session.commit()

    def read(self, username):
        """Reads from data base"""
        user = session.query(User).filter_by(user_name = username).first()
        return user
