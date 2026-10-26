import os
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Base(DeclarativeBase):
    pass


engine = create_engine(os.getenv("DATABASE_URL", "sqlite:///./exercise.db"))
SessionFactory = sessionmaker(bind=engine, expire_on_commit=False)
