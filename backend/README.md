# FastAPI Backend - FoodieHub

This is the FastAPI backend for the FoodieHub food delivery application with PostgreSQL database.

## Features

- ✅ **GET** `/api/menu/` - Get all menu items
- ✅ **GET** `/api/menu/{id}` - Get single menu item
- ✅ **POST** `/api/menu/` - Create new menu item
- ✅ **PUT** `/api/menu/{id}` - Update menu item
- ✅ **DELETE** `/api/menu/{id}` - Delete menu item

## Setup

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Configure PostgreSQL

Make sure PostgreSQL is running and update `database.py` with your credentials:

```python
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:root@localhost:5432/postgres"
```

Or update the `.env` file:

```
DATABASE_URL=postgresql://postgres:root@localhost:5432/postgres
```

### 3. Seed the Database

Add initial menu items to the database:

```bash
python seed_data.py
```

### 4. Start the Server

```bash
python main.py
```

Or using uvicorn directly:

```bash
uvicorn main:app --reload --port 8000
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, visit:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Testing the API

### Using cURL

**GET all menu items:**
```bash
curl http://localhost:8000/api/menu/
```

**GET single item:**
```bash
curl http://localhost:8000/api/menu/1
```

**POST new menu item:**
```bash
curl -X POST http://localhost:8000/api/menu/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "New Pizza",
    "description": "Delicious pizza",
    "price": 299,
    "category": "pizza",
    "image": "/images/pizza.jpg",
    "popular": true
  }'
```

**PUT update item:**
```bash
curl -X PUT http://localhost:8000/api/menu/1 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Updated Pizza Name",
    "description": "Updated description",
    "price": 350,
    "category": "pizza",
    "image": "/images/pizza.jpg",
    "popular": true
  }'
```

**DELETE item:**
```bash
curl -X DELETE http://localhost:8000/api/menu/1
```

### Using Python requests

```python
import requests

# GET all items
response = requests.get("http://localhost:8000/api/menu/")
print(response.json())

# POST new item
new_item = {
    "name": "Test Item",
    "description": "Test description",
    "price": 199,
    "category": "test",
    "image": "/images/test.jpg",
    "popular": False
}
response = requests.post("http://localhost:8000/api/menu/", json=new_item)
print(response.json())
```

## Database Schema

### MenuItem Table

| Column | Type | Description |
|--------|------|-------------|
| id | Integer | Primary key |
| name | String | Item name |
| description | String | Item description |
| price | Float | Price in rupees |
| category | String | Category (pizza, pasta, etc.) |
| image | String | Image URL/path |
| popular | Boolean | Popular item flag |
| created_at | DateTime | Creation timestamp |

## CORS Configuration

The backend is configured to accept requests from:
- `http://localhost:5173` (React Vite dev server)

To add more origins, update `main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Troubleshooting

### Database Connection Error

If you see `could not connect to server`, make sure:
1. PostgreSQL is running
2. Database credentials in `database.py` are correct
3. Database `postgres` exists

### CORS Error in Frontend

Make sure the FastAPI server is running and the CORS middleware includes your React app's URL.

### Port Already in Use

If port 8000 is busy, change it in `main.py`:

```python
uvicorn.run(app, host="0.0.0.0", port=8001)
```

And update the frontend `API_BASE_URL` in `Menu.jsx`.
