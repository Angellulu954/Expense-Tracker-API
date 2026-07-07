from pydantic import BaseModel,Field
from enums import Category
class Expense(BaseModel):
    title:str
    amount:float=Field(...,gt=0)
    category:Category
    
