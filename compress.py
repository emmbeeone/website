import os
from PIL import Image

image_dir = "images-pdfs-docs"

images_to_compress = [
    "Website-Head-Banner-image.png",
    "Classroom-image.png",
    "students-image.jpg"
]

for img_name in images_to_compress:
    img_path = os.path.join(image_dir, img_name)
    if os.path.exists(img_path):
        try:
            with Image.open(img_path) as img:
                # Convert to RGB if necessary before saving as WebP
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")
                    
                # Calculate new size if image is too large (max width 1920)
                max_width = 1920
                if img.width > max_width:
                    ratio = max_width / img.width
                    new_height = int(img.height * ratio)
                    img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
                
                # Save as webp with high compression
                new_img_name = os.path.splitext(img_name)[0] + ".webp"
                new_img_path = os.path.join(image_dir, new_img_name)
                
                # Save optimized
                img.save(new_img_path, "webp", quality=80, optimize=True)
                
                # Optionally, overwrite the original extension if you want to keep references simple, but let's just make new files.
                print(f"Compressed {img_name} -> {new_img_name}")
        except Exception as e:
            print(f"Error compressing {img_name}: {e}")
