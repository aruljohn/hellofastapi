from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return 'Hello FastAPI'

@app.get("/message")
def root():
    return { "message": "Hello FastAPI" }