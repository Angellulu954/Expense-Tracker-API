from fastapi import FastAPI
from app.schemas import Expense
from database import ENGINE
from models import Base

app=FastAPI()
Base.metadata.create_all(bind=ENGINE)

@app.get("/")

def home():
    return {"message":"Hello engineer",
            "running":True}
@app.post("/expenses")
async def CreateExpense(expense:Expense):
        
    return expense
