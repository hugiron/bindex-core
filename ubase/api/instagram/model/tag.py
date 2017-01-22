import json


class Tag:
    def __init__(self):
        pass

    @staticmethod
    def create_by_search_page(response):
        tag = Tag()
        if type(response) == dict:
            data = response
        else:
            data = json.loads(response)
        tag.media_count = data.get('media_count')
        tag.name = data.get('name')
        tag.id = data.get('id')
        return tag
