import os
from PIL import Image

def optimize_images():
    image_dir = 'Images'
    
    # Original total size
    original_size = 0
    new_size = 0
    
    for i in range(1, 9):
        ext = 'png' if i in [1, 4] else 'jpg'
        filename = f'galerie{i}.{ext}'
        path = os.path.join(image_dir, filename)
        
        if not os.path.exists(path):
            print(f"File not found: {path}")
            continue
            
        orig_sz = os.path.getsize(path)
        original_size += orig_sz
        
        # Open and process
        with Image.open(path) as img:
            # Convert to RGB if needed (for saving as WebP from PNG with potential alpha)
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
                
            # Resize if width > 800
            if img.width > 800:
                ratio = 800.0 / img.width
                new_height = int(img.height * ratio)
                img = img.resize((800, new_height), Image.Resampling.LANCZOS)
                
            # Save as WebP
            out_path = os.path.join(image_dir, f'galerie{i}.webp')
            img.save(out_path, 'WEBP', quality=80, method=4)
            
            n_sz = os.path.getsize(out_path)
            new_size += n_sz
            
            print(f"{filename}: {orig_sz/1024:.1f} KB -> galerie{i}.webp: {n_sz/1024:.1f} KB")

    print(f"\nOptimization complete!")
    print(f"Total Original Size: {original_size/1024/1024:.2f} MB")
    print(f"Total New Size: {new_size/1024/1024:.2f} MB")
    print(f"Saved: {(original_size - new_size)/1024/1024:.2f} MB ({(original_size - new_size)/original_size*100:.1f}%)")

if __name__ == '__main__':
    optimize_images()
