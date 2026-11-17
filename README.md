# Student Academic Early-Warning & Intervention System

A Machine Learning-based web application that predicts whether a student may be academically at risk using academic indicators such as age, academic percentage, and attendance percentage.

## Overview

The Student Academic Early-Warning & Intervention System is designed to demonstrate how machine learning can help identify students who may need academic support.

The application uses a **Random Forest Classifier** to predict academic risk and provides the result through a web-based interface connected to a FastAPI backend.

## Features

- Predicts whether a student is **At Risk** or **Not At Risk**.
- Uses three numerical features:
  - Age
  - Academic Percentage
  - Attendance Percentage
- Random Forest classification model.
- FastAPI-based prediction API.
- Interactive web interface.
- Displays predicted risk status and estimated probability.

## Machine Learning Model

**Algorithm:** Random Forest Classifier

**Dataset:** UCI Student Performance Dataset (Mathematics)

**Dataset Information:**
- Total Records: 395
- Original Features: 33
- At-Risk Students: 130
- Not-At-Risk Students: 265

### Target Variable

The target variable `academic_risk` is created using the final grade (G3):

- `1` = At Risk (G3 < 10)
- `0` = Not At Risk (G3 >= 10)

### Model Features

| Feature | Description |
|---|---|
| Age | Student's age |
| Academic Percentage | Derived from first-period grade (G1) |
| Attendance Percentage | Approximated using absence records |

## Model Performance

The model achieved the following results on the held-out test dataset:

| Metric | Score |
|---|---:|
| Accuracy | 86.08% |
| Precision | 75.86% |
| Recall | 84.62% |
| F1-Score | 80.00% |

## Technology Stack

**Programming Language:** Python

**Machine Learning:** Scikit-learn, Pandas, NumPy

**Backend:** FastAPI, Pydantic

**Frontend:** HTML, CSS, JavaScript, Chart.js

**Model Saving:** Joblib

**Tools:** Jupyter Notebook, VS Code, Git, GitHub

## Project Structure

```text
student-academic-early-warning-system/
│
├── backend/
│   └── main.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── data/
│   └── student-mat.csv
│
├── models/
│   └── academic_risk_model_3features.pkl
│
├── LPU_EWS.ipynb
├── train_model.py
├── requirements.txt
└── README.md
```

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/aniketraj009/student-academic-early-warning-system.git
```

### 2. Navigate to the Project Directory

```bash
cd student-academic-early-warning-system
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Start the Backend

```bash
uvicorn backend.main:app --reload
```

Backend API:

```text
http://127.0.0.1:8000
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

### 7. Run the Frontend

Open `frontend/index.html` using VS Code Live Server.

## API Endpoint

**POST** `/predict`

The FastAPI backend receives student information, prepares the three model features, and returns the predicted academic risk class and estimated probability.

## Limitations

- The model is trained on the public UCI Student Performance dataset, not actual LPU student records.
- Attendance percentage is approximated from absence counts using an assumed 100-day scale.
- Academic percentage is derived from G1, the first-period grade.
- The model has not been validated on real institutional student data.
- Predictions should be treated as estimates, not final academic decisions.

## Future Improvements

- Integrate verified institutional student data.
- Improve attendance calculation using actual attendance records.
- Explore additional machine learning algorithms.
- Add explainable AI for understanding prediction factors.
- Develop a more comprehensive student monitoring dashboard.

## Author

**Aniket Raj**

GitHub: [@aniketraj009](https://github.com/aniketraj009)

---

If you find this project interesting, feel free to explore the repository and share your feedback.

**Built with Python, Machine Learning, and FastAPI.**
