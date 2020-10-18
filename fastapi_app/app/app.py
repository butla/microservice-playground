from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return {"Hello": "World"}


@app.get("/{path_param}")
def with_params(path_param: int, query_param: str):
    return {
        "path": path_param,
        "query_param": query_param,
    }
