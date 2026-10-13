from sqlalchemy import create_engine
from sqlalchemy.ext.declotative import declorative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

engine = create_engine(
    settings.database_url,
    connect_args = {"check_same_thread" : False}
)

Session_Local = sessionmaker(autocommit = False, autoflush = False, bind = engine)
Base = declorative_base()


def get_db():
    db = Session_Local()
    try:
        yield db
    finally:
        db.close




def init_db():
    Base.metadata.create_all(bind=engine)
