from fastapi import APIRouter, Depends, Path, HTTPException
from sqlalchemy.orm import Session
from app.api.auth import verify_token
from app.data.base import get_db
from app.schemas import TrackResponse, ArtistResponse
from app.crud.artist import (
    get_all_artists,
    get_artist_info,
)
from app.crud.track import get_artist_tracks

router = APIRouter(dependencies=[Depends(verify_token)])


@router.get("/all", response_model=list[ArtistResponse])
def fetch_all_artists(db: Session = Depends(get_db)):
    original_artists = get_all_artists(db)
    if not original_artists:
        raise HTTPException(status_code=404, detail="No artists found")
    return original_artists


@router.get("/info/{artist_id}", response_model=ArtistResponse)
def fetch_artist_info(
    artist_id: int = Path(..., title="Original Artist ID"),
    db: Session = Depends(get_db),
):
    artist = get_artist_info(db, artist_id)
    if not artist:
        raise HTTPException(status_code=404, detail="Aritst not found")
    return artist


@router.get("/tracks/{artist_id}", response_model=list[TrackResponse])
def fetch_artist_tracks(
    artist_id: int = Path(..., title="Original Artist ID"),
    db: Session = Depends(get_db),
):
    og_artist = get_artist_info(db, artist_id)
    if not og_artist:
        raise HTTPException(status_code=404, detail="Artist not found")
    tracks = get_artist_tracks(db, artist_id)
    if not tracks:
        raise HTTPException(
            status_code=404,
            detail="No tracks found for the given original artist",
        )
    return tracks
