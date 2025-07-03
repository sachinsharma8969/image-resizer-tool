import os

from PIL import Image

#Configuration

input_folder = 'input_images'      # Folder with original images

output_folder = 'resized_images'   # Folder to save resized images

resize_to = (800, 600)             # Target size (width, height)

output_format = 'JPEG'             # Optional: 'JPEG', 'PNG', etc.

def resize_images(input_dir, output_dir, size, format=None):

    # Create output folder if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Loop through all files in the input folder
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
            try:
                img_path = os.path.join(input_dir, filename)
                img = Image.open(img_path)

                # Resize the image
                img = img.resize(size, Image.ANTIALIAS)

                # Prepare new filename and path
                base_name = os.path.splitext(filename)[0]
                new_ext = '.' + format.lower() if format else os.path.splitext(filename)[1]
                output_path = os.path.join(output_dir, base_name + new_ext)

                # Save resized image
                img.save(output_path, format=format if format else img.format)
                print(f"Resized and saved: {output_path}")

            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":

    resize_images(input_folder, output_folder, resize_to, format=output_format)