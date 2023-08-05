from typing import Optional
from pydantic import BaseModel # pylint: disable=no-name-in-module
from datetime import datetime

class Access_Data(BaseModel):
    user_id:str
    channel_id:str
    access_time:datetime

    class Config:
        orm_mode = True