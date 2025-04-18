# Bronify API

Simple audio streaming API that stores and plays Lebron James' parodies of popular songs, inspired by the TikTok trend. This is only a fun side project and is not affiliated with LeBron James, Spotify, or any artists/creators.

![Bronify Meme](./media/bronify.png?raw=true "Bronify Meme")

## Features

- 🎵 Stream LeBron James parody tracks
- 📄 Get detailed track metadata
- 🎤 Organize and query by artist
- 🔍 Search, random track, and stats endpoints
- 💾 Built with Python, FastAPI and SQLite

## Endpoints

### Search

| Method | Endpoint                                    | Description                                      |
|--------|---------------------------------------------|--------------------------------------------------|
| `GET`  | `/search?query={query}&category={category}` | Searches for tracks, artists or orignal artists. |

> **Note**: `category` can be `tracks`, `artists`, or `original_artists`. If omitted, all categories will be searched.

### Tracks

| Method | Endpoint                 | Description                                     |
| ------ | ------------------------ | ----------------------------------------------- |
| `GET`  | `/track/all`             | Returns a list of all tracks with metadata.     |
| `GET`  | `/track/info/{track_id}` | Returns detailed metadata for a specific track. |
| `GET`  | `/track/play/{track_id}` | Streams the audio for a specific track.         |
| `GET`  | `/track/random`          | Streams a random track from the collection.     |

### Artists

| Method | Endpoint                     | Description                                      |
| ------ | ---------------------------- | ------------------------------------------------ |
| `GET`  | `/artist/all`                | Returns a list of all artists.                   |
| `GET`  | `/artist/info/{artist_id}`   | Returns detailed metadata for a specific artist. |
| `GET`  | `/artist/tracks/{artist_id}` | Returns a list of tracks for a specific artist.  |

### Original Artists

| Method | Endpoint                        | Description                                               |
| ------ | ------------------------------- | --------------------------------------------------------- |
| `GET`  | `/og_artist/all`                | Returns a list of all original artists.                   |
| `GET`  | `/og_artist/info/{artist_id}`   | Returns detailed metadata for a specific original artist. |
| `GET`  | `/og_artist/tracks/{artist_id}` | Returns a list of tracks for a specific artist.           |

## Setup and Running Locally

### 1. Clone the repo

```bash
git clone https://github.com/stevenxngo/bronify.git
cd bronify
```

### 2. Create and activate a virtualenv

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download tracks and initialize the database

```bash
# Download the audio files from TikTok
python -m app.data.dl_tracks

# Initialize the SQLite database and populate it
python -m app.data.init_db
```

### 5. Run the app

```bash
uvicorn app.main:app --reload
```

## Usage and Authentication

All endpoints require a bearer token for access which must be added to the `Authorization` header of your requests. The token can be customized by setting the `BRONIFY_TOKEN` environment variable.



## Adknowledgements

- **LeBron James** for being a glorious king and inspiring this project with his greatness.
- **All the talented TikTok creators** who made the original parodies that inspired this project.

## License

This project is open-sourced under the [MIT License](/LICENSE).
