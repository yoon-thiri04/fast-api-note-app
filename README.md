# FastAPI Note App 📝

This is a simple backend testing project built with **FastAPI**, **MongoDB**, and **Python**. It includes **JWT Authentication** to secure API endpoints and demonstrates modern backend development practices.

## 🚀 Features
- User registration and login with JWT-based authentication
- Create, read, update, and delete notes (CRUD)
- Connects to MongoDB for data persistence
- Basic testing with Postman of API endpoints 

### ▶️ Running the App

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   
2. **Run FastAPI Server:**
   ```bash
   uvicorn app.main:app --reload

##  📁 Project Stucture 

```
📁 app/
├── 📁 crud/
│   ├── user.py
│   └── note.py
├── 📁 models/
│   ├── user.py
│   └── note.py
├── 📁 routes/
│   ├── user.py
│   └── note.py
├── 📁 utils/
│   ├── authentication.py
│   └── password.py
├── db.py
├── main.py
└── config.py
requirements.txt
README.md
.env
```


