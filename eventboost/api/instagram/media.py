import re
from bs4 import BeautifulSoup, SoupStrainer
from eventboost.api.instagram.method import *


def get_author(uri):
    try:
        media = get_media_by_url(url=uri)
        return media.owner.id
    except:
        pass
    return None


def get_status(username):
    try:
        user = get_account_by_username(username=username)
        return '{0} {1} {2}'.format(user.full_name,
                                    user.biography,
                                    user.external_url)
    except:
        return ''


def get_notes(source_code):
    wall_strainer = SoupStrainer(attrs={'id': 'page_wall_posts'})
    parser = BeautifulSoup(source_code, 'html.parser', parse_only=wall_strainer)
    regex = re.compile("instagram\.com/[\d\w_/-]+")
    result = list()
    for post in parser.findAll(attrs={'class': 'post_date'}):
        result.extend(regex.findall(str(post)))
    return result
