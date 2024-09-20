from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from infrastructure.postgres.migrations.migrator import DATABASE_URL

engine = create_engine(DATABASE_URL)

SessionMaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)
