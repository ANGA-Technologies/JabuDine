import sqlite3
import os
import random

# Get the directory where the current script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the database file name within the same directory
db_file_name = os.path.join(script_dir, "jabudine.db")

# Connect to SQLite database
connection = sqlite3.connect(db_file_name)
cursor = connection.cursor()

# Function to check if a column exists in a table
def column_exists(table_name, column_name):
    cursor.execute(f"PRAGMA table_info({table_name})")
    return any(row[1] == column_name for row in cursor.fetchall())

# Add rating column if not already present
if not column_exists("restaurants", "rating"):
    cursor.execute("ALTER TABLE restaurants ADD COLUMN rating INTEGER DEFAULT 0")

if not column_exists("dishes", "rating"):
    cursor.execute("ALTER TABLE dishes ADD COLUMN rating INTEGER DEFAULT 0")

# Assign random ratings (between 1 and 5) to all rows in the restaurants table
cursor.execute("SELECT id FROM restaurants")
restaurant_ids = [row[0] for row in cursor.fetchall()]

for restaurant_id in restaurant_ids:
    random_rating = random.randint(1, 5)
    cursor.execute("UPDATE restaurants SET rating = ? WHERE id = ?", (random_rating, restaurant_id))

# Commit changes and close connection
connection.commit()
connection.close()

print("Tables updated successfully with rating column, and random ratings assigned to restaurants.")
