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
    location TEXT NOT NULL
    img TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS dishes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    restaurant_id INTEGER NOT NULL,
    description TEXT NOT NULL,
    FOREIGN KEY (restaurant_id) REFERENCES restaurants (id)
    img TEXT NOT NULL
)
''')

# Insert initial data
restaurants_data = [
    ("The Fancy Fork", "A delightful fusion of flavors and elegance.", "Downtown", "assets/images/rest1.jpg"),
    ("Burger Bliss", "Juicy burgers with a heavenly twist.", "Midtown", "assets/images/rest2.jpg"),
    ("Sushi Symphony", "Orchestrating the finest sushi experience.", "Uptown", "assets/images/rest3.jpg"),
    ("Pasta Paradise", "Where every bite feels like an Italian vacation.", "City Center", "assets/images/rest4.jpg"),
    ("Taco Haven", "Bold spices wrapped in warm tortillas.", "East Side", "assets/images/rest5.jpg")
]

# Insert initial data for dishes
dishes_data = [
    ("Truffle Delight", 1, "An exquisite pasta infused with truffle essence.", "assets/images/dish1.jpg"),
    ("Heavenly Cheeseburger", 2, "A burger that melts in your mouth with every bite.", "assets/images/dish2.jpg"),
    ("Dragon Roll Supreme", 3, "A sushi masterpiece with a fiery finish.", "assets/images/dish3.jpg"),
    ("Tuscan Sunrise", 4, "Classic spaghetti with sun-dried tomatoes and basil.", "assets/images/dish4.jpg"),
    ("Fiery Fiesta Tacos", 5, "Tacos bursting with bold and zesty flavors.", "assets/images/dish5.jpg")
]

cursor.executemany("INSERT INTO dishes (name, restaurant_id, description) VALUES (?, ?, ?)", dishes_data)

cursor.executemany("INSERT INTO restaurants (name, description, location) VALUES (?, ?, ?)", restaurants_data)

# Commit and close the connection
connection.commit()
connection.close()

db_file_name
