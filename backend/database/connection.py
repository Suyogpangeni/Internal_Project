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
password = quote_plus(os.getenv("DB_PASSWORD"))

database_url= f"mysql+mysqldb://{db_user}:{password}@{host}:{port}/{db_name}"
if not database_url:
    print(f"Database {db_name} is not connected")
    
engine= create_engine(database_url,echo=True)
SessionLocal= sessionmaker(bind= engine,autocommit=False,autoflush=True)


Base= declarative_base()

@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db           
        db.commit()        
    except Exception as e:
        db.rollback()      
        print(f"Session rollback due to: {e}")
        raise
    finally:
        db.close()          