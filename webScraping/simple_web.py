import requests
from bs4 import BeautifulSoup

# Get some test data to work with
response = requests.get('http://dataquestio.github.io/web-scraping-pages/simple.html')
content = response.content

# Initialize the parser, and passin the content we're working with
parser = BeautifulSoup(content, 'html.parser')

# Get the body tag from the document.
# Since we passed in the top level of the document to the parser, we need to pick a branch off of the root.
# With BeautifulSoup, we can access branches by using tag types as attributes.
body = parser.body

# Get the p tag from the body.
p = body.p

# Print the text inside the p tag
print(p)

# Get the title tag from the body.
head = parser.head
title = head.title
title_text = title.text

# Print the title text.
print(title_text)

# Get a list of all occurances of head in the element
head = parser.find_all('head')

# Get the title tag
title = head[0].find_all('title')

# Because this is a list of title elements, the title is the first element
title_text = title[0].text
