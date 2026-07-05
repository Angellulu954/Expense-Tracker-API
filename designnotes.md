The purpose of this project is to build a backend API that sits between the frontend and the database. The frontend communicates with the API, and the API is responsible for validating requests, interacting with the database, and returning responses.

the users of this are people who want to manage their expenses 





the API should be able to :

Create a new expense.
Retrieve all expenses.
Retrieve a specific expense by its ID.
Delete an expense.
Filter expenses by category.


database to be used : POSTGREsql because its widely used 

use fastapi because its modern 


API DESIGN :

for creating a new expense:
it receives the title , the amount, the category 

possible errors:
missing title, missing amount and category 

invalid amount 


for retrieving an expense:
it receives the item its suppossed to retrieve

possible errors:
information given doesnt exit 


for deleting an expense:
it receives the item its suppossed to delete 

possible errors :
None

for filtering:
it receives the category

returns :
the items in the category given 


TECH STACK:
Python
FastAPI
PostgreSQL
SQLAlchemy
Alembic
Pydantic-describes what valid data looks like


request flow:
Client sends a request → FastAPI receives it → validates the data → stores it in PostgreSQL → returns a response then the client receives a response or an action is taken such as the deleted expense is no longer visible 


error handling:
write code that stops the errors from occuring eg for invalid amount ensure only positive values are given excluding 0 





