import requests as rqst
from bs4 import BeautifulSoup


def get_author(uri):
    parser = BeautifulSoup(rqst.get(uri).text, 'html.parser')
    for item in parser.find(attrs=dict(name='description'))['content'].split(' '):
        if item and item[:1] == '@':
            return item[1:]
    return None
