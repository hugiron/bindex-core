import json
from ubase.api.instagram.model.account import Account


class Comment:
    def __init__(self):
        pass

    @staticmethod
    def create_from_api(response):
        comment = Comment()
        if type(response) == dict:
            data = response
        else:
            data = json.loads(response)
        comment.text = data.get('text')
        comment.created_at = int(data.get('created_at'))
        comment.id = data.get('id')
        comment.user = Account.create_from_account_page(data.get('user'))
        return comment
