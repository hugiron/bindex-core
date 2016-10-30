from mongoengine import Q
from eventboost.model.token import Token
from eventboost.token.network import token_handler
from eventboost.model.exceptions import RequestLimitException


def get_access_token(server, network, permissions=[]):
    result = None
    handler = token_handler[network]
    query = Q(server=server) & Q(network=network)
    if permissions:
        query &= Q(permissions__all=permissions)
    while not result:
        try:
            token = Token.objects(query).aggregate(*[{'$sample': {'size': 1}}])
            if not token.alive:
                break
            token = token.next()
            if handler.is_active(token['data']):
                result = token['data']
            else:
                Token.objects(Q(id=token['_id'])).delete()
        except RequestLimitException as limit_exception:
            pass
    return result


def set_access_token(network, data, server, metadata):
    try:
        if Token.objects(Q(network=network) & Q(data__access_token=data['access_token'])).first():
            raise Exception('This token already exists')
        Token.create(
            network=network,
            data=data,
            server=server,
            metadata=metadata
        ).save()
        return True
    except:
        return False
