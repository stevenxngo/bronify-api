from pathlib import Path as PathLib
from fastapi import APIRouter, Depends, Path, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.schemas.track import TrackBase, TrackResponse
from app.crud.track import (
    get_all,
    get_track_info,
    get_track_filename,
)

BASE_DIR = PathLib(__file__).resolve().parent.parent.parent

router = APIRouter()


@router.get("/all", response_model=list[TrackBase])
def fetch_all_tracks(db: Session = Depends(get_db)):
    tracks = get_all(db)
    if not tracks:
        raise HTTPException(status_code=404, detail="No tracks found")
    return tracks


@router.get("/info/{track_id}", response_model=TrackResponse)
def fetch_track_info(
    track_id: int = Path(..., title="Track ID"), db: Session = Depends(get_db)
):
    track = get_track_info(db, track_id)
    if not track:
        raise HTTPException(status_code=404, detail="Track not found")
    return track


@router.get("/play/{track_id}", response_class=FileResponse)
def play_track(
    track_id: int = Path(..., title="Track ID"), db: Session = Depends(get_db)
):
    track_filename = get_track_filename(db, track_id)
    if not track_filename:
        raise HTTPException(status_code=404, detail="Track not found")

    file_path = f"{BASE_DIR}/data/tracks/{track_filename}"

    return FileResponse(
        path=file_path, media_type="audio/mpeg", filename=track_filename
    )
