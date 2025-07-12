from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse, Response
import shutil
import os

app = FastAPI()

# Make sure the uploads folder exists
os.makedirs("uploads", exist_ok=True)

@app.get("/")
def read_root():
    return {"message": "Welcome to PennyPilot API"}

# Handles both GET and HEAD requests to /form
@app.get("/form", response_class=HTMLResponse)
@app.head("/form")
async def upload_form(request: Request):
    if request.method == "HEAD":
        return Response(status_code=200)

    # Otherwise return the form HTML
    return """
    <html>
    <head><title>Upload to PennyPilot</title></head>
    <body>
        <h2>📁 Upload a file to PennyPilot Agent</h2>
        <form action="/upload" enctype="multipart/form-data" method="post">
            <input name="file" type="file">
            <input type="submit" value="Upload">
        </form>
    </body>
    </html>
    """

@app.post("/upload", response_class=HTMLResponse)
async def upload_file(file: UploadFile = File(...)):
    with open(f"uploads/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return f"""
        <html>
        <body>
            <h3>✅ File '{file.filename}' uploaded successfully!</h3>
            <a href="/form">Upload another</a>
        </body>
        </html>
    """