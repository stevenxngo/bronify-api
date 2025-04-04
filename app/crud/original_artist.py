from sqlalchemy.orm import Session
from app.models.original_artist import OriginalArtist


def get_all_original_artists(db: Session):
    original_artists = db.query(OriginalArtist).all()
    return original_artists


def get_original_artist_info(db: Session, og_artist_id: int):
    og_artist = (
        db.query(OriginalArtist)
        .filter(OriginalArtist.id == og_artist_id)
        .first()
    )
    if not og_artist:
        return None
    return og_artist
