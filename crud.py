from sqlalchemy.orm import session
import model
from schemas import ItemCreate


def get_user(db: session, user_id: int):
    return db.query(model.User).filter(model.User.uuid == user_id, model.User.is_active == True).first()


def create_user(db: session, uuid: str):
    new_user = model.User(uuid=uuid)
    db.add(new_user)
    db.commit()
    return new_user


def create_info(db: session, info: ItemCreate):
    new_info = model.Info(
        title=info.title,
        cost=info.cost,
        platform=info.platform
    )
    db.add(new_info)
    db.commit()
    return new_info
