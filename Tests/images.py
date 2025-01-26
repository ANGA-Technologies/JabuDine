import os
import requests
from urllib.parse import urlparse

# Function to download and rename images
def download_and_rename_images(image_urls, save_directory, name_format="rest_{index}.jpg"):
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)  # Create directory if it doesn't exist
    
    for index, url in enumerate(image_urls, start=6):
        try:
            # Extract the image from the URL
            response = requests.get(url)
            if response.status_code == 200:
                # Parse the URL to get the image name
                parsed_url = urlparse(url)
                filename = os.path.basename(parsed_url.path)
                
                # Define the new file name with the format (e.g., "restaurant_1.jpg")
                new_filename = name_format.format(index=index)
                
                # Define the full path to save the file
                file_path = os.path.join(save_directory, new_filename)
                
                # Write the image content to the file
                with open(file_path, 'wb') as file:
                    file.write(response.content)
                
                print(f"Image {new_filename} downloaded and saved to {file_path}")
            else:
                print(f"Failed to download image from {url}")
        except Exception as e:
            print(f"Error downloading image from {url}: {e}")

# List of image URLs (replace these with the actual URLs of restaurant images)
image_urls = [
    "https://example.com/restaurant1.jpg",
    "https://example.com/restaurant2.jpg",
    "https://example.com/restaurant3.jpg",
    "https://example.com/restaurant4.jpg",
    "https://example.com/restaurant5.jpg"
]

# Directory to save the downloaded images
save_directory = "assets\images"

# Download and rename images
download_and_rename_images(image_urls, save_directory)
