from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from . import agent
from .system_prompt import prompt
from .ad_auction import ad_auction
from .unsplash_api import get_unsplash_image_url

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserInput(BaseModel):
    input: str

@app.post("/chat")
async def chat(user_input: UserInput):
    try:
        inputs = {"messages": [("user", prompt+user_input.input)]}
        config = {"configurable": {"thread_id": "thread-1"}}
        response = agent.get_response(inputs, config)
        image_url = get_unsplash_image_url(str(response.city)+" skyline")
        response.imgAddress = image_url
        response.ad_auction = ad_auction(str(response.description))
        return {"response": response}
    except Exception as e:
        return {"error": str(e)}