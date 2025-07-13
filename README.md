# 🧠 OverLang AI Health Assistant – Backend

This is the backend for the **OverLang AI Health Assistant**, a FastAPI-powered engine that receives quiz responses, classifies them by age group, calls OpenAI GPT for personalized wellness recommendations, and delivers email confirmations via SMTP.

> ❗ No medical diagnosis is provided. The assistant returns only general, non-diagnostic wellness suggestions.

---

## 🚀 Core Features

- 🔄 REST API built with **FastAPI**
- 🤖 OpenAI GPT-4 integration for personalized responses
- 👶 Age group classification: child, teen, adult, senior
- 🛡️ AI system prompt guardrails to avoid unsafe output
- ✉️ Email capture + confirmation using **Mailtrap SMTP**
- 💡 Daily motivational tip engine via `/api/daily-tip`
- 📦 Clean modular structure with `models`, `services`, `routers`, `utils`

---

## ⚙️ Setup Instructions

### 1️⃣ Create a Virtual Environment

```bash
cd backend
python -m venv .venv
source .venv/Scripts/activate   # macOS/Linux: source .venv/bin/activate
```

2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

3️⃣ Create .env File
Create a .env file in /backend/ using this format:

``` bash
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxx
MAILTRAP_USERNAME=your_mailtrap_username
MAILTRAP_PASSWORD=your_mailtrap_password
DEBUG=True
```

4️⃣ Start the FastAPI Server
```bash

uvicorn main:app --reload
```


---

Would you like me to save this as a `.md` file for download or push?

Also happy to:
- Add a matching `LICENSE` file
- Generate Postman collection or Swagger schema
- Dockerize the backend for easier deployment

Just say the word.



