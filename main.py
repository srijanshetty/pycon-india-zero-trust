from fastapi import FastAPI
from lib.redis_core import Connection

app = FastAPI()
r = Connection()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/redis")
async def redis():
    return r.get('pycon')
