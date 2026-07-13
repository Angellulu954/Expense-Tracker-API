from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
DATABASE_URL="postgresql+psycopg://postgres:postgres@localhost:5432/expense_tracker"
ENGINE=create_engine(DATABASE_URL)
SessionLocal=sessionmaker(bind=ENGINE)


def get_db():
    db=SessionLocal()
    try:
        yield db
        
    finally:
        db.close()