from datetime import datetime
import hashlib
import secrets  # 무작위 솔트 생성을 위해 secrets 모듈을 가져옵니다.
from fastapi import Depends, FastAPI
import logging
from sqlalchemy.orm import Session

from database import db
from crud import write_access_data
from schema import Access_Data

app = FastAPI()


@app.get("/")
async def root():
    """ 루트 API """
    logging.info("hello")
    return {"message": "hello"}

@app.post("/access")
async def access(user_id: str, channel_id: str, access_time: datetime, access_db: Session = Depends(db.get_session)):
    """액세스 API"""
    logging.info("액세스 API")
    
    salt = secrets.token_hex(16) 

    access_id_raw = user_id + channel_id + str(access_time) + salt
    access_id = hashlib.sha256(access_id_raw.encode('utf-8')).hexdigest()
    print("hi2")
    return write_access_data(access_id, access_db)
