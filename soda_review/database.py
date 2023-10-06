from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

_DATABASE_LOCATION = "sqlite:///./database/sodareview.db"

engine = create_engine(_DATABASE_LOCATION, connect_args={"check_same_thread" : False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

