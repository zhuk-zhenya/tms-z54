from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
async def handler():
    return {
        "hello": "world"
    }
