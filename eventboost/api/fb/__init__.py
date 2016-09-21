import json
import requests as rqst
from eventboost.model.exceptions import MethodApiException


class FbApi:
    @staticmethod
    def get_base_uri():
        return 'https://graph.facebook.com/v2.6'

    @staticmethod
    def request(method, params, access_token=None):
        if access_token:
            params['access_token'] = access_token
        response = json.loads(rqst.post(
            url='{0}/{1}'.format(FbApi.get_base_uri(), method),
            data=params
        ).text)
        if 'error' in response:
            raise MethodApiException(
                code=response['error']['code'],
                message=response['error']['message']
            )
        return response
