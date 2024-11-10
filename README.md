# Image Encryption Tool

A simple image encryption and decryption tool that uses pixel manipulation by applying an XOR operation with a specified key. This tool is created using Python and the Pillow library.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Example](#example)

## Overview

This tool allows users to encrypt and decrypt images by performing an XOR operation on each pixel’s RGB values. It’s a basic approach to image encryption, mainly for learning and experimentation.

## Features

- Encrypts an image by applying XOR with a key to each pixel.
- Decrypts an encrypted image using the same key.
- Works with most common image formats (PNG, JPEG, BMP).

## Requirements

- **Python 3.x**
- **Pillow**: A Python imaging library
- **NumPy**: A package for numerical operations in Python

Install the required libraries with:

```bash
pip install pillow numpy
```

## Usage


1. Clone the Repository:

```bash
  git clone https://github.com/username/image-encryption-tool.git
cd image-encryption-tool


```

2. Place Your Image in the Same Directory

- Place the image you want to encrypt in the same directory as the Python file and name it, for example, input_image.png. You can also use any other image name but ensure you update the code accordingly.

3. Run the Script

```bash
  python image_encrpyt.py

```

 This will generate two new files:

- encrypted_image.png: The encrypted version of the original image.
- decrypted_image.png: The decrypted image, which should look like the original.

4. Code Example
Here’s an example snippet of how to use the tool:

```bash
  from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    image = Image.open(input_path).convert("RGB")
    data = np.array(image)
    encrypted_data = data ^ key
    encrypted_image = Image.fromarray(encrypted_data, "RGB")
    encrypted_image.save(output_path)

def decrypt_image(input_path, output_path, key):
    encrypt_image(input_path, output_path, key)

input_path = "input_image.png"
encrypted_path = "encrypted_image.png"
decrypted_path = "decrypted_image.png"
key = 123

encrypt_image(input_path, encrypted_path, key)
decrypt_image(encrypted_path, decrypted_path, key)

```


## How it Works

1. Image Loading: The script loads the image and converts it to RGB format.

2. Pixel Manipulation: Each pixel’s RGB value is XORed with a specified key. This operation scrambles the color values, creating an encrypted image.

3. Decryption: The XOR operation is applied again with the same key, reversing the encryption and restoring the original pixel values.













## Example

Here’s an example flow for a single pixel:

1. Original Pixel: (100, 150, 200)
Key: 123

2. Encrypted Pixel: Each color channel is XORed with the key, resulting in a new color.

3. Decryption: Applying XOR again with the same key restores the original values.


## Notes

- This tool is meant for educational purposes and is not secure for sensitive data encryption.
- For high-resolution images, encryption and decryption may take longer.
