# First make sure you install the following packages via terminal:
# pip install requests
# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

# Get the HTML content of the wikipedia page using requests
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
response = requests.get(url)
html = response.content
print(f"HTML content: {html}")

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
print(f"Title of the page: {soup.title}")
