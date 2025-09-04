from pytubefix import YouTube
from youtube_transcript_api import YouTubeTranscriptApi, FetchedTranscript
from typing import List

url = 'https://www.youtube.com/watch?v=9_PepvnqIfU&t=461s'

yt = YouTube(url)

print(yt.title)
print(yt.description)


video_id: str = url.split('v=')[1].split('&')[0]
yt_transcript_fetcher: YouTubeTranscriptApi = YouTubeTranscriptApi()
res: FetchedTranscript = yt_transcript_fetcher.fetch(video_id, ['en'])

print(res)

transcript_text: str = ' '.join([item['text'] for item in res])

