import sqlite3
import os

# Get the directory where the current script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the database file name within the same directory
db_file_name = os.path.join(script_dir, "jabudine.db")

# Connect to SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect(db_file_name)
cursor = connection.cursor()

# Create a table for storing restaurant information
cursor.execute('''
CREATE TABLE IF NOT EXISTS restaurants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    location TEXT NOT NULL,
    img TEXT NOT NULL
)
''')

# Create a table for storing dish information
cursor.execute('''
CREATE TABLE IF NOT EXISTS dishes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    restaurant_id INTEGER NOT NULL,
    description TEXT NOT NULL,
    img TEXT NOT NULL,
    FOREIGN KEY (restaurant_id) REFERENCES restaurants (id)
)
''')

# Function to add a new restaurant
def add_restaurant():
    name = input("Enter restaurant name: ")
    description = input("Enter restaurant description: ")
    location = input("Enter restaurant location: ")
    img = input("Enter restaurant image URL: ")
    cursor.execute(
        "INSERT INTO restaurants (name, description, location, img) VALUES (?, ?, ?, ?)",
        (name, description, location, img)
    )
    print(f"Restaurant '{name}' added successfully!")

# Function to add a new dish
def add_dish():
    cursor.execute("SELECT id, name FROM restaurants")
    restaurants = cursor.fetchall()

    if not restaurants:
        print("No restaurants found! Please add a restaurant first.")
        return

    print("Available restaurants:")
    for rest in restaurants:
        print(f"{rest[0]}: {rest[1]}")

    restaurant_id = int(input("Enter the ID of the restaurant for the dish: "))
    name = input("Enter dish name: ")
    description = input("Enter dish description: ")
    img = input("Enter dish image URL: ")
    cursor.execute(
        "INSERT INTO dishes (name, restaurant_id, description, img) VALUES (?, ?, ?, ?)",
        (name, restaurant_id, description, img)
    )
    print(f"Dish '{name}' added successfully!")

# Menu loop
def menu():
    while True:
        print("\n--- JabuDine Management System ---")
        print("1. Add a new restaurant")
        print("2. Add a new dish")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_restaurant()
        elif choice == "2":
            add_dish()
        elif choice == "3":
            break
        else:
            print("Invalid choice! Please try again.")

# Run the menu
menu()

# Commit and close the connection
connection.commit()
connection.close()
