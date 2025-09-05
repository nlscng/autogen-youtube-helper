from pytubefix import YouTube
from youtube_transcript_api import YouTubeTranscriptApi, FetchedTranscript
from typing import List
import asyncio


async def get_video_transcript(url: str) -> str:
    """Given a url of type str, return the title, description, and transcript of the video in a str"""
    yt = YouTube(url)
    description: str = yt.description
    title: str = yt.title
    video_id: str = url.split('v=')[1].split('&')[0]
    yt_transcript_fetcher: YouTubeTranscriptApi = YouTubeTranscriptApi()
    feteched_transcript: FetchedTranscript = yt_transcript_fetcher.fetch(video_id, ['en'])
    transcript_text: str = ' '.join([one_snipet.text for one_snipet in feteched_transcript.snippets])
    result = f'Title: {title}\n\nDescription: {description}\n\nTranscript: {transcript_text}'
    return result


if __name__ == "__main__":
    url = 'https://www.youtube.com/watch?v=9_PepvnqIfU&t=461s'
    result = asyncio.run(get_video_transcript(url))
    print(result)