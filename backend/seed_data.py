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
        
        # Sample menu items matching your existing design
        menu_items = [
            MenuItem(
                name="Mushroom Dana",
                description="Exotic slices with flavoring a deep, like rich and tangy magic come alive when a hearty Mushroom Dana makes it a flavorful delight",
                price=9.99,
                category="Main Course",
                image="https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9?w=500",
                popular=True
            ),
            MenuItem(
                name="Cauliflower Rice",
                description="A dish worth savoring, a fluff light and fluffy cauliflower rice presented in the most adventurous way possible",
                price=11.99,
                category="Main Course",
                image="https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=500",
                popular=False
            ),
            MenuItem(
                name="Biryani",
                description="Spices Royale",
                price=12.99,
                category="Main Course",
                image="https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=500",
                popular=True
            ),
            MenuItem(
                name="Tiramisu",
                description="Classic Italian dessert with coffee-soaked ladyfingers and marscapone cream",
                price=7.99,
                category="Dessert",
                image="https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?w=500",
                popular=True
            ),
            MenuItem(
                name="Margherita Pizza",
                description="Fresh tomatoes, mozzarella, basil, and tomato base that bring out its exceptional taste",
                price=9.99,
                category="Pizza",
                image="https://images.unsplash.com/photo-1574071318508-1cdbab80d002?w=500",
                popular=False
            ),
            MenuItem(
                name="Pasta Carbonara",
                description="Creamy pasta with bacon, egg, and parmesan",
                price=10.99,
                category="Pasta",
                image="https://images.unsplash.com/photo-1612874742237-6526221588e3?w=500",
                popular=False
            ),
            MenuItem(
                name="Chocolate Lava Cake",
                description="Warm chocolate cake with molten center served with vanilla ice cream",
                price=6.99,
                category="Dessert",
                image="https://images.unsplash.com/photo-1624353365286-3f8d62daad51?w=500",
                popular=True
            ),
            MenuItem(
                name="Caesar Salad",
                description="Fresh romaine lettuce, croutons, and parmesan",
                price=8.99,
                category="Salad",
                image="https://images.unsplash.com/photo-1546793665-c74683f339c1?w=500",
                popular=False
            ),
            MenuItem(
                name="Punjabi Paneer Roll (veg)",
                description="The amalgam of various vegetable choices, Daytona Cream, Garlic - Rattle, Enhance, plated with masala Cheese ball",
                price=7.99,
                category="Main Course",
                image="https://images.unsplash.com/photo-1626074353765-517a681e40be?w=500",
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
