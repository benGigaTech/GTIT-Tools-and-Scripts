from pyzbar.pyzbar import decode
from PIL import Image

def extract_urls_from_qr_code(image_path):
  """
  Extracts URLs from a QR code image.
  Args:
      image_path: The path to the image file containing the QR code.
  Returns:
      A list of extracted URLs.
  """
  try:
      img = Image.open(image_path)
      # Decode the QR code
      decoded_data = decode(img)
      # Extract URLs from the decoded data.
      urls = []
      for data in decoded_data:
          if data.type == 'QRCODE': # Check for QR code type.
              urls.append(data.data.decode('utf-8')) # Decode the byte data to string.
      return urls

  except Exception as e:
      print(f"An Error Has Occurred: {e}")
      return []

if __name__ == "__main__":
  image_path = input("Enter the path to the image file: ").strip('"') # strips quotation marks from paths given that include spaces.
  extracted_urls = extract_urls_from_qr_code(image_path)

  if extracted_urls:
    #outputs the Extracted URLs to the console.
      print("Extracted URLs:")
      for url in extracted_urls:
          print(url)
    #Else return
  else:
      print("No URLs found in the QR code.")
