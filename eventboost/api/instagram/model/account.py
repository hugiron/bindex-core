import json


class Account:
    def __init__(self):
        pass

    @staticmethod
    def empty():
        account = Account()
        account.id = None
        account.username = None
        account.follows_count = 0
        account.followed_by_count = 0
        account.media_count = 0
        account.profile_pic_url = None
        account.biography = ''
        account.full_name = ''
        account.is_private = False
        account.external_url = ''
        account.is_verified = False
        return account

    @staticmethod
    def create_from_account_page(response):
        account = Account()
        if type(response) == dict:
            data = response
        else:
            data = json.loads(response)
        account.id = data.get('id')
        account.username = data.get('username')
        account.follows_count = data.get('follows').get('count')
        account.followed_by_count = data.get('followed_by').get('count')
        account.media_count = data.get('media').get('count')
        account.profile_pic_url = data.get('profile_pic_url')
        account.biography = data.get('biography')
        account.full_name = data.get('full_name')
        account.is_private = data.get('is_private')
        account.external_url = data.get('external_url')
        account.is_verified = data.get('is_verified')
        return account

    @staticmethod
    def create_from_media_page(response):
        account = Account()
        if type(response) == dict:
            data = response
        else:
            data = json.loads(response)
        account.id = data.get('id')
        account.username = data.get('username')
        account.profile_pic_url = data.get('profile_pic_url')
        account.full_name = data.get('full_name')
        account.is_private = data.get('is_private')
        return account
