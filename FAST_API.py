from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello API"}


@app.get("/hello/{Gio}")
def say_hello(Gio: str):
    return {"message": f"Hello, {Gio}!"}
