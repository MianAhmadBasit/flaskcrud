from fastapi import FastAPI

app = FastAPI()

@app.get("/hi")
async def root():
    return {"message": "hi ahmad"}

@app.get("/hello/{name}")
async def root(name):
    return {"message": f"hi ahmad hello page {name}"}