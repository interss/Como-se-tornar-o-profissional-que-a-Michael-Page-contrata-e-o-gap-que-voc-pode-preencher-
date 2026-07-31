import json
import sys
from youtube_transcript_api import YouTubeTranscriptApi

video_ids = {
    "pv0J-DHsu-g": "video1",
    "O26VX_SRtdk": "video2",
    "MNR468ZegVI": "video3",
    "aiemUUl5dhY": "video4",
}

api = YouTubeTranscriptApi()

for vid, name in video_ids.items():
    try:
        transcript = api.fetch(vid, languages=["pt", "pt-BR", "en", "a.pt"])
        text = " ".join(snippet.text for snippet in transcript)
        out_path = f"transcript_{name}_{vid}.txt"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"OK {vid} -> {out_path} ({len(text)} chars)")
    except Exception as e:
        print(f"FAIL {vid}: {type(e).__name__}: {e}")
