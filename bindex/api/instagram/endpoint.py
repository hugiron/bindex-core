BASE_URL = "https://www.instagram.com"
ACCOUNT_PAGE = "https://www.instagram.com/{{username}}"
MEDIA_LINK = "https://www.instagram.com/p/{{code}}"
ACCOUNT_MEDIAS = "https://www.instagram.com/{{username}}/media?max_id={{maxId}}"
ACCOUNT_JSON_INFO = "https://www.instagram.com/{{username}}/?__a=1"
MEDIA_JSON_INFO = "https://www.instagram.com/p/{{code}}/?__a=1"
MEDIA_JSON_BY_LOCATION_ID = "https://www.instagram.com/explore/locations/{{facebookLocationId}}/?__a=1&max_id={{maxId}}"
MEDIA_JSON_BY_TAG = "https://www.instagram.com/explore/tags/{{tag}}/?__a=1&max_id={{maxId}}"
GENERAL_SEARCH = "https://www.instagram.com/web/search/topsearch/?query={{query}}"
ACCOUNT_JSON_INFO_BY_ID = "ig_user({{userId}}){id,username,external_url,full_name,profile_pic_url,biography," \
                          "followed_by{count},follows{count},media{count},is_private,is_verified}"
LAST_COMMENTS_BY_CODE = "ig_shortcode({{code}}){comments.last({{count}}){count,nodes{id,created_at,text," \
                        "user{id,profile_pic_url,username,follows{count},followed_by{count},biography,full_name," \
                        "media{count},is_private,external_url,is_verified}},page_info}}"
COMMENTS_BEFORE_COMMENT_ID_BY_CODE = "ig_shortcode({{code}}){comments.before({{commentId}},{{count}})" \
                                     "{count,nodes{id,created_at,text,user{id,profile_pic_url,username," \
                                     "follows{count},followed_by{count},biography,full_name,media{count}," \
                                     "is_private,external_url,is_verified}},page_info}}"
INSTAGRAM_QUERY_URL = "https://www.instagram.com/query/"


def get_account_page_link(username):
    return ACCOUNT_PAGE.replace("{{username}}", str(username))


def get_account_json_info_link_by_username(username):
    return ACCOUNT_JSON_INFO.replace("{{username}}", str(username))


def get_account_json_info_link_by_account_id(user_id):
    return ACCOUNT_JSON_INFO_BY_ID.replace("{{userId}}", str(user_id))


def get_account_medias_json_link(username, max_id):
    if not max_id:
        max_id = ''
    return ACCOUNT_MEDIAS.replace("{{username}}", username).replace("{{maxId}}", str(max_id))


def get_media_page_link_by_code(code):
    return MEDIA_LINK.replace("{{code}}", str(code))


def get_media_json_link_by_shortcode(shortcode):
    return MEDIA_JSON_INFO.replace("{{code}}", str(shortcode))


def get_medias_json_by_location_id_link(facebook_location_id, max_id):
    if not max_id:
        max_id = ''
    return MEDIA_JSON_BY_LOCATION_ID.replace("{{facebookLocationId}}", str(facebook_location_id))\
        .replace("{{maxId}}", str(max_id))


def get_medias_json_by_tag_link(tag, max_id):
    if not max_id:
        max_id = ''
    return MEDIA_JSON_BY_TAG.replace("{{tag}}", str(tag)).replace("{{maxId}}", str(max_id))


def get_general_search_json_link(query):
    return GENERAL_SEARCH.replace("{{query}}", str(query))


def get_last_comments_by_code_link(code, count):
    return LAST_COMMENTS_BY_CODE.replace("{{code}}", str(code)).replace("{{count}}", str(count))


def get_comments_before_comment_id_by_code(code, count, comment_id):
    return COMMENTS_BEFORE_COMMENT_ID_BY_CODE.replace("{{code}}", str(code)).replace("{{count}}", str(count))\
        .replace("{{commentId}}", str(comment_id))
