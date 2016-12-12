import re
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
    return re.findall("instagram\.com/[\d\w_/-]+", source_code)
