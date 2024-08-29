# GTIT-Tools-and-Scripts
A repository for general purpose scripts, tools, etc. That I write to make my job a little bit easier.



## Scripts
#### **[QR Decoder](QRDecoder/QRDecoder.py)**
  - A quick script that takes an image as an input, decodes and contained QR codes, and outputs any contained URLs to the console.
  - `-df` or `--defang` flags will return defanged URLs. **Example:** `hxxps[://]example[.]com/alink/to/somethingbad`
  - Usage: `python QRDecoder.py "C:\path\to\your\image.png"
  - Usage w/ Flags: `python QRDecoder.py "C:\path\to\your\image.png" -df` or `python QRDecoder.py "C:\path\to\your\image.png" --defang`
