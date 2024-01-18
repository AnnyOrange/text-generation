import os
import hashlib
from PIL import Image

def process_images(input_folder, output_folder):
    # Iterate through each subfolder (1-11)
    for subfolder_name in os.listdir(input_folder):
        subfolder_path = os.path.join(input_folder, subfolder_name)
        if os.path.isdir(subfolder_path):
            process_subfolder(subfolder_path, output_folder)

def process_subfolder(subfolder_path, output_folder):
    # Load init_image and style_image from the subfolder
    init_image_path = os.path.join(subfolder_path, "init_image.jpg")  # Update the file extension if needed
    style_image_path = os.path.join(subfolder_path, "style_image.jpg")  # Update the file extension if needed

    # Create a hash for the images
    hash_value = hash_images(init_image_path, style_image_path)

    # Create a directory using the hash value
    output_dir = os.path.join(output_folder, hash_value)
    os.makedirs(output_dir, exist_ok=True)

    # Save original and cartoonized images in the output directory
    save_image(init_image_path, os.path.join(output_dir, "original_image.png"))
    save_image(style_image_path, os.path.join(output_dir, "cartoonized_image.png"))

def hash_images(*image_paths):
    # Compute a hash value based on the content of the images
    hash_object = hashlib.sha1()
    for image_path in image_paths:
        with open(image_path, "rb") as f:
            hash_object.update(f.read())
    return hash_object.hexdigest()

def save_image(input_path, output_path):
    # Convert image format if needed and save
    image = Image.open(input_path)
    image.convert("RGB").save(output_path)

if __name__ == "__main__":
    input_folder = r"D:\AI\text-re\text-generation\data_preparation\Text-style-dataset"
    output_folder = r"cartoonizer-dataset"

    process_images(input_folder, output_folder)
