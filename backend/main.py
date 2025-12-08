from fastapi import FastAPI, HTTPException, Depends, status, Response
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, MenuItem, Client
from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime, timedelta
import os
from auth import (
    generate_client_id, 
    generate_client_key, 
    get_client_key_hash, 
    verify_client_key,
    create_access_token,
    get_current_client
)


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  
        "http://localhost:3002", 
        "http://localhost:3000",  
        "https://myrestaurants-apps-ezhfzcbwcabecrdb.eastus2-01.azurewebsites.net", 
        "https://d3r-restaurant-frontend.azurestaticapps.net", 
        "https://*.azurestaticapps.net",  
        "https://d3r-frontend-g2dydbdqf4fug6hr.southeastasia-01.azurewebsites.net",  
        "https://*.azurewebsites.net",
        "https://d3r-frontend.onrender.com",  # Render frontend
        "https://d3r-backend.onrender.com",   # Render backend
        "https://*.onrender.com",  # All Render sites
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic models
class MenuItemBase(BaseModel):
    name: str
    description: str
    price: float
    category: str
    image: Optional[str] = None
    popular: bool = False

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemResponse(MenuItemBase):
    id: int
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)

# Authentication Pydantic models
class ClientRegister(BaseModel):
    email: str
    name: str

class ClientRegisterResponse(BaseModel):
    client_id: str
    client_key: str
    email: str
    name: str
    message: str

class ClientLogin(BaseModel):
    client_id: str
    client_key: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

class ClientInfoResponse(BaseModel):
    client_id: str
    email: str
    name: str
    is_active: bool
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


# Routes
@app.get("/")
def read_root():
    return {"message": "Welcome to the Menu API"}

# ============ AUTHENTICATION ENDPOINTS ============

@app.post("/api/auth/register", response_model=ClientRegisterResponse, status_code=status.HTTP_201_CREATED)
def register_client(client_data: ClientRegister, db: Session = Depends(get_db)):
    """Register a new client and generate credentials"""
    
    # Check if email already exists
    existing_client = db.query(Client).filter(Client.email == client_data.email).first()
    if existing_client:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Generate credentials
    client_id = generate_client_id()
    client_key = generate_client_key()
    client_key_hash = get_client_key_hash(client_key)
    
    # Create new client
    new_client = Client(
        client_id=client_id,
        client_key_hash=client_key_hash,
        email=client_data.email,
        name=client_data.name,
        is_active=True
    )
    
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    
    return {
        "client_id": client_id,
        "client_key": client_key,
        "email": client_data.email,
        "name": client_data.name,
        "message": "Client registered successfully. Please save your client_key securely - it won't be shown again!"
    }

@app.post("/api/auth/login", response_model=TokenResponse)
def login_client(credentials: ClientLogin, db: Session = Depends(get_db)):
    """Login with client_id and client_key to get access token"""
    
    # Find client by client_id
    client = db.query(Client).filter(Client.client_id == credentials.client_id).first()
    
    if not client:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid client_id or client_key"
        )
    
    # Verify client_key
    if not verify_client_key(credentials.client_key, client.client_key_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid client_id or client_key"
        )
    
    # Check if client is active
    if not client.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Client account is inactive"
        )
    
    # Create access token
    access_token = create_access_token(data={"sub": client.client_id})
    
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@app.get("/api/auth/client-info", response_model=ClientInfoResponse)
def get_client_info(current_client: Client = Depends(get_current_client)):
    """Get current authenticated client information"""
    return current_client


@app.get("/api/auth/clients", response_model=List[ClientInfoResponse])
def list_all_clients(db: Session = Depends(get_db)):
    """List all registered clients (admin endpoint)"""
    clients = db.query(Client).all()
    return clients

# ============ MENU ENDPOINTS ============

@app.get("/api/menu/", response_model=List[MenuItemResponse])
def get_menu_items(
    response: Response,
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db)
):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    
    items = db.query(MenuItem).offset(skip).limit(limit).all()
    return items

@app.get("/api/menu/{item_id}", response_model=MenuItemResponse)
def get_menu_item(
    item_id: int, 
    response: Response,
    db: Session = Depends(get_db)
):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    
    db_item = db.query(MenuItem).filter(MenuItem.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return db_item

@app.post("/api/menu/", response_model=MenuItemResponse, status_code=status.HTTP_201_CREATED)
def create_menu_item(
    item: MenuItemCreate, 
    db: Session = Depends(get_db)
):
    db_item = MenuItem(**item.dict())
    
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    
    return db_item

@app.put("/api/menu/{item_id}", response_model=MenuItemResponse)
def update_menu_item(
    item_id: int, 
    item: MenuItemCreate, 
    db: Session = Depends(get_db)
):
    # Query the database for the item
    db_item = db.query(MenuItem).filter(MenuItem.id == item_id).first()
    
    # If item not found, return 404
    if db_item is None:
        raise HTTPException(status_code=404, detail="Menu item not found")
    
    # Update the item with new values
    update_data = item.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_item, key, value)
    
    # Save changes to database
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    
    return db_item

@app.delete("/api/menu/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_menu_item(
    item_id: int, 
    db: Session = Depends(get_db)
):
    # Query the database for the item
    db_item = db.query(MenuItem).filter(MenuItem.id == item_id).first()
    
    # If item not found, return 404
    if db_item is None:
        raise HTTPException(status_code=404, detail="Menu item not found")
    
    # Delete the item
    db.delete(db_item)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)