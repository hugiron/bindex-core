import eventboost.api.vk.users as VkUsers
from eventboost.api.vk import VkApi
import eventboost.api.fb.users as FbUsers
from eventboost.model.exceptions import MethodApiException


class VkToken:
    @staticmethod
    def get_permissions(data):
        user_permissions = VkUsers.get_permissions(access_token=data['access_token'])
        return [item[1] for item in VkApi.get_permissions() if (user_permissions & item[0]) != 0]

    @staticmethod
    def is_active(data):
        try:
            VkUsers.get(
                user_ids='',
                fields=[],
                access_token=data['access_token']
            )
        except MethodApiException as api_exception:
            if api_exception.code == 5:
                return False
            raise api_exception
        return True


class FbToken:
    @staticmethod
    def get_permissions(data):
        permissions = FbUsers.get_permissions(access_token=data['access_token'])
        return [item['permission'].lower() for item in permissions if item['status'] == 'granted']

    @staticmethod
    def is_active(data):
        try:
            FbUsers.get_user_info(
                user_id='me',
                fields=[],
                access_token=data['access_token']
            )
        except MethodApiException as api_exception:
            if api_exception.code == 190:
                return False
            raise api_exception
        return True


token_handler = dict(
    vk=VkToken,
    fb=FbToken
)
