from fastapi import FastAPI

app = FastAPI()

# when someone visits this route, the root function will run and will return the Hello World object
@app.get("/hello")
def hello():
    return {"message": "Hello, World"}
