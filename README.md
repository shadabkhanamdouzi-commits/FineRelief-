💰 AI-Powered Debt Relief & Financial Recovery Platform (FinRelief AI)

An AI-powered financial assistance platform that helps borrowers analyze their financial health, predict loan settlement possibilities, and generate AI-based negotiation strategies for better debt recovery.

Built using React.js, FastAPI, SQLite, SQLAlchemy, and Google Gemini AI.



📌 Features

- 🔐 Secure User Registration & Login
- 💼 User Financial Profile Management
- 💳 Loan Management System
- 📊 Financial Health Analysis
- 💰 AI-Based Settlement Prediction
- 🤖 AI Negotiation Strategy Generator
- 📈 Dashboard with Financial Insights
- 📝 AI History Tracking
- 🧪 API Testing with Swagger UI

---

🏗️ Project Architecture

User
   ↓
React.js Frontend
   ↓
FastAPI Backend
   ↓
Business Logic Layer
 ├── Authentication
 ├── Financial Health Engine
 ├── Settlement Prediction Engine
 ├── AI Negotiation Engine
 └── Loan Management
   ↓
SQLite Database + Google Gemini API


📂 Project Structure

AI-Powered-Debt-Relief-Financial-Recovery-Platform/
│
├── .git/
├── backend/
│   ├── app/
│   │   ├── AI/
│   │   ├── Auth/
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   └── models.py
│   │   ├── routes/
│   │   │   ├── AI.py
│   │   │   ├── AI_routes.py
│   │   │   ├── debts.py
│   │   │   └── users.py
│   │   ├── services/
│   │   │   └── gemini_service.py
│   │   ├── __init__.py
│   │   ├── ai_negotiation_engine.py
│   │   ├── auth.py
│   │   ├── auth_utils.py
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── financial_engine.py
│   │   ├── main.py
│   │   ├── schemas.py
│   │   └── settlement_engine.py
│   │
│   ├── venv/
│   ├── .env
│   ├── .gitignore
│   ├── dependencies.py
│   ├── finrelief.db
│   ├── package-lock.json
│   └── requirements.txt
│
├── frontend/
│   ├── node_modules/
│   ├── public/
│   ├── src/
│   ├── .git/
│   ├── index.html
│   ├── package.json
│   ├── package-lock.json
│   ├── README.md
│   └── vite.config.js
│
├── ER_Diagram/
├── requests/
├── venv/
├── package-lock.json
└── README.md

---

⚙️ Technologies Used

Technology| Purpose
React.js| Frontend UI
FastAPI| Backend API
SQLite| Database
SQLAlchemy| ORM
Google Gemini AI| AI Negotiation Strategy
JWT| Authentication
PyTest| API Testing
Git & GitHub| Version Control

---

🚀 Installation

### Option 1: Docker (Recommended)

**Prerequisites:**
- Docker & Docker Compose installed

**Quick Start:**

```bash
# Clone repository
git clone <repository-url>
cd FineRelief-

# Build and start services
docker-compose up --build
```

**Access the application:**
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

**Or use the startup script:**

```bash
chmod +x start.sh
./start.sh
```

### Option 2: Local Development

1. Clone Repository

```bash
git clone <repository-url>
cd FineRelief-
```

2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate Environment

**Windows:**
```bash
.venv\Scripts\activate
```

**Linux / macOS:**
```bash
source .venv/bin/activate
```

3. Install Dependencies

```bash
# Backend
cd backend
pip install -r requirements.txt

# Frontend
cd ../frontend
npm install
```

---

▶️ Run Backend (Local)

```bash
cd backend
uvicorn app.main:app --reload
```

Backend URL: http://127.0.0.1:8000

Swagger Documentation: http://127.0.0.1:8000/docs

---

▶️ Run Frontend (Local)

```bash
cd frontend
npm run dev
```

Frontend URL: http://localhost:5173

---

🧪 Running Tests

pytest -v


🌟 Future Enhancements

- Email Notifications
- Multi-bank Integration
- Credit Score Analysis
- PDF Financial Reports
- Cloud Deployment (AWS/Azure)
- Mobile Application

---

👨‍💻 Team Members

Project: AI-Powered Debt Relief & Financial Recovery Platform

- Team Leader: Madhu Thaddi
Github Repository : https://github.com/Mithun9661/FineRelief
- Member 1: Mithun Kumar
- Member 2: Mani Prabha Bhuvanasi
- Member 3: Durga Prasad Gandiboina
- Member 4: Lohitha Gude

---

📜 License

This project was developed for educational purposes as part of the Skill Wallet Internship Program.-