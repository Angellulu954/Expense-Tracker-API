from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from sqlalchemy import Enum as SQLEnum,func
from app.enums import Category
from datetime import datetime
class Base(DeclarativeBase):
    pass
class Expense(Base):
    __tablename__="expenses"
    id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    title:Mapped[str]
    amount:Mapped[float]
    category:Mapped[Category]=mapped_column(SQLEnum(Category))
    created_on:Mapped[datetime]=mapped_column(server_default=func.now())
    
    