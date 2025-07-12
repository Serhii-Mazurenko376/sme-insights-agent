from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import uvicorn

from chain import summarize_performance, analyze_risks, generate_final_insights

app = FastAPI(title="PennyPilot – SME Insights API")

@app.get("/")
def read_root():
    return {"message": "Welcome to PennyPilot API"}

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8")

    summary = summarize_performance(text)
    risks = analyze_risks(text)
    insights = generate_final_insights(summary, risks)

    return JSONResponse(content={"insights": insights})

from fastapi.responses import HTMLResponse

@app.get("/form", response_class=HTMLResponse)
def form():
    with open("upload.html", "r") as f:
        return f.read()