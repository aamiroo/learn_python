from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def hello ():
    return{
    "message" : "hello" ,
    "mame" : "amir",
    "github" : "https://github.com/aamiroo"
    }