import re
import eventboost.api.fb.users as FbUsers
import eventboost.api.vk.users as VkUsers


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
        data = re.findall('vk\\.com/id([\\d]+)', content)
        if data:
            return data[0]
        data = re.findall('vk\\.com/([a-zA-Z][a-zA-Z\\d_]+)', content)
        if data:
            return VkUsers.get(
                user_ids=data[0],
                fields=[]
            )[0]['id']
        return None

    @staticmethod
    def parse_fb(content):
        data = re.findall('(facebook|fb)\\.com/profile\\.php/?\\?id=([\\d]+)', content)
        if data:
            return data[0][1]
        data = re.findall('(facebook|fb)\\.com/app_scoped_user_id/([\\d]+)', content)
        if data:
            return data[0][1]
        data = re.findall('(facebook|fb)\\.com/([a-zA-Z\\d][a-zA-Z\\d\\.]+)', content)
        if data:
            return data[0][1] if str.isdigit(data[0][1]) else FbUsers.get_user_id(data[0][1])
        return None

    @staticmethod
    def parse_instagram(content):
        data = re.findall('instagram\\.com/([a-zA-Z\\d_][a-zA-Z\\d_\\.]+)', content)
        result = data[0] if data else None
        data = re.findall(pattern='instagram([^a-zA-Z\\d_]+)?([a-zA-Z\\d_][a-zA-Z\\d_\\.]+)',
                          string=content,
                          flags=re.IGNORECASE)
        result = data[0][1] if not result and data else result
        return result

    @staticmethod
    def parse_twitter(content):
        data = re.findall('twitter\\.com/([a-zA-Z\\d_]+)', content)
        return data[0] if data else None
