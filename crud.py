from sqlalchemy.orm import session
import model
from schemas import ItemCreate
from sqlalchemy import func

def get_user(db: session, user_id: int):
    return db.query(model.User).filter(model.User.uuid == user_id, model.User.is_active == True).first()


def create_user(db: session, uuid: str):
    new_user = model.User(uuid=uuid)
    db.add(new_user)
    db.commit()
    return new_user


def create_info(db: session, user_id: int,  info: ItemCreate):
    new_info = model.Info(
        title=info.title,
        cost=info.cost,
        platform=info.platform,
        user_id=user_id,
        end=info.end
    )
    db.add(new_info)
    db.commit()
    return new_info


def get_user_infos(db: session, user_id, end_date: str):
    infos = db.query(model.Info).filter(
        model.Info.user_id == user_id,
        model.Info.end >= end_date
    ).all()
    return infos

def get_cost(db: session, user_id: str, end_date: str):
    cost = db.query(func.sum(model.Info.cost)).filter(
        model.Info.user_id == user_id,
        model.Info.end >= end_date
    ).scalar()
    return cost if cost else 0
