from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {
        "message":"I am From Github Action."
    }
