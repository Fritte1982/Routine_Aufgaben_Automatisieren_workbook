import requests, bs4
from settings.paths_attributes import PROJECT_STUFF

html_in = PROJECT_STUFF / "example.html"

exampleFile = open(html_in, "r")
example_soup = bs4.BeautifulSoup(exampleFile, features="html.parser")
print(type(example_soup))
print(example_soup.select('#author')[0].attrs)