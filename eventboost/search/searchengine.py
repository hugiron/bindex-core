import eventboost.api.vk.users as VkUsers
import eventboost.api.vk.wall as VkWall
import eventboost.api.instagram.media as InstaMedia


class SearchVkByUserInfo:
    @staticmethod
    def update(profile):
        if profile.contains_vk():
            data = VkUsers.get(profile.get_vk(), ['connections'])
            profile.set_vk(data['id'])
            if 'facebook' in data:
                profile.set_fb(data['facebook'])
            if 'instagram' in data:
                profile.set_instagram(data['instagram'])
            if 'twitter' in data:
                profile.set_twitter(data['twitter'])
        return profile

    @staticmethod
    def is_ready(profile):
        return profile.contains_vk() and \
               not (profile.contains_instagram() and profile.contains_twitter() and profile.contains_fb())


class SearchVkByUserWall:
    @staticmethod
    def update(profile, access_token):
        data = VkWall.get(
            owner_id=profile.get_vk() if int == type(profile.get_vk()) else 0,
            domain=profile.get_vk() if str == type(profile.get_vk()) else '',
            offset=0,
            count=100,
            filter='owner',
            fields=[],
            access_token=access_token
        )
        if 'items' in data:
            for item in data['items']:
                if 'copy_history' not in item and 'post_source' in item and 'url' in item['post_source']:
                    profile.set_instagram(InstaMedia.get_author(item['post_source']['url']))
                    if profile.contains_instagram():
                        break
        return profile

    @staticmethod
    def is_ready(profile):
        return profile.contains_vk() and not profile.contains_instagram()
