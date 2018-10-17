import requests
from bs4 import BeautifulSoup

# Get the website that contains classes.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple_classes.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Get the first inner paragraph.
# Find all the paragraph tags with the class inner-text.
# Then, take the first element in that list.
first_inner_paragraph = parser.find_all("p", class_="inner-text")[0]
print(first_inner_paragraph.text)

second_inner_paragraph = parser.find_all('p', class_= 'inner-text')[1]
second_inner_paragraph_text = second_inner_paragraph.text

first_outer_paragraph = parser.find_all('p', class_ = 'outer-text')[0]
first_outer_paragraph_text = first_outer_paragraph.text

# Perhaps a better solution

inner_paragraphs = parser.find_all('p', class_='inner-text')
outer_paragraphs = parser.find_all('p', class_='outer-text')

# Having the paragraphs in a list by class, I can just index rather than redo the find_all search



#Classes and IDs
# Get the website that contains classes and IDs.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Select all of the elements that have the first-item class.
first_items = parser.select(".first-item")

# Print the text of the first paragraph (the first element with the first-item class).
print(first_items[0].text)

outer_text = parser.find_all('p', class_='outer-text')
first_outer_text = outer_text[0].text
second = parser.find_all('p', id = 'second')
second_text = second[0].texts