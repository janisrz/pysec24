# pip install requests
# pip install numpy
# pip install beautifulsoup4

import requests # Importē requests moduli
import numpy as np # Importē numpy moduli
from bs4 import BeautifulSoup # Importē BeautifulSoup klasi no bs4 moduļa

url = 'https://va.lv/' # URL
response = requests.get(url) # GET request
html_content = response.content # HTML content

soup = BeautifulSoup(html_content, 'html.parser') # BeautifulSoup parses the HTML content
title = soup.title.string # Extracts the title of the webpage
print(f"Title: {title}") # Output: Title: ViA

heading = soup.find('h1').string # Extracts the first h1 tag
print(f"Heading: {heading}") # Output: KURŠ AUGS TU ESI?

paragraph = soup.find('p').text if soup.find('p') else 'No paragraph found' # Extracts all p tags
print(f"Paragraph: {paragraph}") # Output: Paragraph: Tests, kas palīdzēs studiju virziena izvēlē

anchor = soup.find('a')['href'] if soup.find('a') else 'No anchor tag found' # Extracts the href attribute of the first a tag
print(f"URL: {anchor}") # Output: URL: /lapas-karte?view=html&id=1