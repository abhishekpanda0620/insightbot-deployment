from fastapi import FastAPI, File, UploadFile
from parser import extract_errors
from ai_engine import summarize_errors

app = FastAPI()

@app.post("/analyze")
async def analyze_log(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8")
    errors = extract_errors(text)
    summary = summarize_errors(errors)
    return {"summary": summary, "errors": errors}
