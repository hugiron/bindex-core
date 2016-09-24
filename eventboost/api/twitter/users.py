import requests as rqst
from bs4 import BeautifulSoup
from eventboost.api.twitter import TwitterApi


def get_profile_card(username):
    return str(BeautifulSoup(rqst.get('{0}/{1}'.format(TwitterApi.get_base_uri(), username)).text, 'html.parser').find(
        attrs={'class': 'ProfileHeaderCard'}
    ))
