# 🎯 Smart Task Priority Predictor

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3%2B-black?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.2%2B-orange?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![SQLite](https://img.shields.io/badge/SQLite-3-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Bootstrap 5](https://img.shields.io/badge/Bootstrap-5.3-7952B3?logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![Chart.js](https://img.shields.io/badge/Chart.js-4.0-FF6384?logo=chartdotjs&logoColor=white)](https://www.chartjs.org/)
[![Tests](https://img.shields.io/badge/Tests-Passing%20(6%2F6)-brightgreen?logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Author](https://img.shields.io/badge/Author-Sanjay%20S-informational?logo=github&logoColor=white)](https://github.com/Sanjay13-Maker)

> An intelligent, hybrid Python web application combining **Machine Learning (Decision Tree Classifier)** with a **Rule-Based Scoring Engine** to predict and explain task priorities (**Critical**, **High**, **Medium**, **Low**) in real-time.

---

## 🌟 Key Features

- 🧠 **Hybrid Priority Engine**: Blends a multi-parameter scoring formula with a trained Scikit-Learn Decision Tree Classifier.
- 💡 **Explainable AI (XAI)**: Provides human-readable reasoning for every predicted priority level (e.g., tight deadline, high business impact, blocker status).
- 📊 **Interactive Analytics Dashboard**: Live task distribution metrics and Chart.js priority breakdown visualizations.
- ⚡ **Batch CSV Prediction**: Upload and evaluate hundreds of tasks simultaneously with downloadable result reports.
- 🛡️ **Manual Priority Override**: Allows managers to manually adjust priorities with mandatory audit trail reasons.
- 🔐 **User Authentication & OTP Reset**: Secure session-based authentication with local simulated OTP recovery for quick demos.
- 🧪 **100% Test Coverage**: Full suite of unit and integration tests covering scoring formulas, feature pipelines, and database CRUD.
- 🚀 **Cloud-Ready**: Pre-configured with `render.yaml` and `Procfile` for instant deployment on cloud platforms.

---

## 📐 Priority Scoring Formula

The hybrid scoring model calculates priority using weighted attributes:

$$\text{Score} = (\text{Business Impact} \times 4) + (\text{Urgency} \times 3) + (\text{Dependency Count} \times 2) + \text{Deadline Points}$$

### Deadline Weight Matrix:
| Deadline Window | Points |
|---|---|
| **Overdue** | +20 pts |
| **Within 2 days** | +15 pts |
| **Within 7 days** | +10 pts |
| **Within 14 days** | +7 pts |
| **Beyond 14 days** | +3 pts |

### Effort Adjustments:
- **Quick Win** ($< 3\text{ hrs}$): $+5\text{ pts}$
- **Heavy Effort** ($> 20\text{ hrs}$): $-5\text{ pts}$

### Priority Classification:
| Score Range | Priority Label | Badge Color |
|---|---|---|
| **80 – 100** | 🔴 Critical | Danger |
| **60 – 79** | 🟠 High | Warning |
| **40 – 59** | 🟡 Medium | Info |
| **0 – 39** | 🟢 Low | Success |

---

## 🛠️ Tech Stack & Architecture

- **Backend Framework**: Python Flask 2.3+
- **Machine Learning**: Scikit-learn (Decision Tree Classifier) & Joblib
- **Data Engineering**: Pandas, NumPy
- **Database**: SQLite3 (Thread-safe dict-like row factory)
- **Frontend**: HTML5, Modern CSS, Bootstrap 5.3, Font Awesome, Chart.js
- **Testing**: Pytest (6/6 automated test suites)
- **Deployment**: Gunicorn, Render (`render.yaml`), Heroku (`Procfile`)

---

## 📂 Project Structure

```
Smart_Task_Priority_Predictor/
├── app.py                  # Flask application routes & session controller
├── database.py             # SQLite schema, migrations & CRUD operations
├── models.py               # Domain constants (Task types, statuses, priorities)
├── prediction.py           # Scoring engine, ML inference & explanation generator
├── preprocessing.py        # Feature engineering & one-hot encoding pipelines
├── train_model.py          # Machine learning model training script
├── requirements.txt        # Production & development dependencies
├── render.yaml             # Render cloud deployment blueprint
├── Procfile                # Gunicorn process definition for cloud hosts
├── LICENSE                 # MIT License
├── README.md               # Project documentation
│
├── data/
│   └── tasks.csv           # 100-task training dataset
│
├── models/
│   └── priority_model.pkl  # Pretrained Decision Tree model
│
├── static/
│   ├── css/
│   │   └── style.css       # Custom styling, dark modes, animations
│   └── js/
│       └── main.js         # Client-side validation & dynamic charts
│
├── templates/              # Jinja2 HTML templates
│   ├── base.html           # Master navigation & theme shell
│   ├── login.html          # Authentication login
│   ├── register.html       # User registration
│   ├── dashboard.html      # Metrics overview & Chart.js charts
│   ├── tasks.html          # Task inventory list
│   ├── task_form.html      # Create / edit task with instant prediction
│   ├── task_detail.html    # Task insights, explanations & override audit
│   ├── batch_prediction.html # Bulk CSV upload and analytics
│   ├── forgot_password.html # Password recovery
│   └── verify_otp.html     # OTP verification
│
└── tests/                  # Pytest test suite
    ├── test_priority.py    # Unit tests for scoring formula & explanations
    ├── test_validation.py  # Unit tests for deadline calculation & features
    └── test_tasks.py       # Integration tests for database CRUD
```

---

## 🚀 Quick Start Guide

### 1. Clone the Repository
```bash
git clone https://github.com/Sanjay13-Maker/smart-task-priority-predictor.git
cd smart-task-priority-predictor
```

### 2. Set Up a Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. (Optional) Re-train the Machine Learning Model
The repository includes a pre-trained model. If you wish to retrain it:
```bash
python train_model.py
```

### 5. Launch the Application
```bash
python app.py
```

Visit **`http://127.0.0.1:5000`** in your browser.

---

## 🧪 Running Automated Tests

Run the complete Pytest suite to verify scoring accuracy, feature preprocessing, and database transactions:

```bash
python -m pytest -v
```

Expected result:
```
tests/test_priority.py::test_deadline_points PASSED               [ 16%]
tests/test_priority.py::test_calculate_priority_score PASSED      [ 33%]
tests/test_priority.py::test_explanations_generator PASSED        [ 50%]
tests/test_tasks.py::test_user_and_task_crud PASSED               [ 66%]
tests/test_validation.py::test_calculate_days_to_deadline PASSED  [ 83%]
tests/test_validation.py::test_prepare_single_task_features PASSED[100%]

============================== 6 passed in 6.78s ==============================
```

---

## ⚙️ Environment Configuration

| Variable | Default Value | Description |
|---|---|---|
| `FLASK_SECRET_KEY` | `smart_task_priority_secret_key_2026` | Secret key for Flask user sessions |
| `DATABASE_PATH` | `task_priority.db` | Local SQLite database file location |
| `MODEL_PATH` | `models/priority_model.pkl` | Path to trained Scikit-learn model |
| `DATA_PATH` | `data/tasks.csv` | Path to employee tasks dataset |

---

## 👨‍💻 Author

**Sanjay S**
- GitHub: [@Sanjay13-Maker](https://github.com/Sanjay13-Maker)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
