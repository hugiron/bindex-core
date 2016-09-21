from eventboost.api.vk import VkApi


def get(owner_id, domain, offset, count, filter, fields, extended=0, access_token=None):
    data = dict(
        owner_id=owner_id,
        domain=domain,
        offset=offset,
        count=count,
        filter=filter,
        fields=fields,
        extended=extended
    )
    if access_token:
        data['access_token'] = access_token
    return VkApi.request('wall.get', data)
