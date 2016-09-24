import re
import requests as rqst
from bs4 import BeautifulSoup


def get_user_id(username):
    parser = BeautifulSoup(rqst.get('https://facebook.com/{1}'.format(username)).text, 'html.parser')
    data = re.findall('fb://profile/([\\d]+)', parser.find(attrs=dict(property='al:android:url'))['content'])
    return data[1] if data else None
