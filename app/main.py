from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def ready():
    return {"ready": "true"}
