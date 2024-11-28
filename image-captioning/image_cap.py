"""
This script generates a caption for a given image using a pretrained model from the Hugging Face Transformers library.

Modules:
    requests: To make HTTP requests.
    PIL.Image: To handle image processing.
    transformers.AutoProcessor: To preprocess the image and text.
    transformers.BlipForConditionalGeneration: To generate captions for the image.

Functions:
    None

Usage:
    1. Ensure you have the required libraries installed: requests, Pillow, transformers.
    2. Replace 'cat.jpeg' with the path to your image file.
    3. Run the script to generate and print a caption for the image.

Example:
    $ python image_cap.py

Attributes:
    processor (AutoProcessor): The processor for preprocessing the image and text.
    model (BlipForConditionalGeneration): The model for generating captions.
    img_path (str): The path to the image file.
    image (PIL.Image.Image): The loaded image in RGB format.
    text (str): The text prompt for the image captioning model.
    inputs (dict): The processed inputs for the model.
    outputs (torch.Tensor): The generated caption tokens.
    caption (str): The decoded caption text.
"""
import requests
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

# Load the pretrained processor and model
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Load your image, DONT FORGET TO WRITE YOUR IMAGE NAME
img_path = "cat.jpeg"
# convert it into an RGB format 
image = Image.open(img_path).convert('RGB')

# You do not need a question for image captioning
text = "the image of"
inputs = processor(images=image, text=text, return_tensors="pt")

# Generate a caption for the image
outputs = model.generate(**inputs, max_length=50)

# Decode the generated tokens to text
caption = processor.decode(outputs[0], skip_special_tokens=True)
# Print the caption
print(caption)

