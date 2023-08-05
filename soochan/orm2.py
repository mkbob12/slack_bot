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

    # data_add
    ins = table.insert().values(user_id='test', channel_id='test', access_time='2021-01-01 00:00:00', access_id='test')
    db_conn = db_engine.connect()
    db_conn.execute(ins)
    # data_select
    s = table.select()
    result = db_conn.execute(s)
    for row in result:
        print(row)
    db_conn.close()

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

# ORM test
def orm_test():
    db_engine = create_engine(SQL_URL, echo=True)
    db_conn = db_engine.connect()
    new_access = Access_Table(user_id='test', channel_id='test', access_time='2021-01-01 00:00:00', access_id='test')
    db_conn.add(new_access)
    db_conn.commit()
    db_conn.close()
    # data_select
    db_conn = db_engine.connect()
    s = db_conn.query(Access_Table.access_id == 'test').all()
    for row in s:
        print(row)
    
orm_test()