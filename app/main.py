from fastapi import FastAPI,Depends,HTTPException
from app.schemas import ExpenseCreate,ExpenseResponse
from app.database import ENGINE,get_db
from app.models import Base
from app.models import Expense 
from sqlalchemy.orm import Session 
from sqlalchemy import Select
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

@app.get("/expenses", response_model=list[ExpenseResponse])
async def get_expenses(db:Session=Depends(get_db)):
    stmt=Select(Expense)
    expenses=db.scalars(stmt).all()
    
    return expenses

@app.get("/expenses/{expense_id}",response_model=ExpenseResponse)
async def get_expense_by_id( expense_id:int, db:Session=Depends(get_db)):
    value=db.get(Expense,expense_id)
    if value is None:
        raise HTTPException(status_code=404,detail="Expense not Found")
    return value
@app.put("/expense/{expense_id},response_model=ExpenseResponse")
async def update_expense(expense_id:int,expense:ExpenseCreate,db:Session=Depends(get_db)):
    found=db.get(Expense,expense_id)
    if found==None:
        raise HTTPException(status_code=404,detail="Expense with that Id doesnt not exist")
    
    found.title=expense.title
    found.amount=expense.amount
    found.category=expense.category
    
    
    db.commit()
    db.refresh(found)
    return found
