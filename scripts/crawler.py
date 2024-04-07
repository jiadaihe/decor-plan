from pathlib import Path
from bs4 import BeautifulSoup
import scrapy
import requests


# def parse(url: str):

headers = dict({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    # "Accept-Encoding": "gzip, deflate",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    # "Accept-Language": "en-US,en;q=0.5",
    # "User-Agent": "3"
})

r = requests.get(
    "https://www.westelm.com/products/solstice-coffee-table-h9127/?pkey=csolstice-collection",
    headers=headers)
# get request headers
print(r.request.headers)
soup = BeautifulSoup(r.content, "lxml")
print(soup.prettify())
