"""
Query all clients from the database to verify data is being stored
"""
from database import SessionLocal
from models import Client
from datetime import datetime

def query_all_clients():
    """Display all registered clients from the database"""
    db = SessionLocal()
    
    try:
        print("=" * 80)
        print("📊 QUERYING DATABASE: clients TABLE")
        print("=" * 80)
        
        # Query all clients
        clients = db.query(Client).all()
        
        if not clients:
            print("\n⚠️  No clients found in database.")
            print("Register a client first using the frontend or Postman!")
            return
        
        print(f"\n✅ Found {len(clients)} client(s) in database:\n")
        
        for i, client in enumerate(clients, 1):
            print(f"{'=' * 80}")
            print(f"CLIENT #{i}")
            print(f"{'=' * 80}")
            print(f"ID (Database):     {client.id}")
            print(f"CLIENT ID:         {client.client_id}")
            print(f"CLIENT KEY HASH:   {client.client_key_hash[:50]}...")
            print(f"EMAIL:             {client.email}")
            print(f"NAME:              {client.name}")
            print(f"IS ACTIVE:         {client.is_active}")
            print(f"CREATED AT:        {client.created_at}")
            print()
        
        print("=" * 80)
        print("🔐 SECURITY NOTE:")
        print("=" * 80)
        print("✅ Client keys are HASHED with bcrypt (not stored in plain text)")
        print("✅ Original client_key is shown ONLY ONCE during registration")
        print("✅ Database stores only the bcrypt hash for security")
        print("=" * 80)
        
        # Show raw SQL query
        print("\n📝 SQL QUERY EXECUTED:")
        print("-" * 80)
        print("SELECT * FROM clients;")
        print("-" * 80)
        
    except Exception as e:
        print(f"\n❌ Error querying database: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    query_all_clients()
