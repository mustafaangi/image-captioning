"""
This script processes images in a specified directory and generates captions for them using a pre-trained image captioning model from the Hugging Face Transformers library. The generated captions are saved to a text file.
Modules:
    os: Provides a way of using operating system dependent functionality.
    glob: Finds all the pathnames matching a specified pattern according to the rules used by the Unix shell.
    transformers: Provides state-of-the-art machine learning models for natural language processing tasks.
    transformers: Provides state-of-the-art machine learning models for natural language processing tasks.
    warnings: Provides a way to handle warnings in the code.
Functions:
    None
Variables:
    image_dir (str): The directory containing the images to be processed.
    image_exts (list): A list of image file extensions to look for in the directory.
    captioner (pipeline): The image captioning pipeline initialized with the specified model.
    caption_file (file object): The file object for writing the generated captions.
Usage:
    Run the script to process images in the specified directory and generate captions for them. The captions will be saved to a file named 'captions.txt' in the current working directory.
"""
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

import argparse

# Configuration section
image_exts = ["jpg", "jpeg", "png"]

# Alternatively, you can pass image_exts as an argument to a function
def process_images(image_dir, image_exts):
    captions = []
    for image_ext in image_exts:
        for img_path in glob.glob(os.path.join(image_dir, f"*.{image_ext}")):
            try:
                print(f"Processing image: {img_path}")
                
                # Generate caption
                caption = captioner(img_path)[0]['generated_text']
                
                print(f"Caption: {caption}")
                captions.append(f"{os.path.basename(img_path)}: {caption}\n")
                
            except Exception as e:
                print(f"Error processing {img_path}: {str(e)}")
                continue

    with open("captions.txt", "w") as caption_file:
        caption_file.writelines(captions)
                    print(f"Caption: {caption}")
                    caption_file.write(f"{os.path.basename(img_path)}: {caption}\n")
                else:
                    print(f"No caption generated for {img_path}")
# Call the function with the directory and image extensions
process_images(image_dir, image_exts)
parser = argparse.ArgumentParser(description="Process images and generate captions.")
parser.add_argument("image_dir", type=str, help="The directory containing the images to be processed.")
args = parser.parse_args()

image_dir = args.image_dir
image_dir = "PATH_TO_IMAGE_DIRECTORY"
image_exts = ["jpg", "jpeg", "png"]

# Process images and generate captions
with open("captions.txt", "w") as caption_file:
    for image_ext in image_exts:
        for img_path in glob.glob(os.path.join(image_dir, f"*.{image_ext}")):
            try:
                print(f"Processing image: {img_path}")
                
                # Generate caption
                caption = captioner(img_path)[0]['generated_text']
                
            except Exception as e:
                print(f"Error processing {img_path}: {type(e).__name__}: {str(e)}")
                continue
            except Exception as e:
                print(f"Error processing {img_path}: {str(e)}")
                continue