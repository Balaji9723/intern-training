import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, declarative_base
DATABASE_URL = "postgresql://postgres:Thasmag97@localhost:5432/test1"

engine = sa.create_engine(DATABASE_URL) # connnect the database
session_local = sessionmaker(bind = engine) #create the session 
Base = declarative_base() # for metadata

def get_db():
    db = session_local()
    try: 
        yield db

    finally:
        db.close()
    

