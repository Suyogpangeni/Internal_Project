from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
import os
from urllib.parse import quote_plus
from contextlib import contextmanager
load_dotenv()

host = os.getenv("DB_HOST")
port = int(os.getenv("DB_PORT", 3306))
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD", "")
password = quote_plus(os.getenv("db_password"))

database_url= f"mysql+mysqldb://{db_user}:{password}@{host}:{port}/{db_name}"
    
engine= create_engine(
    database_url,
    echo=True,
    pool_pre_ping=True,
    pool_recycle=1800,
)
SessionLocal= sessionmaker(bind= engine,autocommit=False,autoflush=True)


Base= declarative_base()

@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db                 
    except Exception as e:
        db.rollback()      
        print(f"Session rollback due to: {e}")
        raise
    finally:
        db.close()          
