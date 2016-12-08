import eventboost.api.vk.users as VkUsers
import eventboost.api.vk.wall as VkWall
import eventboost.api.instagram.media as InstaMedia
import eventboost.api.twitter.users as TwitterUsers
from eventboost.search.tools.sociallinkparser import SocialLinkParser


class SearchVkByUserInfo:
    @staticmethod
    def update(profile):
        if profile.contains_vk():
            data = VkUsers.get(
                user_ids=profile.get_vk(),
                fields=['connections', 'site', 'status']
            )[0]
            profile.set_vk(data['id'])
            if 'facebook' in data:
                profile.set_fb(data['facebook'])
            if 'instagram' in data:
                profile.set_instagram(data['instagram'])
            if 'twitter' in data:
                profile.set_twitter(data['twitter'])
            if 'skype' in data:
                profile.set_skype(data['skype'])
            profile = SocialLinkParser.parse(
                profile=profile,
                content='{0} {1}'.format(data.get('site'), data.get('status')),
                vk=False
            )
        return profile

    @staticmethod
    def is_ready(profile):
        return profile.contains_vk() and \
               not (profile.contains_instagram() and profile.contains_twitter() and profile.contains_fb())


class SearchVkByUserWall:
    @staticmethod
    def update(profile):
        if not str(profile.get_vk()).isdigit():
            profile.set_vk(VkUsers.get(user_ids=profile.get_vk(), fields=[])[0]['id'])
        for url in InstaMedia.get_notes(VkWall.get_source_code(owner_id=profile.get_vk())):
            profile.set_instagram(InstaMedia.get_author('https://{0}'.format(url)))
            if profile.contains_instagram():
                break
        return profile

    @staticmethod
    def is_ready(profile):
        return profile.contains_vk() and not profile.contains_instagram()


class SearchInstagramByUserStatus:
    @staticmethod
    def update(profile):
        if profile.contains_instagram():
            profile = SocialLinkParser.parse(
                profile=profile,
                content=InstaMedia.get_status(profile.get_instagram()),
                instagram=False
            )
        return profile

    @staticmethod
    def is_ready(profile):
        return profile.contains_instagram() and \
               not (profile.contains_fb() and profile.contains_vk() and profile.contains_twitter())


class SearchTwitterByUserStatus:
    @staticmethod
    def update(profile):
        if profile.contains_twitter():
            profile = SocialLinkParser.parse(
                profile=profile,
                content=TwitterUsers.get_profile_card(profile.get_twitter()),
                twitter=False
            )
        return profile

    @staticmethod
    def is_ready(profile):
        return profile.contains_twitter() and \
               not (profile.contains_fb() and profile.contains_instagram() and profile.contains_vk())
