import re


class SocialLinkParser:
    @staticmethod
    def parse(profile, content, vk=True, fb=True, instagram=True, twitter=True):
        if vk and not profile.contains_vk():
            profile.set_vk(SocialLinkParser.parse_vk(content))
        if fb and not profile.contains_fb():
            profile.set_fb(SocialLinkParser.parse_fb(content))
        if instagram and not profile.contains_instagram():
            profile.set_instagram(SocialLinkParser.parse_instagram(content))
        if twitter and not profile.contains_twitter():
            profile.set_twitter(SocialLinkParser.parse_twitter(content))
        return profile

    @staticmethod
    def parse_vk(content):
        pass

    @staticmethod
    def parse_fb(content):
        data = re.findall('facebook\\.com/profile\\.php/?\\?id=([\\d]+)', content)
        if data:
            return data[1]
        data = re.findall('facebook\\.com/app_scoped_user_id/([\\d]+)', content)
        if data:
            return data[1]
        data = re.findall('facebook\\.com/([a-zA-Z\\d][a-zA-Z\\d\\.]+)', content)
        if data:
            return data[1] if str.isdigit(data[1]) else FbUsers.get_user_id(data[1])
        return None

    @staticmethod
    def parse_instagram(content):
        data = re.findall('instagram\\.com/([a-zA-Z\\d_][a-zA-Z\\d_\\.]+)', content)
        return data[1] if data else None

    @staticmethod
    def parse_twitter(profile, content):
        pass
