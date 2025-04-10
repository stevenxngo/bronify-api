from sqlalchemy.orm import Session
from app.models import Track, Artist, OriginalArtist
from app.schemas import TrackResponse


def get_all(db: Session):
    tracks = db.query(Track).all()
    return [TrackResponse.from_orm(track) for track in tracks]


def get_track_info(db: Session, track_id: int):
    track = db.query(Track).filter(Track.id == track_id).first()
    if not track:
        return None
    return TrackResponse.from_orm(track)


def get_all_files(db: Session):
    tracks = db.query(Track).all()
    if not tracks:
        return []
    return [f"{track.filename}.{track.format}" for track in tracks]


def get_track_file(db: Session, track_id: int):
    track = db.query(Track).filter(Track.id == track_id).first()
    track_file = f"{track.filename}.{track.format}" if track else None
    return track_file


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


def search_tracks(db: Session, query: str):
    tracks = (
        db.query(Track)
        .filter(Track.title.ilike(f"%{query}%"))
        .all()
    )

    if not tracks:
        return []

    return [TrackResponse.from_orm(track) for track in tracks]


def search_all(db: Session, query: str):
    tracks = (
        db.query(Track)
        .join(Artist)
        .join(OriginalArtist)
        .filter(
            Track.title.ilike(f"%{query}%")
            | Artist.name.ilike(f"%{query}%")
            | Track.original_title.ilike(f"%{query}%")
            | OriginalArtist.name.ilike(f"%{query}%")
        )
        .all()
    )

    if not tracks:
        return []

    return [TrackResponse.from_orm(track) for track in tracks]
