import json
import time
import random
import requests as rqst
from pendex.model.exceptions import MethodApiException, RequestLimitException


class FbApi:
    @staticmethod
    def get_base_uri():
        return 'https://graph.facebook.com/v2.6'

    @staticmethod
    def request(method, params, access_token=None, get_request=False):
        if access_token:
            params['access_token'] = access_token
        if not get_request:
            response = json.loads(rqst.post(
                url='{0}/{1}'.format(FbApi.get_base_uri(), method),
                data=params
            ).text)
        else:
            response = json.loads(rqst.get(
                url='{0}/{1}'.format(FbApi.get_base_uri(), method),
                params=params
            ).text)
        if 'error' in response:
            if response['error']['code'] == 17:
                time.sleep(3 * random.random())
                return FbApi.request(
                    method=method,
                    params=params,
                    access_token=access_token,
                    get_request=get_request
                )
                #raise RequestLimitException(message=response['error']['message'])
            raise MethodApiException(
                code=response['error']['code'],
                message=response['error']['message']
            )
        return response
