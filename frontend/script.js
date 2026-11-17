
// LPU EWS - Complete Frontend JavaScript


// 1. Dashboard Charts

const riskChart = document.getElementById("risk-chart");
const performanceChart = document.getElementById("performance-chart");

riskChart.innerHTML = '<canvas id="riskCanvas"></canvas>';
performanceChart.innerHTML = '<canvas id="performanceCanvas"></canvas>';

new Chart(document.getElementById("riskCanvas"), {
    type: "doughnut",
    data: {
        labels: ["Not At Risk", "At Risk"],
        datasets: [{
            data: [265, 130],
            backgroundColor: ["#3b82f6", "#ef4444"],
            borderWidth: 0
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                position: "bottom",
                labels: {
                    color: "#e5e7eb"
                }
            }
        }
    }
});

new Chart(document.getElementById("performanceCanvas"), {
    type: "bar",
    data: {
        labels: ["Accuracy", "Precision", "Recall", "F1 Score"],
        datasets: [{
            data: [86.08, 75.86, 84.62, 80.00],
            backgroundColor: [
                "#3b82f6",
                "#8b5cf6",
                "#22c55e",
                "#f59e0b"
            ],
            borderRadius: 6
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            y: {
                beginAtZero: true,
                max: 100,
                ticks: {
                    color: "#94a3b8"
                }
            },
            x: {
                ticks: {
                    color: "#94a3b8"
                }
            }
        },
        plugins: {
            legend: {
                display: false
            }
        }
    }
});


// 2. Sidebar Navigation

const navigationLinks = document.querySelectorAll(".navigation a");
const dashboardSection = document.querySelector(".dashboard-section");
const predictionSection = document.getElementById("prediction-section");
const mainContent = document.querySelector(".main-content");
const topbarTitle = document.querySelector(".topbar h1");

const pageTitles = [
    "Dashboard",
    "Student Prediction",
    "Data Overview",
    "Advanced Visualizations",
    "Model Performance",
    "Feature Analysis",
    "About Project"
];

navigationLinks.forEach((link, index) => {

    link.addEventListener("click", function(event) {

        event.preventDefault();

        navigationLinks.forEach(item => {
            item.classList.remove("active");
        });

        this.classList.add("active");

        const oldPage = document.querySelector(".dynamic-page");

        if (oldPage) {
            oldPage.remove();
        }

        dashboardSection.style.display = "none";
        predictionSection.style.display = "none";

        topbarTitle.textContent = pageTitles[index];

        if (index === 0) {
            dashboardSection.style.display = "block";
            return;
        }

        if (index === 1) {
            predictionSection.style.display = "block";
            return;
        }

        const page = document.createElement("section");

        page.className = "dynamic-page content-card";

        page.innerHTML = `
            <h2>${pageTitles[index]}</h2>
            <p style="color:#94a3b8; margin-top:15px;">
                This section will be developed next.
            </p>
        `;

        mainContent.insertBefore(
            page,
            mainContent.querySelector("footer")
        );

    });

});


// 3. Student Prediction API Connection

const predictionForm = document.getElementById("predictionForm");

predictionForm.addEventListener("submit", async function(event) {

    event.preventDefault();

    const submitButton = predictionForm.querySelector(
        "button[type='submit']"
    );

    const resultBox = document.getElementById("prediction-result");

    const formData = new FormData(predictionForm);

    const studentData = {
        student_name: formData.get("student_name").trim(),
        age: Number(formData.get("age")),
        academic_percentage: Number(formData.get("percentage")),
        attendance_percentage: Number(formData.get("attendance"))
    };

    if (
        !studentData.student_name ||
        !Number.isInteger(studentData.age) ||
        studentData.age < 15 ||
        studentData.age > 22 ||
        !Number.isFinite(studentData.academic_percentage) ||
        studentData.academic_percentage < 0 ||
        studentData.academic_percentage > 100 ||
        !Number.isFinite(studentData.attendance_percentage) ||
        studentData.attendance_percentage < 0 ||
        studentData.attendance_percentage > 100
    ) {
        resultBox.innerHTML = `
            <div class="prediction-result-card">
                <h3 style="color:#ef4444;">
                    Invalid Input
                </h3>
                <p>Please enter valid student details.</p>
            </div>
        `;
        return;
    }

    submitButton.disabled = true;
    submitButton.textContent = "Predicting...";

    resultBox.innerHTML = `
        <p>Analyzing student information...</p>
    `;

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/predict",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(studentData)
            }
        );

        const result = await response.json();

        if (!response.ok) {
            throw new Error(
                typeof result.detail === "string"
                    ? result.detail
                    : JSON.stringify(result.detail || "Prediction failed")
            );
        }

        const isAtRisk = result.prediction === 1;
        const probability = Number(result.risk_probability);

        resultBox.innerHTML = `
            <div class="prediction-result-card">

                <h3>
                    ${isAtRisk
                        ? "⚠️ Student At Risk"
                        : "✅ Student Not At Risk"}
                </h3>

                <p style="color:#94a3b8;">
                    Student Name:
                    <strong>${escapeHTML(result.student_name)}</strong>
                </p>

                <h2 style="color:${isAtRisk ? "#ef4444" : "#22c55e"}">
                    ${escapeHTML(result.risk_status)}
                </h2>

                <p style="margin-top:12px;">
                    Estimated Risk Probability:
                    <strong>${probability.toFixed(2)}%</strong>
                </p>

                <div style="
                    background:#334155;
                    height:12px;
                    border-radius:10px;
                    margin-top:15px;
                ">

                    <div style="
                        width:${Math.max(0, Math.min(100, probability))}%;
                        height:12px;
                        border-radius:10px;
                        background:${isAtRisk ? "#ef4444" : "#22c55e"};
                    "></div>

                </div>

                <p style="
                    margin-top:15px;
                    color:#94a3b8;
                    font-size:13px;
                ">
                    Prediction generated using the 3-feature
                    Random Forest model. This is a prototype
                    and should not replace faculty assessment.
                </p>

            </div>
        `;

    } catch (error) {

        resultBox.innerHTML = `
            <div class="prediction-result-card">
                <h3 style="color:#ef4444;">
                    Prediction Error
                </h3>

                <p>${escapeHTML(error.message)}</p>

                <p>
                    Check that your FastAPI server is running.
                </p>
            </div>
        `;

    } finally {

        submitButton.disabled = false;
        submitButton.textContent = "Predict Academic Risk";

    }

});


// 4. Safe HTML Display

function escapeHTML(value) {

    return String(value).replace(/[&<>"']/g, character => ({
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#039;"
    })[character]);

}


console.log("LPU EWS Dashboard Loaded!");
