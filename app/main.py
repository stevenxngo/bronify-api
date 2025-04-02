from fastapi import FastAPI

app = FastAPI(title="Bronify")


@app.get("/")
def root():
    return {"message": "Bronify"}
