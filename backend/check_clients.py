from database import SessionLocal
from models import Client
import sys

db = SessionLocal()

try:
    print("=" * 60)
    print("Checking Clients in Database")
    print("=" * 60)
    
    clients = db.query(Client).all()
    
    if not clients:
        print("\n⚠️  No clients found in database!")
        print("You need to register a new client first.")
    else:
        print(f"\nFound {len(clients)} client(s):\n")
        for client in clients:
            print(f"ID: {client.id}")
            print(f"Client ID: {client.client_id}")
            print(f"Email: {client.email}")
            print(f"Name: {client.name}")
            print(f"Active: {client.is_active}")
            print(f"Created: {client.created_at}")
            print("-" * 60)
    
    print("\n" + "=" * 60)
    
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
finally:
    db.close()
