import re
import requests as rqst
from bs4 import BeautifulSoup
from eventboost.api.fb import FbApi


def get_user_id(username):
    parser = BeautifulSoup(rqst.get('https://facebook.com/{0}'.format(username)).text, 'html.parser')
    data = re.findall('fb://profile/([\\d]+)', parser.find(attrs=dict(property='al:android:url'))['content'])
    return data[0] if data else None


def get_user_info(user_id, fields, access_token):
    return FbApi.request(
        method=user_id,
        params=dict(
            fields=','.join(fields)
        ),
        access_token=access_token
    )


def get_permissions(access_token):
    return FbApi.request(
        method='me/permissions',
        params=dict(),
        access_token=access_token,
        get_request=True
    )['data']
