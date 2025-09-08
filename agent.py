from pytubefix import YouTube
from youtube_transcript_api import YouTubeTranscriptApi, FetchedTranscript
from typing import List
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
import asyncio
import os

api_key_name = "OPENAI_API_KEY"

async def get_video_transcript(url: str) -> str:
    """Given a url of type str, return the title, description, and transcript of the video in a str"""
    yt = YouTube(url)
    description: str = yt.description
    title: str = yt.title
    video_id: str = url.split('v=')[1].split('&')[0]
    yt_transcript_fetcher: YouTubeTranscriptApi = YouTubeTranscriptApi()
    fetched_transcript: FetchedTranscript = yt_transcript_fetcher.fetch(video_id, ['en'])
    transcript_text: str = ' '.join([one_snipet.text for one_snipet in fetched_transcript.snippets])
    result = f'Title: {title}\n\nDescription: {description}\n\nTranscript: {transcript_text}'
    return result

async def get_video_transcript_with_timestamp(url: str) -> str:
    """Given a url of type str, return the title, description, and transcript of the video in a str"""
    yt = YouTube(url)
    description: str = yt.description
    title: str = yt.title
    video_id: str = url.split('v=')[1].split('&')[0]
    yt_transcript_fetcher: YouTubeTranscriptApi = YouTubeTranscriptApi()
    fetched_transcript: FetchedTranscript = yt_transcript_fetcher.fetch(video_id, languages=['en'])
    transcript_text: str = ', '.join([str(one_snipet.start) + ":" + one_snipet.text for one_snipet in fetched_transcript.snippets])
    result = f'Title: {title}\n\nDescription: {description}\n\nTranscript with timestamp: {transcript_text}'
    return result

async def query(url, query):
    model = OpenAIChatCompletionClient(
        model="o4-mini", 
        api_key=os.getenv(api_key_name),
        temperature=0
    )
    agent = AssistantAgent(
        name="YouTube_Video_Proxy",
        system_message="""
        You are a helpful assistant, you will be given a url of a youtube video, and the user
        will ask you questions about the video. You can the tool to answer the user's questions. If 
        the answer to the question is not in the video, you should say "I don't know the answer." """,
        tools = [
             get_video_transcript,
             get_video_transcript_with_timestamp
        ]
        model = model
    )

if __name__ == "__main__":
    url = 'https://www.youtube.com/watch?v=9_PepvnqIfU&t=461s'
    result = asyncio.run(get_video_transcript_with_timestamp(url))
    print(result)