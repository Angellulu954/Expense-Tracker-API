from pydantic import BaseModel,Field
from enum import Enum
class Category(Enum):
    FOOD="Food"
    TRANSPORT="Transport"
    RENT="Rent"
    ENTERTAINMENT="Entertainment"
    HEALTHCARE="Healthcare"
    SHOPPING="Shopping"
    OTHER="Other"
class Expense(BaseModel):
    title:str
    amount:float=Field(...,gt=0)
    category:Category
    
