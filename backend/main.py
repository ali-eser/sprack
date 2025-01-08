from fastapi import FastAPI, Request
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline
import os

app = FastAPI()

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

@app.get("/")
async def analyze_sentiment(req: Request):
    result = classifier("I got left out but managed to get back in")
    return result[0]