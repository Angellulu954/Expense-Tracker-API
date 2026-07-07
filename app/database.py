from sqlalchemy import create_engine
DATABASE_URL="postgresql+psycopg://postgres:Matoroki06#@localhost:5432/expense_tracker"
ENGINE=create_engine(DATABASE_URL)
