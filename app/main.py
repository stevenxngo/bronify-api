from fastapi import FastAPI
from app.api.routes import shared, tracks, artists, original_artists

app = FastAPI(title="Bronify")

app.include_router(shared.router, tags=["Search"])
app.include_router(tracks.router, prefix="/track", tags=["Tracks"])
app.include_router(
    artists.router,
    prefix="/artist",
    tags=["Artists"],
)
app.include_router(
    original_artists.router,
    prefix="/og_artist",
    tags=["Original Artists"],
)


@app.get("/")
def root():
    return {"message": "Bronify"}
