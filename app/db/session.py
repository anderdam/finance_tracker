from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session as SessionType
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engine = create_engine(settings.database_url, future=True, echo=False)
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False, future=True)


def get_db() -> Generator[SessionType, None, None]:
    db = Session()
    try:
        yield db
    finally:
        db.close()
