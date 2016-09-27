from mongoengine import Q
from eventboost.model.token import Token
from eventboost.token.network import token_handler
from eventboost.model.exceptions import RequestLimitException


def get_access_token(network, permissions=[]):
    result = None
    try:
        handler = token_handler[network]
        while not result:
            try:
                token = Token.objects(Q(network=network) &
                                      Q(data__permissions__exists=True) &
                                      Q(data__permissions__all=permissions))\
                    .aggregate([{'$sample': {'size': 1}}])
                if not token:
                    break
                if handler.is_active(token.get_data()):
                    result = token.get_data()
                else:
                    token.delete()
            except RequestLimitException as limit_exception:
                pass
            except:
                break
    except:
        pass
    return result


def set_access_token(network, data):
    try:
        if Token.objects(Q(network=network) & Q(data__access_token=data['access_token'])).first():
            raise Exception('This token already exists')
        Token.create(
            network=network,
            data=data
        ).save()
        return True
    except:
        return False
