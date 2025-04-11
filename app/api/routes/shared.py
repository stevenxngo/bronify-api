from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.auth import verify_token
from app.data.base import get_db
from app.schemas import TrackResponse, ArtistResponse, OriginalArtistResponse
from app.crud.track import (
    search_tracks,
    search_all,
)
from app.crud.artist import search_artists
from app.crud.original_artist import search_original_artists
from app.api.enums import Category

router = APIRouter(dependencies=[Depends(verify_token)])


@router.get(
    "/search",
    response_model=list[
        TrackResponse | ArtistResponse | OriginalArtistResponse
    ],
)
def search(
    query: str,
    category: Optional[Category] = None,
    db: Session = Depends(get_db),
):
    if category == Category.tracks:
        data = search_tracks(db, query)
    elif category == Category.artists:
        data = search_artists(db, query)
    elif category == Category.original_artists:
        data = search_original_artists(db, query)
    else:
        data = search_all(db, query)
    return data
