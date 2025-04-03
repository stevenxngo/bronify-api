from pathlib import Path
import pandas as pd
from sqlalchemy.orm import Session
from .database import engine, Base
from ..models.track import Track
from ..models.artist import Artist
from ..models.original_artist import OriginalArtist

BASE_DIR = Path(__file__).resolve().parent

Base.metadata.create_all(bind=engine)


def import_csv():
    db = Session(bind=engine)

    tracks_df = pd.read_csv(BASE_DIR / "tracks.csv")

    unique_artists = tracks_df["artist"].unique()
    for artist in unique_artists:
        existing_artist = db.query(Artist).filter_by(name=artist).first()
        if not existing_artist:
            db.add(Artist(name=artist))

    unique_original_artists = tracks_df["original_artist"].unique()
    print(unique_original_artists)
    for original_artist in unique_original_artists:
        if not pd.isna(original_artist):
            print(original_artist)
            existing_original_artist = (
                db.query(OriginalArtist).filter_by(name=original_artist).first()
            )
            if not existing_original_artist:
                db.add(OriginalArtist(name=original_artist))

    for _, row in tracks_df.iterrows():
        existing_track = db.query(Track).filter_by(title=row["title"]).first()

        if not existing_track:
            artist = db.query(Artist).filter_by(name=row["artist"]).first()
            original_artist = (
                db.query(OriginalArtist)
                .filter_by(name=row["original_artist"])
                .first()
            )

            db.add(
                Track(
                    title=row["title"],
                    artist_id=artist.id,
                    original_title=row["original_title"],
                    original_artist_id=(
                        (original_artist.id) if original_artist else None
                    ),
                    filename=row["filename"],
                    format=row["format"],
                    url=row["url"],
                )
            )

    db.commit()
    db.close()


import_csv()
