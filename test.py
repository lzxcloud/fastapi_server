
from database import SessionLocal
from model import User

res = SessionLocal().query(User.uuid).all()
print(res)