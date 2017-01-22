import json
from bindex.api.instagram.model.account import Account
from bindex.api.instagram.endpoint import *


INSTAGRAM_URL = "https://www.instagram.com/"
TYPE_IMAGE = "image"
TYPE_VIDEO = "video"


class Media:
    def __init__(self):
        pass

    @staticmethod
    def empty():
        media = Media()
        media.id = None
        media.type = TYPE_IMAGE
        media.created_time = 0
        media.code = ''
        media.link = '{0}p/{1}'.format(INSTAGRAM_URL, media.code)
        media.image_standard_resolution_url = ''
        media.caption = ''
        media.owner = Account.empty()
        return media

    @staticmethod
    def create_from_api(response):
        media = Media()
        if type(response) == dict:
            data = response
        else:
            data = json.loads(response)
        media.id = data.get('id')
        media.created_time = int(data.get('created_time'))
        media.type = data.get('type')
        media.link = data.get('link')
        media.code = data.get('code')
        if data.get('caption'):
            media.caption = data.get('caption').get('text')
        media.image_low_resolution_url = data.get('images').get('low_resolution').get('url')
        media.image_thumbnail_url = data.get('images').get('thumbnail').get('url')
        media.image_standard_resolution_url = data.get('images').get('standard_resolution').get('url')
        if media.type == TYPE_VIDEO:
            media.video_low_resolution_url = data.get('videos').get('low_resolution').get('url')
            media.video_standard_resolution_url = data.get('videos').get('standard_resolution').get('url')
            media.video_low_bandwidth_url = data.get('videos').get('low_bandwidth').get('url')
        return media

    @staticmethod
    def create_from_media_page(response):
        media = Media()
        if type(response) == dict:
            data = response
        else:
            data = json.loads(response)
        media.id = data.get('id')
        media.type = TYPE_IMAGE
        if data.get('is_video'):
            media.type = TYPE_VIDEO
            media.video_standard_resolution_url = data.get('video_url')
        media.created_time = int(data.get('date'))
        media.code = data.get('code')
        media.link = '{0}p/{1}'.format(INSTAGRAM_URL, media.code)
        media.image_standard_resolution_url = data.get('display_src')
        if data.get('caption'):
            media.caption = data.get('caption')
        media.owner = Account.create_from_media_page(data.get('owner'))
        return media

    @staticmethod
    def create_from_tag_page(response):
        media = Media()
        if type(response) == dict:
            data = response
        else:
            data = json.loads(response)
        media.code = data.get('code')
        media.link = get_media_page_link_by_code(code=media.code)
        media.comments_count = data.get('comments').get('count')
        media.likes_count = data.get('likes').get('count')
        media.owner_id = data.get('owner').get('id')
        if data.get('caption'):
            media.caption = data.get('caption')
        media.created_time = int(data.get('date'))
        media.image_thumbnail_url = data.get('thumbnail_src')
        media.image_standard_resolution_url = data.get('display_src')
        media.type = TYPE_IMAGE
        if data.get('is_video'):
            media.type = TYPE_VIDEO
            media.video_views = data.get('video_views')
        media.id = data.get('id')
        return media
