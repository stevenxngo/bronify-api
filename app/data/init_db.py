from pathlib import Path
import pandas as pd
from sqlalchemy.orm import Session
from .database import engine, Base
from ..api.models import Track

BASE_DIR = Path(__file__).resolve().parent

Base.metadata.create_all(bind=engine)


def import_csv():
    db = Session(bind=engine)

    tracks_df = pd.read_csv(BASE_DIR / "tracks.csv")

    for _, row in tracks_df.iterrows():
        existing_track = db.query(Track).filter_by(title=row["title"]).first()

        if not existing_track:
            db.add(
                Track(
                    title=row["title"],
                    artist=row["artist"],
                    original_title=row["original_title"],
                    original_artist=row["original_artist"],
                    filename=row["filename"],
                    format=row["format"],
                    url=row["url"],
                )
            )

    db.commit()
    db.close()


import_csv()
