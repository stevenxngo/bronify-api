from pathlib import Path as PathLib
import random
from fastapi import APIRouter, Depends, Path, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.schemas.track import TrackResponse
from app.crud.track import (
    get_all,
    get_track_info,
    get_all_files,
    get_track_file,
)

BASE_DIR = PathLib(__file__).resolve().parent.parent.parent

router = APIRouter()


@router.get("/all", response_model=list[TrackResponse])
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
    track_file = get_track_file(db, track_id)
    if not track_file:
        raise HTTPException(status_code=404, detail="Track not found")

    file_path = f"{BASE_DIR}/data/tracks/{track_file}"

    return FileResponse(
        path=file_path, media_type="audio/mpeg", filename=track_file
    )


@router.get("/random")
def play_random_track(db: Session = Depends(get_db)):
    tracks = get_all_files(db)
    if not tracks:
        raise HTTPException(status_code=404, detail="No tracks found")

    random_track = random.choice(tracks)

    file_path = f"{BASE_DIR}/data/tracks/{random_track}"

    return FileResponse(
        path=file_path,
        media_type="audio/mpeg",
        filename=f"{random_track}",
    )
