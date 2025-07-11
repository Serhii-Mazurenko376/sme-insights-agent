from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI(title="PennyPilot – SME Insights API")

@app.get("/")
def read_root():
    return {"message": "Welcome to PennyPilot API"}

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    # Placeholder: Here you can send 'content' to LangChain logic
    return JSONResponse(content={"filename": file.filename, "size": len(content)})

# Only for local/dev Replit use
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
