from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class Access_Table(Base):
    __tablename__ = 'access_table'

    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    channel_id = Column(String)
    access_time = Column(DateTime)
    access_id = Column(String)
    


class Task_Table(Base): 
    __table__name__ = 'task_table'
    
    id = Column(Integer, primary_key=True)
    access_id = Column(String)
    time = Column(DateTime)
    bot_message = Column(String)
    user_message = Column(String)
    task_status = Column(String)