from eventboost.api.vk import VkApi


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


def get_permissions(access_token):
    data = dict(access_token=access_token)
    return VkApi.request('account.getAppPermissions', data)
