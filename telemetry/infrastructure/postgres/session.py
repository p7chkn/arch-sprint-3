from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from config import config


engine = create_engine(config.postgres_dsn)

SessionMaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_session() -> Session:
    db = SessionMaker()
    return db