import os

from PIL import Image

# === Configuration ===

input_folder = 'input_images'         # Folder with original images

output_folder = 'output_images'       # Folder to save resized images

new_size = (800, 600)                 # Desired size (width, height)

output_format = 'JPEG'               # Can be 'JPEG', 'PNG', etc.

# === Ensure output folder exists ===

os.makedirs(output_folder, exist_ok=True)

# === Process images ===

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        img_path = os.path.join(input_folder, filename)
        with Image.open(img_path) as img:
            img_resized = img.resize(new_size)
            base_name = os.path.splitext(filename)[0]
            output_path = os.path.join(output_folder, f"{base_name}.{output_format.lower()}")
            img_resized.save(output_path, output_format)
            print(f"Resized and saved: {output_path}")

print("✅ All images resized and saved.")

