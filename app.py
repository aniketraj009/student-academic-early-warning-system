
import streamlit as st
import pandas as pd
from pathlib import Path

# Page Configuration
st.set_page_config(
    page_title="LPU Academic Early Warning System",
    page_icon="🎓",
    layout="wide"
)

# Load CSS
css_path = Path("assets/style.css")

if css_path.exists():
    with open(css_path) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# Load Dataset
df = pd.read_csv("data/student-mat.csv")
df["academic_risk"] = (df["G3"] < 10).astype(int)

# Sidebar
st.sidebar.title("🎓 LPU EWS")
st.sidebar.caption("Student Academic Early-Warning System")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "👨‍🎓 Student Prediction",
        "📊 Data Overview",
        "📈 Model Performance",
        "🔍 Feature Analysis",
        "ℹ️ About"
    ]
)

st.sidebar.divider()
st.sidebar.caption("Prototype Dataset")
st.sidebar.write(f"Total Records: {len(df)}")
st.sidebar.write(f"Features: {df.shape[1]}")

# Dashboard Page
if page == "🏠 Dashboard":

    st.title("🎓 Student Academic Early-Warning System")
    st.write("Monitor academic performance and identify students at risk.")

    st.divider()

    total_students = len(df)
    at_risk = int(df["academic_risk"].sum())
    safe_students = total_students - at_risk
    risk_percentage = (at_risk / total_students) * 100

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Students", total_students)
    col2.metric("At-Risk Students", at_risk)
    col3.metric("Not At Risk", safe_students)
    col4.metric("Risk Percentage", f"{risk_percentage:.2f}%")

    st.divider()

    left, right = st.columns(2)

    with left:
        st.subheader("Academic Risk Distribution")

        risk_data = pd.DataFrame({
            "Category": ["Not At Risk", "At Risk"],
            "Students": [safe_students, at_risk]
        })

        st.bar_chart(
            risk_data.set_index("Category")
        )

    with right:
        st.subheader("Average Student Grades")

        grade_data = pd.DataFrame({
            "Average Grade": [
                df["G1"].mean(),
                df["G2"].mean(),
                df["G3"].mean()
            ]
        }, index=["G1", "G2", "G3"])

        st.bar_chart(grade_data)

    st.divider()

    st.info(
        "This dashboard uses a public student dataset "
        "for academic risk prediction research."
    )

# Data Overview Page
elif page == "📊 Data Overview":

    st.title("📊 Dataset Overview")

    st.metric("Total Records", len(df))
    st.metric("Total Features", df.shape[1])

    st.subheader("Dataset Preview")
    st.dataframe(df.head(10), use_container_width=True)

    st.subheader("Statistical Summary")
    st.dataframe(df.describe(), use_container_width=True)

# Model Performance Page
elif page == "📈 Model Performance":

    st.title("📈 Random Forest Model Performance")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Accuracy", "81.01%")
    col2.metric("Precision", "66.67%")
    col3.metric("Recall", "84.62%")
    col4.metric("F1 Score", "74.58%")

    st.info(
        "Metrics are from the held-out test set "
        "of the tuned Random Forest model."
    )

# Feature Analysis Page
elif page == "🔍 Feature Analysis":

    st.title("🔍 Feature Analysis")

    st.subheader("Average Grades")

    st.bar_chart(df[["G1", "G2", "G3"]].mean())

    st.subheader("Academic Risk by Past Failures")

    failure_data = df.groupby(
        "failures"
    )["academic_risk"].mean() * 100

    st.bar_chart(failure_data)

# Student Prediction Page
elif page == "👨‍🎓 Student Prediction":

    st.title("👨‍🎓 Student Academic Risk Prediction")

    st.info(
        "Student prediction form will be added in the next development step."
    )

# About Page
elif page == "ℹ️ About":

    st.title("ℹ️ About This Project")

    st.write("""
    The LPU Student Academic Early-Warning System is a
    machine learning prototype designed to identify
    students who may be at academic risk.

    **Technology Stack**
    - Python
    - Pandas
    - Scikit-learn
    - Random Forest
    - Streamlit

    **Dataset:** UCI Student Performance Dataset.

    This is a research prototype, not an official LPU system.
    """)
