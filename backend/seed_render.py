# Run this script to seed your Render database with menu items
# Make sure you have the DATABASE_URL from Render

import os
from seed_data import seed_menu_items

if __name__ == "__main__":
    # The DATABASE_URL will be loaded from your .env file or environment
    print("🌱 Seeding Render database with menu items...")
    print("📍 Using DATABASE_URL from environment")
    seed_menu_items()
