"""
This script scrapes images from a specified Wikipedia page, generates captions for each image using a pretrained model, 
and writes the captions to a file.

Modules:
    requests: To make HTTP requests to download web pages and images.
    PIL (Pillow): To handle image processing.
    io: To handle byte streams.
    bs4 (BeautifulSoup): To parse HTML and extract image elements.
    transformers: To load the pretrained image captioning model and processor.

Functions:
    None

Usage:
    Run the script to download images from the specified Wikipedia page, generate captions, and save them to 'captions.txt'.

Workflow:
    1. Load the pretrained processor and model for image captioning.
    2. Download the specified Wikipedia page.
    3. Parse the page to find all image elements.
    4. For each image element:
        a. Extract the image URL.
        b. Skip SVG images and very small images.
        c. Correct malformed URLs.
        d. Download the image.
        e. Convert the image data to a PIL Image.
        f. Process the image and generate a caption using the model.
        g. Write the image URL and caption to 'captions.txt'.
"""
import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
from transformers import AutoProcessor, BlipForConditionalGeneration

# Load the pretrained processor and model
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# URL of the page to scrape
url = "URL of wanted page"

# Download the page
response = requests.get(url)
# Parse the page with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all img elements
img_elements = soup.find_all('img')

# Open a file to write the captions
with open("captions.txt", "w") as caption_file:
    # Iterate over each img element
    for img_element in img_elements:
        img_url = img_element.get('src')

        # Skip if the image is an SVG or too small (likely an icon)
        if 'svg' in img_url or '1x1' in img_url:
            continue

        # Correct the URL if it's malformed
        if img_url.startswith('//'):
            img_url = 'https:' + img_url
        elif not img_url.startswith('http://') and not img_url.startswith('https://'):
            continue  # Skip URLs that don't start with http:// or https://

        try:
            # Download the image
            response = requests.get(img_url)
            # Convert the image data to a PIL Image
            raw_image = Image.open(BytesIO(response.content))
            if raw_image.size[0] * raw_image.size[1] < 400:  # Skip very small images
                continue

            raw_image = raw_image.convert('RGB')

            # Process the image
            inputs = processor(raw_image, return_tensors="pt")
            # Generate a caption for the image
            out = model.generate(**inputs, max_new_tokens=50)
            # Decode the generated tokens to text
            caption = processor.decode(out[0], skip_special_tokens=True)

            # Write the caption to the file, prepended by the image URL
            caption_file.write(f"{img_url}: {caption}\n")
        except Exception as e:
            print(f"Error processing image {img_url}: {e}")
            continue