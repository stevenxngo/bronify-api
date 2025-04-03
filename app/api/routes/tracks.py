from fastapi import APIRouter, Depends, Path, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.schemas.track import TrackBase
from app.crud.track_crud import get_track


router = APIRouter()


@router.get("/id/{track_id}", response_model=TrackBase)
def fetch_track(
    track_id: int = Path(..., title="Track ID"), db: Session = Depends(get_db)
):
    track = get_track(db, track_id)
    if not track:
        raise HTTPException(status_code=404, detail="Track not found")
    return track
