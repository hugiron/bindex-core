import re
import requests as rqst
from bs4 import BeautifulSoup
from pendex.api.twitter import TwitterApi


def get_profile_card(username):
    if not username:
        return None
    return str(BeautifulSoup(rqst.get('{0}/{1}'.format(TwitterApi.get_base_uri(), username)).text, 'html.parser').find(
        attrs={'class': 'ProfileHeaderCard'}
    ))


def get_user_id_by_screen_name(username):
    if not username:
        return None
    id = re.findall(pattern="data-user-id=\"(\d+)\"",
                    string=rqst.get('{0}/{1}'.format(TwitterApi.get_base_uri(), username)).text)
    return id[0] if id else None


def get_screen_name_by_user_id(user_id):
    if not user_id:
        return None
    username = re.findall(pattern="id=\"twitter-([^\"]+)\"",
                          string=rqst.get('{0}/intent/user?user_id={1}'.format(TwitterApi.get_base_uri(), user_id)).text)
    return username[0] if username else None
