class SocialLinkParser:
    @staticmethod
    def parse(profile, content, vk=True, fb=True, instagram=True, twitter=True):
        if vk and not profile.contains_vk():
            profile.set_vk(SocialLinkParser.parse_vk(profile, content))
        if fb and not profile.contains_fb():
            profile.set_fb(SocialLinkParser.parse_fb(profile, content))
        if instagram and not profile.contains_instagram():
            profile.set_instagram(SocialLinkParser.parse_instagram(profile, content))
        if twitter and not profile.contains_twitter():
            profile.set_twitter(SocialLinkParser.parse_twitter(profile, content))
        return profile

    @staticmethod
    def parse_vk(profile, content):
        pass

    @staticmethod
    def parse_fb(profile, content):
        pass

    @staticmethod
    def parse_instagram(profile, content):
        pass

    @staticmethod
    def parse_twitter(profile, content):
        pass
