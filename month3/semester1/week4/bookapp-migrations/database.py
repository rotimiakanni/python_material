from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# from sqlalchemy import text

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:test@localhost:5432/test"


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# db = SessionLocal()
# print("Connection successful!")
# print(db.execute(text("SELECT 1")))
# db.close()
