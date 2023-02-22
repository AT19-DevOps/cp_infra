#
# @add_user.py Copyright (c) 2023 Jalasoft.
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


from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(20), unique=True, nullable=False)
    password = Column(String(80), nullable=False)

engine = create_engine('mysql+pymysql://root@localhost/converter_db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def add_user(username, password):
    existing_user = session.query(User).filter_by(user_name=username).first()
    if not existing_user:
        user = User(user_name=username, password=password)
        session.add(user)
        session.commit()

add_user("converter_user", "1234")