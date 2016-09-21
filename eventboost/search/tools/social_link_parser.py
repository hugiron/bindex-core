class SocialLinkParser:
    @staticmethod
    def parse(user, content, vk=True, fb=True, instagram=True, twitter=True):
        if vk & (not user.vk):
            user.vk = SocialLinkParser.parse_vk(user, content)
        if fb & (not user.fb):
            user.fb = SocialLinkParser.parse_fb(user, content)
        if instagram & (not user.instagram):
            user.instagram = SocialLinkParser.parse_instagram(user, content)
        if twitter & (not user.twitter):
            user.twitter = SocialLinkParser.parse_twitter(user, content)
        return user

    @staticmethod
    def parse_vk(user, content):
        pass

    @staticmethod
    def parse_fb(user, content):
        pass

    @staticmethod
    def parse_instagram(user, content):
        pass

    @staticmethod
    def parse_twitter(user, content):
        pass
