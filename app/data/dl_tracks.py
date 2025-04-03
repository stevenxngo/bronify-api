import csv
import sys
import yt_dlp
from pathlib import Path
from ..log import get_logger

logger = get_logger()

BASE_DIR = Path(__file__).resolve().parent

csv_file = BASE_DIR / "tracks.csv"
output_dir = BASE_DIR / "tracks"

output_dir.mkdir(parents=True, exist_ok=True)

try:
    with open(csv_file, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        urls = list(reader)
except FileNotFoundError:
    logger.error("CSV file not found at %s", csv_file)
    sys.exit()

for entry in urls:
    url = entry.get("url", "").strip()
    filename = entry.get("filename", "").strip()
    file_format = entry.get("format", "mp3").strip()

    if not url or not filename:
        logger.info(
            "Skipping invalid entry, missing url or filename: %s",
            entry,
        )
        continue

    output_file = output_dir / filename

    if output_file.with_suffix(f".{file_format}").exists():
        logger.info(
            "Skipping %s.%s, file already exists.",
            filename,
            file_format,
        )
        continue

    ydl_opts = {
        "format": "bestaudio/best",
        "extract_audio": True,
        "audio_format": file_format,
        "outtmpl": str(output_file),
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": file_format,
                "preferredquality": "192",
            }
        ],
    }

    logger.info(
        "Downloading audio from %s as %s.%s",
        url,
        filename,
        file_format,
    )

    with yt_dlp.YoutubeDL(ydl_opts) as ydl_instance:
        ydl_instance.download([url])

logger.info(
    "All downloads completed. Check the output directory: %s",
    output_dir,
)
