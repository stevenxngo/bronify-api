from enum import Enum


class Category(str, Enum):
    tracks = "tracks"
    artists = "artists"
    original_artists = "original_artists"
