import os
import glob
from transformers import pipeline

# Suppress specific warnings (optional)
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

# Initialize the image captioning pipeline with the correct task
print("Initializing image captioning pipeline...")
captioner = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
print("Pipeline initialized.")

# Directory setup
image_dir = "/Users/mustafaangi/Desktop/image.cap"
image_exts = ["jpg", "jpeg", "png"]

# Process images and generate captions
with open("captions.txt", "w") as caption_file:
    for image_ext in image_exts:
        for img_path in glob.glob(os.path.join(image_dir, f"*.{image_ext}")):
            try:
                print(f"Processing image: {img_path}")
                
                # Generate caption
                caption = captioner(img_path)[0]['generated_text']
                
                print(f"Caption: {caption}")
                caption_file.write(f"{os.path.basename(img_path)}: {caption}\n")
                
            except Exception as e:
                print(f"Error processing {img_path}: {str(e)}")
                continue