from sqlalchemy.orm import Session
from app.models.track import Track
from app.schemas.track import TrackResponse


def get_all(db: Session):
    tracks = db.query(Track).all()
    return [TrackResponse.from_orm(track) for track in tracks]


def get_track_info(db: Session, track_id: int):
    track = db.query(Track).filter(Track.id == track_id).first()
    if not track:
        return None
    return TrackResponse.from_orm(track)


def get_track_filename(db: Session, track_id: int):
    track = db.query(Track).filter(Track.id == track_id).first()
    track_filename = f"{track.filename}.{track.format}" if track else None
    return track_filename


def get_artist_tracks(db: Session, artist_id: int):
    tracks = db.query(Track).filter(Track.artist_id == artist_id).all()
    if not tracks:
        return []
    return [TrackResponse.from_orm(track) for track in tracks]


def get__og_artist_tracks(db: Session, og_artist_id: int):
    tracks = (
        db.query(Track).filter(Track.original_artist_id == og_artist_id).all()
    )
    if not tracks:
        return []
    return [TrackResponse.from_orm(track) for track in tracks]
