#!/usr/bin/env python3
import subprocess
import sys

# First, try to install Pillow if not available
try:
    from PIL import Image, ImageChops
except ImportError:
    print("Installing Pillow...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow", "-q"])
    from PIL import Image, ImageChops

# Open and trim the image
try:
    img = Image.open('SA.png').convert('RGB')
    # Find the bounding box of non-white pixels
    bbox = ImageChops.difference(img, Image.new('RGB', img.size, 'white')).getbbox()
    
    if bbox:
        trimmed_img = img.crop(bbox)
        trimmed_img.save('SA.png')
        print("✓ Image trimmed successfully!")
    else:
        print("No white space found to trim.")
except Exception as e:
    print(f"Error: {e}")
