# 🚀 Quick Start Guide - FoodieHub

This guide will get your FastAPI backend + React frontend running with PostgreSQL.

## Prerequisites

- ✅ PostgreSQL installed and running
- ✅ Python 3.8+ installed
- ✅ Node.js installed
- ✅ Git Bash or PowerShell

---

## Step 1: Start PostgreSQL

Make sure PostgreSQL is running with your database credentials:
- **Username**: `postgres`
- **Password**: `root`
- **Database**: `postgres`
- **Port**: `5432`

---

## Step 2: Setup & Start Backend (FastAPI)

### Terminal 1 - Backend

```bash
# Navigate to backend folder
cd backend

# Install Python dependencies (first time only)
pip install -r requirements.txt

# Seed the database with initial menu items
python seed_data.py

# Start the FastAPI server
python main.py
```

✅ Backend will run on **http://localhost:8000**

You should see:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete.
```

Visit http://localhost:8000/docs to see the API documentation.

---

## Step 3: Start Frontend (React)

### Terminal 2 - Frontend

```bash
# From project root (not backend folder)
cd ..

# Install Node dependencies (first time only)
npm install

# Start React dev server
npm run dev
```

✅ Frontend will run on **http://localhost:5173**

---

## Step 4: Test Everything

1. Open browser to **http://localhost:5173**
2. Click **Menu** in the navbar
3. You should see menu items loaded from the database!

---

## 🧪 Test CRUD Operations

### View API Documentation
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Test with cURL or Postman

**GET all items:**
```bash
curl http://localhost:8000/api/menu/
```

**POST new item:**
```bash
curl -X POST http://localhost:8000/api/menu/ \
  -H "Content-Type: application/json" \
  -d "{\"name\": \"New Item\", \"description\": \"Test\", \"price\": 199, \"category\": \"main\", \"popular\": false}"
```

**PUT update item (ID 1):**
```bash
curl -X PUT http://localhost:8000/api/menu/1 \
  -H "Content-Type: application/json" \
  -d "{\"name\": \"Updated Name\", \"description\": \"Updated\", \"price\": 299, \"category\": \"main\", \"popular\": true}"
```

**DELETE item (ID 1):**
```bash
curl -X DELETE http://localhost:8000/api/menu/1
```

---

## 🔄 See Changes Reflect in Frontend

1. Keep both servers running
2. Add/update/delete items using the API (Swagger UI or cURL)
3. Refresh the React **Menu** page
4. Changes will appear immediately! ✨

---

## 📁 Project Structure

```
my-react-app/
├── backend/                 # FastAPI Backend
│   ├── main.py             # API routes (GET, POST, PUT, DELETE)
│   ├── models.py           # Database models
│   ├── database.py         # PostgreSQL connection
│   ├── seed_data.py        # Initial data script
│   ├── requirements.txt    # Python dependencies
│   └── README.md           # Backend documentation
│
├── src/                    # React Frontend
│   ├── pages/
│   │   └── Menu.jsx       # Menu page (fetches from API)
│   ├── components/
│   │   └── Navbar.jsx     # Navigation
│   └── context/
│       └── CartContext.jsx
│
└── QUICKSTART.md          # This file
```

---

## ⚙️ Configuration

### Backend Port (FastAPI)
**File**: `backend/main.py`
```python
uvicorn.run(app, host="0.0.0.0", port=8000)
```

### Frontend API URL
**File**: `src/pages/Menu.jsx`
```javascript
const API_BASE_URL = 'http://localhost:8000';
```

### Database Connection
**File**: `backend/database.py`
```python
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:root@localhost:5432/postgres"
```

---

## 🐛 Troubleshooting

### Backend won't start
- Check PostgreSQL is running
- Verify credentials in `backend/database.py`
- Run: `pip install -r requirements.txt`

### Frontend shows "Failed to load menu items"
- Make sure backend is running on port 8000
- Check browser console for errors
- Verify CORS settings in `backend/main.py`

### Database empty
- Run: `python seed_data.py` from backend folder

### Port already in use
- Backend: Change port in `main.py`
- Frontend: Use different port with `npm run dev -- --port 3000`

---

## 🎉 You're All Set!

Now when you:
- **Add a menu item** via API → It appears in frontend
- **Update a menu item** → Changes show on refresh
- **Delete a menu item** → It disappears from menu

The backend (FastAPI + PostgreSQL) is now fully connected to your React frontend! 🚀
