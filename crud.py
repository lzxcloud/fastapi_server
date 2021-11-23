from sqlalchemy.orm import session
import model
import schemas


def get_user(db: session, user_id: int):
    return db.query(model.User).filter(model.User.uuid == user_id, model.User.is_active == True).first()


def create_user(db: session, uuid: str):
    new_user = model.User(uuid=uuid)
    db.add(new_user)
    db.commit()
    return new_user
