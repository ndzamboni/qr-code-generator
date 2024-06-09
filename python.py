import os
import qrcode
from PIL import Image

def generate_qr_code(data, file_name):
    # Create a directory named 'qrcodes' if it doesn't exist
    os.makedirs('qrcodes', exist_ok=True)
    
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # controls the error correction used for the QR Code
        box_size=10,  # controls how many pixels each “box” of the QR code is
        border=4,  # controls how many boxes thick the border should be (the default is 4)
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Construct the full file path
    file_path = os.path.join('qrcodes', file_name)
    
    # Save the image
    img.save(file_path)
    print(f"QR code saved as {file_path}")

# Get user input
data = input("Enter the website URL: ")
file_name = input("Enter the name of the file to save the QR code (e.g., qr_code.png): ")

generate_qr_code(data, file_name)
