import urllib.parse
import requests
from pendex.api.vk import VkApi


def get(owner_id, domain, offset, count, filter, fields, extended=0, access_token=None):
    data = dict(
        owner_id=owner_id,
        domain=domain,
        offset=offset,
        count=count,
        filter=filter,
        fields=','.join(fields),
        extended=extended
    )
    if access_token:
        data['access_token'] = access_token
    return VkApi.request('wall.get', data)


def get_source_code(owner_id):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/53.0.2785.116 YaBrowser/16.10.0.2309 Safari/537.36'
    }
    return urllib.parse.unquote(requests.get(url='https://vk.com/wall{0}?own=1'.format(owner_id),
                                             headers=headers).text)
