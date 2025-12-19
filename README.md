# 🩺 Public Health AI Chatbot

An AI-driven public health awareness chatbot built using **FastAPI (Python)** and **React (Vite)**.

## 🚀 Features
- Disease awareness (Dengue, Malaria, COVID)
- Symptom & prevention guidance
- Emergency keyword detection
- Modern, responsive UI
- Runs fully locally (no internet required)

## 🛠 Tech Stack
- Backend: FastAPI (Python)
- Frontend: React + Vite
- API Communication: REST

## ▶️ How to Run Locally

### Backend
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m uvicorn main:app --reload --port 8000
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

Open:
- Frontend: http://localhost:5173
- Backend API: http://127.0.0.1:8000

## ⚠️ Disclaimer
This chatbot is for **educational purposes only** and does not provide medical diagnosis.
