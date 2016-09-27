from mongoengine import Document, ListField, DictField, StringField
from eventboost.token.network import *


class Token(Document):
    network = StringField()
    permissions = ListField()
    data = DictField()
    meta = {
        'collection': 'tokens',
        'indexes': [
            {
                'fields': ['network', 'permissions']
            }
        ]
    }

    @staticmethod
    def create(network, data):
        handler = token_handler[network]
        result = Token()
        if handler.is_active(data):
            result.set_permissions(handler.get_permissions(data))
            result.set_data(data)
            result.set_network(network)
            return result
        return None

    def get_permissions(self):
        return self.permissions

    def set_permissions(self, permissions):
        self.permissions = permissions

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_network(self):
        return self.network

    def set_network(self, network):
        self.network = network
