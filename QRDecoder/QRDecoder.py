import argparse
from pyzbar.pyzbar import decode
from PIL import Image

def extract_urls_from_qr_code(image_path, defang=False):
    """
    Extracts URLs from a QR code image and optionally defangs them.
    Args:
        image_path: The path to the image file containing the QR code.
        defang: A boolean flag indicating whether to defang the URLs.
    Returns:
        A list of extracted URLs, optionally defanged.
    """
    try:
        img = Image.open(image_path)
        # Decode the QR code
        decoded_data = decode(img)
        # Extract URLs from the decoded data.
        urls = []
        for data in decoded_data:
            if data.type == 'QRCODE': # Check for QR code type.
                url = data.data.decode('utf-8') # Decode the byte data to string.
                if defang:
                    url = url.replace('.', '[.]').replace('http', 'hxxp')  # Basic defanging
                urls.append(url)

        return urls

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract URLs from a QR code image.")
    parser.add_argument("image_path", help="Path to the image file containing the QR code") # strips quotation marks from paths given that include spaces.
    parser.add_argument("-df", "--defang", action="store_true", default=False, help="Defang the extracted URLs") 
    args = parser.parse_args()

    extracted_urls = extract_urls_from_qr_code(args.image_path, args.defang)

    if extracted_urls:
        print("Extracted URLs:")
        #outputs the Extracted URLs to the console.
        for url in extracted_urls:
            print(url)
            # else return
    else:
        print("No URLs found in the QR code.")
