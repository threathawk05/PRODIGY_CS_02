from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    # Open the image and convert it to RGB if it's not
    image = Image.open(input_path).convert("RGB")
    # Convert image data to a NumPy array
    data = np.array(image)
    
    # Apply XOR operation with the key on each pixel
    encrypted_data = data ^ key  # XOR each pixel with the key
    encrypted_image = Image.fromarray(encrypted_data, "RGB")
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(input_path, output_path, key):
    # Decrypt by repeating the same XOR operation
    encrypt_image(input_path, output_path, key)
    print(f"Image decrypted and saved as {output_path}")

# Paths to input and output images and encryption key
input_path = "input_image.jpg"  # Path to the original image
encrypted_path = "encrypted_image.png"
decrypted_path = "decrypted_image.png"
key = 123  # Key must be an integer for XOR

# Encrypt the image
encrypt_image(input_path, encrypted_path, key)

# Decrypt the image
decrypt_image(encrypted_path, decrypted_path, key)
