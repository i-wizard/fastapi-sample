from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

from settings import settings

engine = create_engine(settings.DB_URL, 
                       echo=True
)

BaseClass = declarative_base()

SessionLocal = sessionmaker(bind=engine)