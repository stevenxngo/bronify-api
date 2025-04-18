from sqlalchemy.orm import Session
from app.models.artist import Artist


def get_all_artists(db: Session):
    artists = db.query(Artist).all()
    return artists


def get_artist_info(db: Session, artist_id: int):
    artist = db.query(Artist).filter(Artist.id == artist_id).first()
    if not artist:
        return None
    return artist


def search_artists(db: Session, query: str):
    artists = (
        db.query(Artist)
        .filter(Artist.name.ilike(f"%{query}%"))
        .all()
    )

    if not artists:
        return []

    return artists
