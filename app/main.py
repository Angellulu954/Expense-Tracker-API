from fastapi import FastAPI
from app.schemas import Expense as ExpenseSchema
from app.database import ENGINE,SessionLocal
from app.models import Base
from app.models import Expense as ExpenseModel

app=FastAPI()

Base.metadata.create_all(bind=ENGINE)

@app.get("/")

def home():
    return {"message":"Hello engineer",
            "running":True}
@app.post("/expenses")

async def CreateExpense(expense:ExpenseSchema):
    db=None
    try:
        db=SessionLocal()
        db_expense=ExpenseModel(
        title=expense.title,
        category=expense.category,
        amount=expense.amount
        
    )
        db.add(db_expense)
        db.commit()
    finally:
        if db is not None:

            db.close()
        
    return expense

