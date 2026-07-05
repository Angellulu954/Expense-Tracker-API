from fastapi import FastAPI
from app.schemas import Expense
app=FastAPI()

@app.get("/")

def home():
    return {"message":"Hello engineer",
            "running":True}
@app.post("/expenses")
async def CreateExpense(expense:Expense):
        
    return expense
