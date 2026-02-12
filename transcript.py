from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
import json

api = YouTubeTranscriptApi()


def get_video_id(url: str) -> str:
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    return query_params["v"][0]


def get_transcript(video_id: str):
    transcript_list = api.list(video_id)

    try:
        return transcript_list.find_transcript(["en"]).fetch()
    except:
        return transcript_list.find_generated_transcript(["hi"]).fetch()


video_url = "https://www.youtube.com/watch?v=1nAlZrccKBs&t=2s"



with open("transcript.json", "w", encoding="utf-8") as f:
    transcript = get_transcript(get_video_id(video_url))

    data = [
        {
            "text": entry.text,
            "start": round(entry.start, 2),
            "duration": round(entry.duration, 2)
        }
        for entry in transcript
    ]

    json.dump(data, f, indent=4, ensure_ascii=False)




