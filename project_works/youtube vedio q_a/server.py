# installing fastapi uvicorn

"""
   fastapi : 
        FastAPI is a modern, high-performance web framework for building APIs with Python.
   uvicorn :
        Uvicorn is a lightning-fast ASGI (Asynchronous Server Gateway Interface) server for Python web apps. 
        It's the production-ready server most commonly used to run FastAPI apps. 
   youtube-transcript-api :     
        Fetch Transcript via Backend Using youtube-transcript-api
        We can auto-fetch transcripts using this Python library:
   YoutubeLoader :
        class langchain_community.document_loaders.youtube.YoutubeLoader(video_id: str, add_video_info: bool = False, 
        language: str | Sequence[str] = 'en', translation: str | None = None, transcript_format: TranscriptFormat = TranscriptFormat.TEXT, 
        continue_on_failure: bool = False, chunk_size_seconds: int = 120)[source]
        Load YouTube video transcripts.

        Initialize with YouTube video ID.   
"""
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from langchain_openai import ChatOpenAI
import os 
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import TextLoader
from youtube_transcript_api import YouTubeTranscriptApi
from langchain_community.document_loaders import YoutubeLoader



load_dotenv()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
prompt = PromptTemplate(
    template = "Use a Transcript to answer the question in english - \n {question} \n from the text/transcript - \n{text}"
)
model = ChatOpenAI(model = "gpt-4o-mini")
parser = StrOutputParser()

def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['hi','ur','en-IN','en', 'en-US', 'en-GB'])
        return " ".join([t["text"] for t in transcript])
    except Exception as e:
        print("Transcript fetch failed:", str(e))
        return "Transcript not available"


@app.post("/ask")
async def ask_question(req: Request):
    body = await req.json()
    # transcript = body['transcript']
    video_id = body.get("video_id")
    question = body['question']
    video_url = body.get("video_url")
    print(video_id, video_url)
    transcript = ""

    if video_url:
        video_id = video_url.split("v=")[-1].split("&")[0]
        print("Trying YoutubeLoader...")
        try:
            print("Using YoutubeLoader with:", video_url)
            loader = YoutubeLoader.from_youtube_url(video_url,add_video_info=False,language="hi")
            docs = loader.load()
            if docs:
                transcript = docs[0].page_content
                print("YoutubeLoader transcript loaded.")
            else:
                raise ValueError("YoutubeLoader returned no documents.")
        except Exception as e:
            print("YoutubeLoader failed:", e)
        if not transcript or transcript.strip().lower().startswith("transcript not available"):
            print("Falling back to youtube_transcript_api with video_id:", video_id)
            transcript = get_transcript(video_id)
    elif video_id:
        print("Using youtube_transcript_api with video_id:", video_id)
        transcript = get_transcript(video_id)
    elif "transcript" in body:
        transcript = body["transcript"]
    print("Transcript loaded:", transcript[:500], "...") 

    chain = prompt | model | parser
    
    response = chain.invoke({'question': question, 'text': transcript})
    print("Question:", question)
    print("Response:", response)
    
    return {"answer": response}