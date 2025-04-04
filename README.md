# Bronify API

Simple audio streaming API that stores and plays Lebron James' parodies of popular songs, inspired by the TikTok trend.

![Bronify Meme](./media/bronify.png?raw=true "Bronify Meme")

## Features

- 🎵 Stream LeBron James parody tracks
- 📄 Get detailed track metadata
- 🎤 Organize and query by artist
- 🔍 Search, random track, and stats endpoints
- 💾 Built with Python, FastAPI and SQLite

## Endpoints

### Track Endpoints

| Method | Endpoint                 | Description                                     |
| ------ | ------------------------ | ----------------------------------------------- |
| `GET`  | `/track/all`             | Returns a list of all tracks with metadata.     |
| `GET`  | `/track/info/{track_id}` | Returns detailed metadata for a specific track. |
| `GET`  | `/track/play/{track_id}` | Streams the audio for a specific track.         |
| `GET`  | `/track/random`          | Streams a random track from the collection.     |

### Artist Endpoints

| Method | Endpoint                     | Description                                      |
| ------ | ---------------------------- | ------------------------------------------------ |
| `GET`  | `/artist/all`                | Returns a list of all artists.                   |
| `GET`  | `/artist/info/{artist_id}`   | Returns detailed metadata for a specific artist. |
| `GET`  | `/artist/tracks/{artist_id}` | Returns a list of tracks for a specific artist.  |

### Original Artist Endpoints

| Method | Endpoint                        | Description                                               |
| ------ | ------------------------------- | --------------------------------------------------------- |
| `GET`  | `/og_artist/all`                | Returns a list of all original artists.                   |
| `GET`  | `/og_artist/info/{artist_id}`   | Returns detailed metadata for a specific original artist. |
| `GET`  | `/og_artist/tracks/{artist_id}` | Returns a list of tracks for a specific artist.           |

## Setup and Running Locally

# 1. Clone the repo

git clone https://github.com/stevenxngo/bronify.git
cd bronify

# 2. Create and activate a virtualenv

python -m venv venv
source venv/bin/activate

# 3. Install dependencies

pip install -r requirements.txt

# 4. Run the app

uvicorn app.main:app --reload

## License

This project is open-sourced under the [MIT License](https://opensource.org/licenses/MIT).
