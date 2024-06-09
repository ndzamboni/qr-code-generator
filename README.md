# Dynamic QR Code Generator

This is a simple Python script that generates QR codes from user-provided URLs and saves them as image files. The script uses the `qrcode` and `Pillow` libraries to create and manipulate QR code images.

## Features

- Generates QR codes for any URL.
- Allows user to specify the file name for the generated QR code image.
- Saves the QR code image as a PNG file in a dedicated `qrcodes` folder.

## Prerequisites

Make sure you have Python installed on your system. This script is compatible with Python 3.x.

## Installation

1. Clone the repository or download the script file.
2. Install the required Python libraries using pip:

    ```sh
    pip install qrcode[pil]
    ```

## Usage

1. Run the script:

    ```sh
    python qr_generator.py
    ```

2. When prompted, enter the website URL you want to encode in the QR code.
3. Enter the desired file name for the QR code image (e.g., `my_qr_code.png`).

The script will generate the QR code and save it in the `qrcodes` folder.

## Example

```sh
Enter the website URL: https://www.example.com
Enter the name of the file to save the QR code (e.g., qr_code.png): example_qr_code.png
QR code saved as qrcodes/example_qr_code.png
