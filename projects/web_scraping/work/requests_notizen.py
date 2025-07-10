import requests
from icecream import ic

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
ic(res.status_code == requests.codes.OK)
print ( res.text)
res = requests.get('http://inventwithpython.com/page_that_does_not_exist') 
res.raise_for_status() 