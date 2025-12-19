from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from engine import build_response

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Chat(BaseModel):
    message: str

@app.post("/chat")
def chat(data: Chat):
    return build_response(data.message)

@app.get("/")
def root():
    return {"status": "running"}
