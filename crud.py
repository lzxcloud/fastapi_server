from sqlalchemy.orm import session
from . import model, schemas


def get_user(db: session, user_id: int):
    return db.query(model.User).filter(model.User.uuid == user_id).first()


def create_user(db: session,user: schemas.user):
    new_user = model.User(uuid=user.uuid, platform=user.platform)
    db.add(new_user)
    db.commit()
    db.refresh()
    return new_user
