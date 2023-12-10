from PIL import Image
import os

def resize_images_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".png"):
            file_path = os.path.join(folder_path, filename)

            with Image.open(file_path) as img:
                # Calculate the new width maintaining the aspect ratio
                aspect_ratio = img.width / img.height
                new_height = 50
                new_width = int(aspect_ratio * new_height)

                # Resize the image
                resized_img = img.resize((new_width, new_height))

                # Save the resized image back to the folder
                resized_img.save(file_path)

                print(f"Resized {filename}")

folder_path = '.'  # Replace with the path to your folder
resize_images_in_folder(folder_path)
