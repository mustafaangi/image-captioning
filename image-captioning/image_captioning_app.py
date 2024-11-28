from PIL import Image
import gradio as gr
import numpy as np
from transformers import AutoProcessor, BlipForConditionalGeneration

# Load the pretrained processor and model
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def caption_image(input_image: np.ndarray, max_length: int = 50):
    """
    Parameters:
    input_image (np.ndarray): The input image in numpy array format.
    max_length (int): The maximum length of the generated caption. Default is 50.

    Returns:
    str: The generated caption for the image.
    """
    
    # Convert numpy array to PIL Image and convert to RGB
    raw_image = Image.fromarray(input_image).convert('RGB')

    # Process the image
    inputs = processor(raw_image, return_tensors="pt")

    # Generate a caption for the image
    out = model.generate(**inputs, max_length=max_length)
    
    # Decode the generated tokens to text
    caption = processor.decode(out[0], skip_special_tokens=True)

    return caption
    fn=caption_image, 
    inputs=gr.Image(), 
    outputs="text",
    title="Image Captioning",
    description="This is a simple web app for generating captions for images using a trained model."
)
    description="This web app generates descriptive captions for images using a pretrained model. Upload an image, and the app will process it to generate a meaningful caption."
iface.launch()