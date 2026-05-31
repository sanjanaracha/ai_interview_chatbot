from fastapi import FastAPI, Request
from openai import OpenAI
import os

app = FastAPI()

client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL")
)


@app.get("/")
def home():
    return {"message": "Backend Running Successfully"}


@app.post("/questions")
async def questions(req: Request):
    data = await req.json()
    prompt = data["prompt"]
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return {
        "response": response.choices[0].message.content
    }