from sqlalchemy import Column, Integer, String, Boolean
from database.connection import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(70), nullable=False)
    useremail = Column(String(100), nullable=False, unique=True)
    password = Column(String(200), nullable=False)
    role = Column(String(50), nullable=False)
    firstlogin = Column(Boolean, default=False)
    isdeleted = Column(Boolean, default=False)