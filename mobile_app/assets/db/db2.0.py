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
    # Fetch the list of valid restaurants from the database
    cursor.execute("SELECT id, name FROM restaurants")
    restaurants = cursor.fetchall()

    # Check if there are no restaurants in the database
    if not restaurants:
        print("No restaurants found! Please add a restaurant first.")
        return

    # Display the list of available restaurants
    print("Available restaurants:")
    for rest in restaurants:
        print(f"{rest[0]}: {rest[1]}")

    # Prompt the user for a restaurant ID and validate it
    try:
        restaurant_id = int(input("Enter the ID of the restaurant for the dish: "))
    except ValueError:
        print("Invalid input. Please enter a numeric ID.")
        return

    # Check if the restaurant ID exists in the database
    valid_restaurant_ids = [rest[0] for rest in restaurants]
    if restaurant_id not in valid_restaurant_ids:
        print("Invalid restaurant selected. Please choose a valid restaurant ID.")
        return

    # Prompt for dish details
    name = input("Enter dish name: ")
    description = input("Enter dish description: ")
    img = input("Enter dish image URL: ")

    # Display confirmation details to the user
    print("\nPlease confirm the details before adding the dish:")
    print(f"Restaurant ID: {restaurant_id}")
    print(f"Dish Name: {name}")
    print(f"Description: {description}")
    print(f"Image URL: {img}")
    
    confirmation = input("\nDo you want to proceed? (yes/no): ").strip().lower()
    if confirmation not in ['yes', 'y']:
        print("Dish addition canceled.")
        return

    # Insert the dish into the database
    try:
        cursor.execute(
            "INSERT INTO dishes (name, restaurant_id, description, img) VALUES (?, ?, ?, ?)",
            (name, restaurant_id, description, img)
        )
        print(f"Dish '{name}' added successfully!")
    except Exception as e:
        print(f"An error occurred while adding the dish: {e}")


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
