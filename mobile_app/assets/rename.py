import os

# Function to rename and save images from a source folder to a target folder
def rename_and_save_images(source_directory, target_directory, name_format="rest{index}.jpg"):
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)  # Create target directory if it doesn't exist
    
    # List all files in the source directory
    files = os.listdir(source_directory)
    
    # Filter out non-image files (optional: customize extensions if needed)
    image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    
    for index, image_file in enumerate(image_files, start=6):
        try:
            # Define the new file name with the format (e.g., "rest_1.jpg")
            new_filename = name_format.format(index=index)
            
            # Define full paths for the source and target
            source_path = os.path.join(source_directory, image_file)
            target_path = os.path.join(target_directory, new_filename)
            
            # Rename and move the file to the target directory
            os.rename(source_path, target_path)
            
            print(f"Image '{image_file}' renamed to '{new_filename}' and saved to '{target_directory}'")
        except Exception as e:
            print(f"Error processing image '{image_file}': {e}")

script_dir = os.path.dirname(os.path.abspath(__file__))

# Source directory containing the images
source_directory = os.path.join(script_dir, "raw")

# Target directory to save renamed images
target_directory = os.path.join(script_dir, "images")

# Rename and save images
rename_and_save_images(source_directory, target_directory)
