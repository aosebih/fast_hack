from fastapi import FastAPI,Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
app = FastAPI()

frontend_path = os.path.join(os.path.dirname(__file__), "frontend")

app.mount("/static", StaticFiles(directory=os.path.join(frontend_path)), name="static")

@app.get("/")
async def root():
    return FileResponse(os.path.join(frontend_path, "index.html"))

@app.get("/calculate")

def calculate(
    w: float = Query(..., gt=0),
    h: float = Query(..., gt=0)
):
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
