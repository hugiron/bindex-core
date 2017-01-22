import json
import string
import random
import requests as rqst
from pendex.api.instagram.model.account import Account
from pendex.api.instagram.model.media import Media
from pendex.api.instagram.model.comment import Comment
from pendex.api.instagram.endpoint import *
from pendex.model.exceptions import InstagramException, InstagramNotFoundException


def get_account_by_username(username):
    try:
        response = rqst.get(get_account_json_info_link_by_username(username=username))
        return Account.create_from_account_page(response=json.loads(response.text).get('user'))
    except Exception:
        return Account.empty()


def get_account_by_id(id):
    try:
        response = get_api_request(get_account_json_info_link_by_account_id(user_id=id))
        return Account.create_from_account_page(response=response.text)
    except Exception:
        return Account.empty()


def get_medias(username, count):
    try:
        index = 0
        medias = []
        max_id = ''
        is_more_available = True
        while index < count and is_more_available:
            response = rqst.get(get_account_medias_json_link(username=username, max_id=max_id))
            if response.status_code != 200:
                raise InstagramException('Response code is not equal 200. Something went wrong. Please report issue.')
            data = json.loads(response.text)
            if not data.get('items'):
                return medias
            for item in data.get('items'):
                if index == count:
                    return medias
                index += 1
                media = Media.create_from_api(item)
                medias.append(media)
                max_id = media.id
            is_more_available = data.get('more_available')
        return medias
    except Exception:
        return Media.empty()


def get_media_by_url(url):
    try:
        if url and url[-1] != '/':
            url += '/'
        response = rqst.get('{0}?__a=1'.format(url))
        if response.status_code == 404:
            raise InstagramNotFoundException('Account with given username does not exist.')
        if response.status_code != 200:
            raise InstagramException('Response code is not equal 200. Something went wrong. Please report issue.')
        return Media.create_from_media_page(response=json.loads(response.text).get('media'))
    except Exception:
        return Media.empty()


def get_media_by_code(code):
    return get_media_by_url(get_media_page_link_by_code(code=code))


def get_location_medias_by_id(facebook_location_id, quantity):
    try:
        index = 0
        medias = []
        offset = ''
        has_next = True
        while index < quantity and has_next:
            response = rqst.get(get_medias_json_by_location_id_link(facebook_location_id=facebook_location_id,
                                                                    max_id=offset))
            if response.status_code != 200:
                raise InstagramException('Response code is not equal 200. Something went wrong. Please report issue.')
            data = json.loads(response.text)
            if not (data.get('location') and data.get('location').get('media') and
                        data.get('location').get('media').get('nodes')):
                return medias
            for node in data.get('location').get('media').get('nodes'):
                if index == quantity:
                    return medias
                index += 1
                media = Media.create_from_tag_page(response=node)
                medias.append(media)
            has_next = data.get('location').get('media').get('page_info').get('has_next_page')
            offset = data.get('location').get('media').get('page_info').get('end_cursor')
        return medias
    except Exception:
        return []


def get_comments_by_media_code(code, count):
    try:
        index = 0
        comments = []
        comment_id = '0'
        has_next = True
        while index < count and has_next:
            response = get_api_request(get_comments_before_comment_id_by_code(code=code,
                                                                              count=count,
                                                                              comment_id=comment_id))
            if response.status_code != 200:
                raise InstagramException('Response code is not equal 200. Something went wrong. Please report issue.')
            data = json.loads(response.text)
            if not data.get('comments'):
                return comments
            for node in data.get('comments').get('nodes'):
                if index == count:
                    return comments
                index += 1
                comment = Comment.create_from_api(response=node)
                comments.append(comment)
            has_next = data.get('comments').get('page_info').get('has_previous_page')
            comment_id = data.get('comments').get('page_info').get('start_cursor')
        return comments
    except Exception:
        return []


def generate_random_string(size, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def get_api_request(params):
    csrf = generate_random_string(10)
    form = {'q': params}
    headers = {
        'Cookie': 'csrftoken=%s;' % csrf,
        'X-Csrftoken': csrf,
        'Referer': 'https://www.instagram.com/'
    }
    return rqst.post(
        url=INSTAGRAM_QUERY_URL,
        data=form,
        headers=headers
    )
