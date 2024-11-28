
```markdown
# Image Captioning Project

## Overview

The Image Captioning Project utilizes pre-trained models from Hugging Face's Transformers library to automatically generate descriptive captions for images. It includes scripts for processing local images, a Gradio web app for interactive captioning, and an automated scraper to extract and caption images from web pages.

## Features

- **Local Image Captioning:** Generate captions for images in a specified directory.
- **Web Interface:** Interactive web app using Gradio for uploading images and viewing captions.
- **Automated Scraping:** Scrape images from Wikipedia pages and generate captions automatically.
- **Additional Tools:** Simple greeting app demonstrating Gradio integration.

## Installation

1. **Clone the Repository**
   ```sh
   git clone https://github.com/mustafaangi/image-captioning.git
   cd image-captioning
   ```

2. **Set Up Virtual Environment**
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Dependencies**
   ```sh
   pip install --upgrade pip
   pip install torch transformers pillow gradio beautifulsoup4 requests
   ```

4. **Authenticate with Hugging Face (If Required)**
   ```sh
   huggingface-cli login
   ```
   *Follow the prompts to enter your Hugging Face token.*

## Usage

### Local Image Captioning
Generate captions for images in the `image.cap` directory:
```sh
python3 loc_img_cap.py --image_dir /path/to/image.cap
```

### Web Interface
Launch the Gradio web app:
```sh
python3 image_captioning_app.py
```

### Automated Scraping
Scrape images from a Wikipedia page and generate captions:
```sh
python3 automate_url_captioner.py
```

### Greeting App
Run a simple greeting interface:
```sh
python3 hello.py
```

## Project Structure

```plaintext
image-captioning-project/
├── .venv/                     # Virtual environment
├── image.cap/                 # Directory with images
│   ├── cat.jpeg
│   ├── cat2.jpeg
│   └── cat3.jpeg
├── loc_img_cap.py             # Caption local images
├── image_captioning_app.py    # Gradio web app
├── image_cap.py               # Generate caption for a single image
├── automate_url_captioner.py  # Scrape and caption images from URL
├── hello.py                   # Simple Gradio greeting app
├── captions.txt               # Generated captions
├── README.md                  # Project documentation

```

## Acknowledgments

- [Hugging Face](https://huggingface.co/) for the Transformers library
- [Salesforce BLIP](https://huggingface.co/Salesforce/blip-image-captioning-base) for the image captioning model
- [Gradio](https://gradio.app/) for the web interface

   
