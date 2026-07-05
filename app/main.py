from fastapi import FastAPI
app=FastAPI()

@app.get("/")
def printtest():
    return {"message":"Hello engineer",
            "running":True}