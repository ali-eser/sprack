from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline
import os

app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

model_name = "distilbert-base-uncased-finetuned-sst-2-english"
model_path = "models/sentiment"

if not os.path.exists(model_path):
    os.makedirs(model_path)

try:
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    tokenizer = AutoTokenizer.from_pretrained(model_path)

    model.save_pretrained(model_path)
    tokenizer.save_pretrained(model_path)
except Exception as e:
    print(f"Error downloading model. Error: {e}")

classifier = pipeline(model=model_name, tokenizer=tokenizer)

@app.post("/analysis")
async def analyze_sentiment(req: Request):
    data = await req.json()
    user_input = data["user_input"]
    print(user_input)
    result = classifier(user_input)
    print(result)
    return result[0]