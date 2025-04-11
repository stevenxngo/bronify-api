from fastapi import APIRouter, Depends, Path, HTTPException
from sqlalchemy.orm import Session
from app.api.auth import verify_token
from app.data.base import get_db
from app.schemas import TrackResponse, OriginalArtistResponse
from app.crud.original_artist import (
    get_all_original_artists,
    get_original_artist_info,
)
from app.crud.track import get__og_artist_tracks

router = APIRouter(dependencies=[Depends(verify_token)])


@router.get("/all", response_model=list[OriginalArtistResponse])
def fetch_all_original_artists(db: Session = Depends(get_db)):
    original_artists = get_all_original_artists(db)
    if not original_artists:
        raise HTTPException(status_code=404, detail="No original artists found")
    return original_artists


@router.get("/info/{og_artist_id}", response_model=OriginalArtistResponse)
def fetch_original_artist_info(
    og_artist_id: int = Path(..., title="Original Artist ID"),
    db: Session = Depends(get_db),
):
    og_artist = get_original_artist_info(db, og_artist_id)
    if not og_artist:
        raise HTTPException(status_code=404, detail="Original aritst not found")
    return og_artist


@router.get("/tracks/{og_artist_id}", response_model=list[TrackResponse])
def fetch_original_artist_tracks(
    og_artist_id: int = Path(..., title="Original Artist ID"),
    db: Session = Depends(get_db),
):
    og_artist = get_original_artist_info(db, og_artist_id)
    if not og_artist:
        raise HTTPException(status_code=404, detail="Original artist not found")
    tracks = get__og_artist_tracks(db, og_artist_id)
    if not tracks:
        raise HTTPException(
            status_code=404,
            detail="No tracks found for the given original artist",
        )
    return tracks
