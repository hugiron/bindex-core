from io import StringIO
import re
import requests as rqst
from bs4 import BeautifulSoup
from eventboost.api.instagram import InstagramApi


def get_author(uri):
    parser = BeautifulSoup(rqst.get(uri).text, 'html.parser')
    try:
        for item in parser.find(attrs=dict(name='description'))['content'].split(' '):
            if item and item[:1] == '@':
                return item[1:]
    except:
        pass
    return None


def get_status(username):
    parser = BeautifulSoup(rqst.get('{0}/{1}'.format(InstagramApi.get_base_uri(), username)).text, 'html.parser')
    buffer = StringIO()
    try:
        buffer.write(parser.find(attrs=dict(name='description'))['content'])
        for item in parser.findAll('script'):
            for res in re.findall(InstagramApi.get_pattern_uri_in_status(), str(item)):
                buffer.write(' ')
                buffer.write(res)
    except:
        pass
    return buffer.getvalue()
