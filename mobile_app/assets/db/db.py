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

# Insert initial data
restaurants_data = [
    ("The Fancy Fork", "A delightful fusion of flavors and elegance.", "Downtown", "assets/images/rest1.jpg"),
    ("Burger Bliss", "Juicy burgers with a heavenly twist.", "Midtown", "assets/images/rest2.jpg"),
    ("Sushi Symphony", "Orchestrating the finest sushi experience.", "Uptown", "assets/images/rest3.jpg"),
    ("Pasta Paradise", "Where every bite feels like an Italian vacation.", "City Center", "assets/images/rest4.jpg"),
    ("Taco Haven", "Bold spices wrapped in warm tortillas.", "East Side", "assets/images/rest5.jpg"),
    ("The Green Bowl", "Fresh and healthy salads for every mood.", "West Side", "assets/images/rest6.jpg"),
    ("BBQ Junction", "Smoky, tender, and saucy barbecue treats.", "Old Town", "assets/images/rest7.jpg"),
    ("Mediterranean Marvels", "Authentic Mediterranean cuisine with a modern twist.", "Seafront", "assets/images/rest8.jpg"),
    ("The Dessert Den", "Sweet treats and desserts to brighten your day.", "Midtown", "assets/images/rest9.jpg"),
    ("Curry Chronicles", "A journey through the rich flavors of Indian curries.", "South Side", "assets/images/rest10.jpg"),
    ("Noodle Nirvana", "Wok-tossed noodles with vibrant flavors.", "Downtown", "assets/images/rest11.jpg"),
    ("Steakhouse Royal", "Prime cuts of beef cooked to perfection.", "North End", "assets/images/rest12.jpg"),
    ("The Vegan Loft", "Plant-based dishes that satisfy every craving.", "East End", "assets/images/rest13.jpg"),
    ("Pizza Perfection", "A variety of gourmet pizzas made fresh daily.", "City Square", "assets/images/rest14.jpg"),
    ("Dim Sum Dynasty", "Steamed and fried dim sum for every taste.", "Chinatown", "assets/images/rest15.jpg"),
    ("Ramen Retreat", "Slurp-worthy ramen bowls packed with umami.", "Little Tokyo", "assets/images/rest16.jpg"),
    ("Soul Food Spot", "Comforting Southern classics made with love.", "South East", "assets/images/rest17.jpg"),
    ("Sizzle Steakhouse", "Sizzling plates of juicy steaks and gourmet sides.", "Suburbs", "assets/images/rest18.jpg"),
    ("The Smoothie Shack", "Refreshing, nutrient-packed smoothies and bowls.", "Oceanview", "assets/images/rest19.jpg"),
    ("Bakery Bliss", "Freshly baked pastries and bread made from scratch.", "Downtown", "assets/images/rest20.jpg"),
    ("The Seafood Bar", "Fresh seafood served with a side of coastal charm.", "Marina", "assets/images/rest21.jpg"),
    ("Brunch Bonanza", "The best brunch in town, served all day.", "Riverfront", "assets/images/rest22.jpg"),
    ("Fusion Feast", "Bold fusion cuisine that surprises and delights.", "Hollywood", "assets/images/rest23.jpg"),
    ("Bistro Breeze", "A cozy spot for French bistro-style dishes.", "Park Lane", "assets/images/rest24.jpg"),
    ("Sizzling Sushi", "Innovative sushi rolls served with style.", "Bay Area", "assets/images/rest25.jpg"),
    ("Churrasco Charms", "Brazilian-style grilled meats served to perfection.", "Beach Road", "assets/images/rest26.jpg"),
    ("Spice Street", "A vibrant mix of exotic spices in every dish.", "Cultural District", "assets/images/rest27.jpg"),
    ("Steamed Heaven", "Dim sum and steamed buns in a cozy atmosphere.", "Waterfront", "assets/images/rest28.jpg"),
    ("Fried Fables", "Crispy and golden fried food that brings joy.", "Industrial Park", "assets/images/rest29.jpg"),
    ("Noodles & More", "All your noodle favorites, plus hearty sides.", "Downtown", "assets/images/rest30.jpg")
]

# Insert initial data for dishes
dishes_data = [
    ("Truffle Delight", 1, "An exquisite pasta infused with truffle essence.", "assets/images/dish1.jpg"),
    ("Heavenly Cheeseburger", 2, "A burger that melts in your mouth with every bite.", "assets/images/dish2.jpg"),
    ("Dragon Roll Supreme", 3, "A sushi masterpiece with a fiery finish.", "assets/images/dish3.jpg"),
    ("Tuscan Sunrise", 4, "Classic spaghetti with sun-dried tomatoes and basil.", "assets/images/dish4.jpg"),
    ("Fiery Fiesta Tacos", 5, "Tacos bursting with bold and zesty flavors.", "assets/images/dish5.jpg"),
    ("Kale Bliss Salad", 6, "A nutritious bowl of kale, quinoa, and citrus dressing.", "assets/images/dish6.jpg"),
    ("Smoky Ribs Platter", 7, "Tender ribs slathered in a house-made smoky sauce.", "assets/images/dish7.jpg"),
    ("Falafel Dream Wrap", 8, "Crispy falafel in a soft pita with tahini drizzle.", "assets/images/dish8.jpg"),
    ("Chocolate Avalanche", 9, "A decadent dessert with layers of chocolate goodness.", "assets/images/dish9.jpg"),
    ("Butter Chicken Bowl", 10, "Creamy butter chicken served with fragrant basmati rice.", "assets/images/dish10.jpg"),
    ("Sizzling Tofu Stir-Fry", 11, "A mix of veggies and tofu in a savory stir-fry.", "assets/images/dish11.jpg"),
    ("Lobster Mac & Cheese", 12, "Luxurious lobster paired with creamy mac and cheese.", "assets/images/dish12.jpg"),
    ("Veggie Power Bowl", 13, "A nourishing mix of roasted veggies and grains.", "assets/images/dish13.jpg"),
    ("Classic Margherita Pizza", 14, "Fresh mozzarella, basil, and tomato on a thin crust.", "assets/images/dish14.jpg"),
    ("Dim Sum Feast", 15, "A selection of steamed and fried dim sum options.", "assets/images/dish15.jpg"),
    ("Miso Ramen", 16, "A rich, umami-packed ramen bowl with miso broth.", "assets/images/dish16.jpg"),
    ("Chicken & Waffles", 17, "Golden crispy chicken with fluffy waffles and syrup.", "assets/images/dish17.jpg"),
    ("BBQ Brisket Plate", 18, "Tender brisket served with smoky barbecue sauce.", "assets/images/dish18.jpg"),
    ("Tropical Smoothie Bowl", 19, "A smoothie bowl topped with fresh fruit and granola.", "assets/images/dish19.jpg"),
    ("Cinnamon Roll Frenzy", 20, "Warm, gooey cinnamon rolls with cream cheese icing.", "assets/images/dish20.jpg"),
    ("Shrimp Scampi Pasta", 21, "Garlic butter shrimp tossed with linguine.", "assets/images/dish21.jpg"),
    ("Lamb Kofta Skewers", 22, "Spiced lamb skewers served with yogurt sauce.", "assets/images/dish22.jpg"),
    ("Eggplant Parmesan", 23, "Crispy breaded eggplant smothered in marinara and cheese.", "assets/images/dish23.jpg"),
    ("Baked Salmon Fillet", 24, "Perfectly baked salmon with a lemon butter glaze.", "assets/images/dish24.jpg"),
    ("Pavlova Perfection", 25, "A light, airy meringue dessert topped with whipped cream and fruit.", "assets/images/dish25.jpg"),
    ("Chicken Shawarma Wrap", 26, "Spiced chicken wrapped in pita with fresh veggies.", "assets/images/dish26.jpg"),
    ("Beef Wellington", 27, "Tender beef wrapped in puff pastry with mushrooms.", "assets/images/dish27.jpg"),
    ("Coconut Curry Soup", 28, "A creamy coconut-based soup with exotic spices.", "assets/images/dish28.jpg"),
    ("Vegetarian Paella", 29, "A vibrant Spanish rice dish with mixed vegetables.", "assets/images/dish29.jpg"),
    ("Peking Duck", 30, "Crispy duck served with pancakes and hoisin sauce.", "assets/images/dish30.jpg")
]

cursor.executemany("INSERT INTO dishes (name, restaurant_id, description, img) VALUES (?, ?, ?, ?)", dishes_data)

cursor.executemany("INSERT INTO restaurants (name, description, location, img) VALUES (?, ?, ?, ?)", restaurants_data)

# Commit and close the connection
connection.commit()
connection.close()

db_file_name
