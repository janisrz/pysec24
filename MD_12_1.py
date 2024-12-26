import requests
from bs4 import BeautifulSoup

url = 'https://va.lv/'
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')

title = soup.title.string if soup.title else 'No title found'
print(f"Title: {title}")

# Extract all headings (H1-H6)
headings = {}
for i in range(1, 7):
    tag = f'h{i}'
    headings[tag] = [heading.get_text() for heading in soup.find_all(tag)]
print("Headings:")
for tag, texts in headings.items():
    print(f"{tag}:")
    for text in texts:
        print(f"  {text}")

# Extract all paragraphs
paragraphs = [p.get_text() for p in soup.find_all('p')]
print("Paragraphs:")
for paragraph in paragraphs:
    print(f"  {paragraph}")

# Extract all links
links = [a['href'] for a in soup.find_all('a', href=True)]
print("Links:")
for link in links:
    print(f"  {link}")

# Extract all images
images = [img['src'] for img in soup.find_all('img', src=True)]
print("Images:")
for image in images:
    print(f"  {image}")

# Extract meta description
meta_description = soup.find('meta', attrs={'name': 'description'})
meta_content = meta_description['content'] if meta_description else 'No meta description found'
print(f"Meta Description: {meta_content}") # Output: Meta Description: No meta description found