import os
import urllib.request

# Function to download a file from a URL
def download_file(url, dest):
    dest_dir = os.path.dirname(dest)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir, exist_ok=True)

    try:
        print(f"Downloading from {url} to {dest}...")
        urllib.request.urlretrieve(url, dest)
    except Exception as e:
        print(f"An error occurred: {e}")

# Piemērs, lai lejupielādētu pirmo atrasto .pdf failu

url = 'https://va.lv/'
dest = 'C:/Users/Janis/Downloads/va.pdf'

download_file(url, dest)

# Output: An error occured: HTTP Error 403: Forbidden
        