from mongoengine import Q
from eventboost.search.searchengine import *
from eventboost.model.profile import Profile


parser = [
    SearchVkByUserWall,
    SearchVkByUserInfo,
    SearchInstagramByUserStatus,
    SearchTwitterByUserStatus
]


def profile_parser(profile):
    current_progress = 0
    old_progress = -1
    while current_progress != old_progress:
        old_progress = current_progress
        for i in range(len(parser)):
            if (current_progress & (1 << i)) == 0 and parser[i].is_ready(profile=profile):
                current_progress |= 1 << i
                profile = parser[i].update(profile=profile)
    return profile


def profile_save(profile):
    upsert_query = (Q(vk__exists=False) | Q(vk=profile.get_vk())) & \
                   (Q(fb__exists=False) | Q(fb=profile.get_fb()))
    upsert_data = dict(upsert=True, new=True)
    if profile.contains_vk():
        upsert_data['vk'] = profile.get_vk()
    if profile.contains_fb():
        upsert_data['fb'] = profile.get_fb()
    if profile.contains_instagram():
        upsert_data['instagram'] = profile.get_instagram()
    if profile.contains_twitter():
        upsert_data['twitter'] = profile.get_twitter()
    Profile.objects(upsert_query).modify(**upsert_data)


def get_contains_count(profile):
    return profile.contains_vk() + profile.contains_fb() + profile.contains_instagram() + profile.contains_twitter()
