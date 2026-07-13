from pydantic import BaseModel,Field
from app.enums import Category
from datetime import datetime
from pydantic import ConfigDict
class ExpenseCreate(BaseModel):
    title:str
    amount:float=Field(...,gt=0)
    category:Category
class ExpenseResponse(BaseModel):
    id: int
    title:str
    amount:float
    category:Category
    created_on: datetime
    model_config=ConfigDict(from_attributes=True)
