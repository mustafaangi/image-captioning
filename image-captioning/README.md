# Image Captioning Project

## Description

This project generates descriptive captions for images located in a specified directory using Hugging Face's `transformers` library and the `Blip2` image captioning model. Captions are saved to a `captions.txt` file.

## Features

- Supports image formats: `.jpg`, `.jpeg`, `.png`.
- Utilizes the `Blip2` model for high-quality image captions.
- Outputs captions in a structured text file for easy reference.

## Requirements

- Python 3.9 or higher
- Virtual Environment (recommended)

## Setup

### 1. Clone the Repository


git clone https://github.com/yourusername/image-captioning-project.git
cd image-captioning-project


2. Create and Activate a Virtual Environment
It's recommended to use a virtual environment to manage dependencies.

python3 -m venv .venv
source .venv/bin/activate

3. Install Dependencies
Note: Ensure you have PyTorch installed correctly. You might need to follow specific instructions based on your system and whether you have a CUDA-compatible GPU.

pip install --upgrade pip
pip install torch transformers pillow

4. Authenticate with Hugging Face (If Required)
Some models may require authentication. If prompted, log in using:

huggingface-cli login

Follow the instructions to enter your Hugging Face token, which you can obtain from Hugging Face Tokens.

Usage
Prepare Images

Place the images you want to caption in the image.cap directory:

/image.cap
  ├── cat.jpeg
  ├── cat2.jpeg
  └── cat3.jpeg

Run the Captioning Script
Ensure your virtual environment is activated.

python3 loc_img_cap.py

View Captions

cat.jpeg: A small kitten sitting on a tiled floor.
cat2.jpeg: A small orange cat sitting on a white background.
cat3.jpeg: A small kitten standing on a wooden floor.

After running the script, captions will be saved in captions.txt:

Troubleshooting
Dependency Conflicts

If you encounter issues related to Pillow versions, ensure compatibility:

pip uninstall pillow
pip install "pillow<11.0,>=8.0"

Module Not Found Errors

If you receive errors about missing modules like transformers or torch, ensure they're installed within your virtual environment:

pip install transformers torch

Authentication Issues

If accessing certain models requires authentication, ensure you've logged in with:

huggingface-cli login

Shape Mismatch Errors

Ensure you're using compatible model and processor pairs. Consider using smaller models if running on limited hardware resources.

SSL Warnings

Warnings about LibreSSL vs. OpenSSL indicate that your SSL library is outdated. While these are usually warnings and may not prevent the script from running, it's recommended to update your SSL libraries to avoid potential security issues.

brew install openssl


Then, consider reinstalling Python to link against the updated OpenSSL.

Project Structure

image-captioning-project/
├── .venv/                 # Virtual environment directory
├── image.cap/             # Directory containing images to caption
│   ├── cat.jpeg
│   ├── cat2.jpeg
│   └── cat3.jpeg
├── loc_img_cap.py         # Main script for generating image captions
├── captions.txt           # Output file with generated captions
└── README.md              # Project documentation


Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

Acknowledgments
Hugging Face for the powerful transformers library.
Salesforce BLIP for the image captioning model.
PyTorch for the deep learning framework.
