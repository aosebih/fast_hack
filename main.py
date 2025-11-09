import os
from fastapi import FastAPI, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

project_root = os.path.dirname(__file__)
frontend_dir = os.path.join(project_root, "frontend")

# mount a static directory that actually exists (avoid runtime error)
if os.path.isdir(frontend_dir):
    static_dir = frontend_dir
    index_path = os.path.join(frontend_dir, "index.html")
else:
    static_dir = project_root
    index_path = os.path.join(project_root, "index.html")

app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
async def root():
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"detail": "No frontend index.html found. During development, run your React dev server (npm start) at http://localhost:3000."}

@app.get("/calculate")
def calculate(w: float = Query(..., gt=0), h: float = Query(..., gt=0)):
    bmi = w / (h ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    return {"bmi": round(bmi, 2), "category": category}
