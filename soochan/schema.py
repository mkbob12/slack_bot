from typing import Optional
from pydantic import BaseModel # pylint: disable=no-name-in-module
from datetime import datetime

class Access_Data(BaseModel):
    user_id: Optional[str] = None
    channel_id: Optional[str] = None
    access_time: Optional[datetime] = None

    class Config:
        orm_mode = True

class Task_Data(BaseModel):
    access_id:str
    time : Optional[datetime] = None
    bot_message: Optional[str] = None
    user_message: Optional[str] = None
    task_status: Optional[str] = None
    
    class Config:
        orm_mode = True