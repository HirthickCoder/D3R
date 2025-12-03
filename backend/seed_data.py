# seed_data.py - Script to add initial menu items to the database
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, MenuItem

# Create tables
Base.metadata.create_all(bind=engine)

def seed_menu_items():
    db = SessionLocal()
    
    try:
        # Check if data already exists
        existing_count = db.query(MenuItem).count()
        if existing_count > 0:
            print(f"Database already has {existing_count} menu items. Skipping seed.")
            return
        
        # Sample menu items
        menu_items = [
            MenuItem(
                name="Margherita Pizza",
                description="Fresh tomatoes, mozzarella, and basil",
                price=299,
                category="pizza",
                image="/images/pizza.jpg",
                popular=True
            ),
            MenuItem(
                name="Pasta Carbonara",
                description="Creamy pasta with pancetta and parmesan",
                price=249,
                category="pasta",
                image="/images/carbo.jpg",
                popular=True
            ),
            MenuItem(
                name="Chocolate Lava Cake",
                description="Warm chocolate cake with a molten center",
                price=179,
                category="dessert",
                image="/images/lavas.jpg",
                popular=True
            ),
            MenuItem(
                name="Caesar Salad",
                description="Fresh romaine lettuce with Caesar dressing",
                price=199,
                category="salad",
                image="/images/salad.jpg",
                popular=False
            ),
            MenuItem(
                name="Grilled Salmon",
                description="Fresh salmon with lemon butter sauce",
                price=399,
                category="main",
                image="/images/salmon.jpg",
                popular=False
            ),
            MenuItem(
                name="Mojito",
                description="Refreshing mint and lime cocktail",
                price=149,
                category="drinks",
                image="/images/mojito.jpg",
                popular=True
            ),
            MenuItem(
                name="Classic Burger",
                description="Juicy beef patty with fresh vegetables",
                price=189,
                category="main",
                image="/images/burger.jpg",
                popular=False
            ),
            MenuItem(
                name="Veggie Burger",
                description="Plant-based patty with fresh vegetables",
                price=169,
                category="main",
                image="/images/burger.jpg",
                popular=False
            ),
        ]
        
        # Add all items to database
        for item in menu_items:
            db.add(item)
        
        db.commit()
        print(f"✅ Successfully added {len(menu_items)} menu items to the database!")
        
        # Display added items
        print("\nAdded menu items:")
        for item in menu_items:
            print(f"  - {item.name} (₹{item.price}) - {item.category}")
            
    except Exception as e:
        print(f"❌ Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    print("🌱 Seeding database with menu items...")
    seed_menu_items()
