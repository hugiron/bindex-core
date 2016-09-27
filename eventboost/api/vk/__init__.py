import json
import requests as rqst
from eventboost.model.exceptions import MethodApiException, RequestLimitException


class VkApi:
    @staticmethod
    def get_base_uri():
        return 'https://api.vk.com/method'

    @staticmethod
    def get_version():
        return 5.53

    @staticmethod
    def request(method, params, access_token=None, v=None):
        if access_token:
            params['access_token'] = access_token
        params['v'] = v if v else VkApi.get_version()
        response = json.loads(rqst.post(
            url='{0}/{1}'.format(VkApi.get_base_uri(), method),
            data=params
        ).text)
        if 'error' in response:
            if response['error']['error_code'] == 6:
                raise RequestLimitException(message=response['error']['error_msg'])
            raise MethodApiException(
                code=response['error']['error_code'],
                message=response['error']['error_msg']
            )
        return response['response']

    @staticmethod
    def execute(code, params, access_token, v=None):
        params['access_token'] = access_token
        params['code'] = code
        params['v'] = v if v else VkApi.get_version()
        response = json.loads(rqst.post(
            url='{0}/execute'.format(VkApi.get_base_uri()),
            data=params
        ).text)
        if 'error' in response:
            raise MethodApiException(
                code=response['error']['error_code'],
                message=response['error']['error_msg']
            )
        return response['response']

    @staticmethod
    def get_permissions():
        return [
            (1, 'notify'),
            (2, 'friends'),
            (4, 'photos'),
            (8, 'audio'),
            (16, 'video'),
            (131072, 'docs'),
            (2048, 'notes'),
            (128, 'pages'),
            (1024, 'status'),
            (32, 'offers'),
            (64, 'questions'),
            (8192, 'wall'),
            (262144, 'groups'),
            (4096, 'messages'),
            (4194304, 'email'),
            (524288, 'notifications'),
            (1048576, 'stats'),
            (32768, 'ads'),
            (134217728, 'market'),
            (65536, 'offline')
        ]
