from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#for sqlite db connection
# sqlite_file_name = "database.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"
# connect_args = {"check_same_thread": False}
# engine = create_engine(sqlite_url, connect_args=connect_args)

#for postgresql db connection
db_url = "postgresql+psycopg2://postgres:2002@localhost:5432/postgres"
engine = create_engine(db_url)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def create_db_and_tables():
    print("Creating database and tables...")
    Base.metadata.create_all(bind=engine)

def get_session():
    db = Session()
    try:
        yield db
    finally:
        db.close()

