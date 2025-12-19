from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from openai import OpenAI

# Load env variables
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI(title="Public Health AI Chatbot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

SYSTEM_PROMPT = """
You are a public health awareness assistant.
You provide disease awareness, symptoms, prevention tips, and when to seek medical care.
You must NOT give diagnosis or prescriptions.
Always include a short medical disclaimer.
"""

@app.get("/")
def health():
    return {"status": "running"}

@app.post("/chat")
def chat(req: ChatRequest):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": req.message},
        ],
        temperature=0.4,
        max_tokens=400,
    )

    reply = response.choices[0].message.content

    return {
        "reply": reply
    }