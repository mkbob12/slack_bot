from sqlalchemy.orm import Session

import models

def write_access_data(access_id: str, db: Session):
    
    query_result = db.query(models.Access_Table).filter(models.Access_Table.access_id == access_id).first()
    if query_result is None:
  
        access_data = models.Access_Table(access_id=access_id,user_id="hi",channel_id="hello",access_time="2023-04-10T02:33:23")
        db.add(access_data)
        db.commit()
        return {"message": "{access_data} 출력", 'result': True}
    else:
        # 이미 해당 액세스 ID가 데이터베이스에 존재하는 경우
        return {"message": "이미 액세스 ID가 존재합니다", 'result': False}
