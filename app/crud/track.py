from sqlalchemy.orm import Session
from app.models.track import Track
from app.schemas.track import TrackBase, TrackResponse


def get_all(db: Session):
    tracks = db.query(Track).all()
    return [
        TrackResponse.from_orm(track)
        for track in tracks
    ]

def get_track_info(db: Session, track_id: int):
    track = db.query(Track).filter(Track.id == track_id).first()
    if not track:
        return None
    return TrackResponse.from_orm(track)

def get_track_filename(db: Session, track_id: int):
    track = db.query(Track).filter(Track.id == track_id).first()
    track_filename = f"{track.filename}.{track.format}" if track else None
    return track_filename
