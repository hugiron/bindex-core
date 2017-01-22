import requests as rqst
from bs4 import BeautifulSoup, SoupStrainer
from bindex.api.vk import VkApi


def get(user_ids, fields, name_case='nom', access_token=None):
    if list != type(user_ids):
        user_ids = [user_ids]
    data = dict(
        v=VkApi.get_version(),
        user_ids=','.join(map(str, user_ids)),
        fields=','.join(fields),
        name_case=name_case
    )
    if access_token:
        data['access_token'] = access_token
    return VkApi.request('users.get', data)


def get_phones(user_id):
    info_strainer = SoupStrainer(attrs={'class': 'profile_info_cont'})
    if str(user_id).isdigit():
        user_id = 'id{0}'.format(user_id)
    headers = {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
    }
    user_info = rqst.get('https://m.vk.com/{0}'.format(user_id), headers=headers).text
    parser = BeautifulSoup(user_info, 'html.parser', parse_only=info_strainer)
    return [phone.text for phone in parser.findAll(attrs={'class': 'si_phone'})]


def get_permissions(access_token):
    data = dict(access_token=access_token)
    return VkApi.request('account.getAppPermissions', data)
