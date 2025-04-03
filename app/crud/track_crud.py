from sqlalchemy.orm import Session
from app.models.track import Track
from app.schemas.track import TrackBase


def get_track(db: Session, track_id: int):
    track = db.query(Track).filter(Track.id == track_id).first()
    return TrackBase.from_orm_with_artists(track)
