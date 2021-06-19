import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DEFAULT_DB = "sqlite:///./sql_app.db"
ACTUAL_DB = os.environ.get("DATABASE_URL", DEFAULT_DB).replace(
    "postgres://", "postgresql://"
)

if ACTUAL_DB.startswith("sqlite"):
    engine = create_engine(ACTUAL_DB, connect_args={"check_same_thread": False})
else:
    engine = create_engine(ACTUAL_DB)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
