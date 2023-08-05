"""SQLAlchemy ORM models Metadata read test. """

import os
import sys
from sqlalchemy import MetaData, create_engine, Table, Column, Integer, String, DateTime
from config import conf

SQL_URL = f'mysql+pymysql://root:{conf["dbpassword"]}@localhost:3306/bot?charset=utf8mb4'

# Table definition
def metadata_check():
    db_engine = create_engine(SQL_URL, echo=True)
    metadata = MetaData()
    table = Table('access_table', metadata, autoload_with=db_engine)
    # table = Table('access_table', metadata, autoload=True, autoload_with=db_engine)
    print(table.columns)
    print(table.columns.keys())

metadata_check()


# Class definition
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Access_Table(Base):
    __tablename__ = 'access_table'

    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    channel_id = Column(String)
    access_time = Column(DateTime)
    access_id = Column(String)