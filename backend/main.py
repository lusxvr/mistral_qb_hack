from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

from . import agent

app = FastAPI()

class UserInput(BaseModel):
    input: str

@app.post("/chat")
async def chat(user_input: UserInput):
    try:
        inputs = {"messages": [("user", user_input.input)]}
        config = {"configurable": {"thread_id": "thread-1"}}
        response = agent.get_response(agent.get_agent(), inputs, config)
        return {"response": response}
    except Exception as e:
        return {"error": str(e)}