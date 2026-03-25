from auth.model.Users import Users
from database.connection import Base, engine


def create_table():
    Base.metadata.create_all(bind=engine)