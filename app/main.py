from fastapi import FastAPI
from app.api.routes import tracks

app = FastAPI(title="Bronify")

app.include_router(tracks.router, prefix="/track", tags=["Tracks"])


@app.get("/")
def root():
    return {"message": "Bronify"}
