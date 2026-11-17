
from pathlib import Path

import joblib
import pandas as pd

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "academic_risk_model_3features.pkl"

app = FastAPI(title="LPU Academic Early-Warning API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_methods=["GET", "POST"],
    allow_headers=["*"]
)

model = joblib.load(MODEL_PATH)


class StudentData(BaseModel):
    student_name: str = Field(min_length=1, max_length=100)
    age: int = Field(ge=15, le=22)
    academic_percentage: float = Field(ge=0, le=100)
    attendance_percentage: float = Field(ge=0, le=100)


@app.get("/")
def home():
    return {
        "message": "LPU EWS API is running",
        "model": "Random Forest",
        "features": 3
    }


@app.post("/predict")
def predict(student: StudentData):

    try:
        student_df = pd.DataFrame([{
            "age": student.age,
            "academic_percentage": student.academic_percentage,
            "attendance_percentage": student.attendance_percentage
        }])

        prediction = int(model.predict(student_df)[0])

        probability = float(
            model.predict_proba(student_df)[0][
                list(model.classes_).index(1)
            ]
        )

        return {
            "student_name": student.student_name,
            "prediction": prediction,
            "risk_status": "At Risk" if prediction == 1 else "Not At Risk",
            "risk_probability": round(probability * 100, 2)
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )
