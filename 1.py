from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def handler():
    return {
        "hello": "world"
    }
@app.get("/hello")
async def handler():
    return {';)'}

