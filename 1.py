from fastapi import FastAPI
import pydantic

app = FastAPI()


class Numbers(pydantic.BaseModel):
    a: int
    b: int


class TaskArgs(pydantic.BaseModel):
    name: str
    args: Numbers


@app.put("/task/3/")
async def handler(obj: TaskArgs):
    a = obj.args.a
    b = obj.args.b
    return {
        "result": a / b,
        "task": obj.name,
    }


@app.get("/hello")
async def handler():
    return {
        "hello": "world",
    }
