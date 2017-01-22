import pendex.api.vk.users as VkUsers
import pendex.api.vk.wall as VkWall
import pendex.api.instagram.media as InstaMedia
import pendex.api.twitter.users as TwitterUsers
from pendex.search.tools.sociallinkparser import SocialLinkParser
from pendex.api.instagram.method import get_account_by_id
from pendex.api.twitter.users import get_screen_name_by_user_id
from pendex.api.vk.users import get_phones


class SearchVkByUserInfo:
    @staticmethod
    def update(profile):
        if profile.contains_vk():
            data = VkUsers.get(
                user_ids=profile.get_vk(),
                fields=['connections', 'site', 'status']
            )[0]
            if 'facebook' in data and not profile.contains_fb():
                profile.set_fb(data['facebook'])
            if 'instagram' in data and not profile.contains_instagram():
                profile.set_instagram(data['instagram'])
            if 'twitter' in data and not profile.contains_twitter():
                profile.set_twitter(data['twitter'])
            if 'skype' in data and not profile.contains_skype():
                profile.set_skype(data['skype'])
            profile = SocialLinkParser.parse(
                profile=profile,
                content='{0} | {1} | {2}'.format(data.get('site'), data.get('status'), '|'.join(get_phones(profile.get_vk()))),
                vk=False
            )
        return profile

    @staticmethod
    def is_ready(profile):
        return profile.contains_vk() and \
               not (profile.contains_instagram() and profile.contains_twitter() and profile.contains_fb()
                    and profile.contains_skype() and profile.contains_phone())


class SearchVkByUserWall:
    @staticmethod
    def update(profile):
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
            instagram_username = get_account_by_id(id=profile.get_instagram()).username
            profile = SocialLinkParser.parse(
                profile=profile,
                content=InstaMedia.get_status(instagram_username),
                instagram=False
            )
        return profile

    @staticmethod
    def is_ready(profile):
        return profile.contains_instagram() and \
               not (profile.contains_fb() and profile.contains_vk() and profile.contains_twitter()
                    and profile.contains_phone())


class SearchTwitterByUserStatus:
    @staticmethod
    def update(profile):
        if profile.contains_twitter():
            twitter_username = get_screen_name_by_user_id(user_id=profile.get_twitter())
            profile = SocialLinkParser.parse(
                profile=profile,
                content=TwitterUsers.get_profile_card(twitter_username),
                twitter=False
            )
        return profile

    @staticmethod
    def is_ready(profile):
        return profile.contains_twitter() and \
               not (profile.contains_fb() and profile.contains_instagram() and profile.contains_vk()
                    and profile.contains_phone())
