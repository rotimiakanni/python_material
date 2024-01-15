from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# from sqlalchemy import text

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:test@localhost:5432/bookapp"


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# db = SessionLocal()
# print("Connection successful!")
# print(db.execute(text("SELECT 1")))
# db.close()
