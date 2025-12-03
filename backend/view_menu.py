#!/usr/bin/env python3
"""
Quick script to view all menu items in the database
"""
from sqlalchemy.orm import Session
from database import SessionLocal
from models import MenuItem

def view_all_menu_items():
    db = SessionLocal()
    
    try:
        items = db.query(MenuItem).all()
        
        if not items:
            print(" No menu items found in database!")
            print("\nRun 'python seed_data.py' to add sample data.")
            return
        
        print(f"\n{'='*80}")
        print(f"📋 MENU ITEMS IN DATABASE ({len(items)} items)")
        print(f"{'='*80}\n")
        
        for item in items:
            print(f"ID: {item.id}")
            print(f"Name: {item.name}")
            print(f"Description: {item.description}")
            print(f"Price: ₹{item.price}")
            print(f"Category: {item.category}")
            print(f"Popular: {'✓ Yes' if item.popular else '✗ No'}")
            print(f"Image: {item.image}")
            print(f"Created: {item.created_at}")
            print(f"{'-'*80}\n")
        
        # Summary by category
        categories = {}
        for item in items:
            cat = item.category
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(item.name)
        
        print(f"\n{'='*80}")
        print("📊 SUMMARY BY CATEGORY")
        print(f"{'='*80}\n")
        
        for cat, names in categories.items():
            print(f"{cat.upper()}: {len(names)} items")
            for name in names:
                print(f"  • {name}")
            print()
            
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    view_all_menu_items()
