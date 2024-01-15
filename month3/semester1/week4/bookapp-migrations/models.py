from sqlalchemy import Column, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Book(Base):
    __tablename__ = "books"

    id = Column(String, primary_key=True, index=True)
    title = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    isbn = Column(String, nullable=False)
    publisher = Column(String, nullable=False)
    author = Column(String, nullable=False)
