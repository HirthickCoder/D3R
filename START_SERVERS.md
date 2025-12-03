# 🚀 START BOTH SERVERS - Simple Guide

## Step-by-Step Connection

### ✅ Step 1: Start Backend (Terminal 1)

Open PowerShell/Command Prompt and run:

```powershell
cd backend
python seed_data.py
python main.py
```

**✅ Backend running on:** http://localhost:8000

You should see:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

---

### ✅ Step 2: Start Frontend (Terminal 2)

Open a NEW PowerShell/Command Prompt and run:

```powershell
npm run dev
```

**✅ Frontend running on:** http://localhost:5173

---

### ✅ Step 3: Test Connection

1. **Open browser:** http://localhost:5173
2. **Check Home page** - should show items from database
3. **Check Menu page** - should also show items from database

**What's connected now:**
- ✅ Home page → fetches from PostgreSQL via FastAPI
- ✅ Menu page → fetches from PostgreSQL via FastAPI
- ✅ All data stored in `menu_items` table

---

## 🧪 Test the Full Connection

### View Database Data

```bash
cd backend
python view_menu.py
```

### Test Adding Data via API

**Method 1: Using Swagger UI**
1. Go to http://localhost:8000/docs
2. Click **POST /api/menu/**
3. Click "Try it out"
4. Enter:
```json
{
  "name": "Test Pizza",
  "description": "This is a test item",
  "price": 350,
  "category": "pizza",
  "image": "/images/pizza.jpg",
  "popular": true
}
```
5. Click "Execute"
6. **Refresh your React app** → New item appears! ✨

**Method 2: Using PowerShell**

```powershell
curl -X POST http://localhost:8000/api/menu/ `
  -H "Content-Type: application/json" `
  -d '{\"name\": \"Test Item\", \"description\": \"Test\", \"price\": 199, \"category\": \"main\", \"popular\": false}'
```

Then refresh http://localhost:5173 and see the new item!

---

## ✅ Verification Checklist

- [ ] PostgreSQL is running
- [ ] Backend server started (port 8000)
- [ ] Frontend dev server started (port 5173)
- [ ] Database has menu items (`python view_menu.py`)
- [ ] Home page shows menu items
- [ ] Menu page shows menu items
- [ ] Can add items via API
- [ ] New items appear after refresh

---

## 🔄 What Happens Now

```
PostgreSQL Database (menu_items table)
         ↕
FastAPI Backend (port 8000)
    GET /api/menu/
    POST /api/menu/
    PUT /api/menu/{id}
    DELETE /api/menu/{id}
         ↕
React Frontend (port 5173)
    Home.jsx → fetches menu items
    Menu.jsx → fetches menu items
```

**Any changes in the database → Immediately visible in frontend (after refresh)**

---

## 🐛 Troubleshooting

### "Failed to load menu items"
```bash
# Check if backend is running
curl http://localhost:8000/api/menu/

# Should return JSON array of menu items
```

### Empty menu on frontend
```bash
# Add sample data
cd backend
python seed_data.py
```

### CORS Error
- Make sure backend `main.py` has: `allow_origins=["http://localhost:5173"]`

### Port conflicts
- Backend: Change port in `main.py` → `uvicorn.run(app, port=8001)`
- Frontend: Use `npm run dev -- --port 3000`

---

## 🎉 Success!

If you see menu items on both Home and Menu pages, **your frontend is successfully connected to the PostgreSQL database via FastAPI!** 🚀

Now any changes you make in the database will reflect in your React app.
