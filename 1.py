from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def handler():
    return {
        "hello": "world"
    }
