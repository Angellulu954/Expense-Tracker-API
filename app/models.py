from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column,DateTime,Float,String,Integer,Enum as SQLEnum,func
from enums import Category
class Base(DeclarativeBase):
    pass
class Expense(Base):
    __tablename__="expenses"
    id=Column(Integer,primary_key=True,autoincrement=True)
    title=Column(String)
    amount=Column(Float)
    category=Column(SQLEnum(Category))
    created_on=Column(DateTime,
                      server_default=func.now()
                      )
    