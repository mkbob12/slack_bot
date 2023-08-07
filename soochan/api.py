from datetime import datetime
import hashlib 
from fastapi import Depends, FastAPI
import logging
from sqlalchemy.orm import Session

from database import db
from crud import write_access_data
from schema import Access_Data
from config import salt

app = FastAPI()


@app.get("/")
async def root():
    """ Root API """
    logging.info("Hello World")
    return {"message": "Hello World"}

@app.post("/access")
async def access(access_item: Access_Data, access_db: Session = Depends(db.get_session)):
    """Access API"""
    logging.info("Access API")
    # make Access_Data
    access_id_raw = access_item.user_id + access_item.channel_id + str(access_item.access_time) + salt
    # hash each 5 times
    # for _ in range(5):
    access_id = hashlib.sha256(access_id_raw.encode('utf-8')).hexdigest()
    return write_access_data(access_id, access_item, access_db)