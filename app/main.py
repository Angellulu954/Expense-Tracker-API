from fastapi import FastAPI,Depends
from app.schemas import ExpenseCreate,ExpenseResponse
from app.database import ENGINE,SessionLocal,get_db
from app.models import Base
from app.models import Expense 
from sqlalchemy.orm import Session

app=FastAPI()

Base.metadata.create_all(bind=ENGINE)

@app.get("/")

def home():
    return {"message":"Hello engineer",
            "running":True}
@app.post("/expenses", response_model=ExpenseResponse)

async def CreateExpense(expense:ExpenseCreate, db:Session=Depends(get_db)):
    
    
    
    db_expense=Expense(
    title=expense.title,
    category=expense.category,
    amount=expense.amount
        
    )
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    
    
        
    return db_expense

