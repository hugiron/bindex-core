class Profile:
    def __init__(self, vk=None, fb=None, instagram=None, twitter=None):
        self.__vk = vk
        self.__fb = fb
        self.__instagram = instagram
        self.__twitter = twitter

    def __str__(self):
        return 'User\nVK: {0}\nFacebook: {1}\nInstagram: {2}\nTwitter: {3}'.format(self.__vk,
                                                                                   self.__fb,
                                                                                   self.__instagram,
                                                                                   self.__twitter)

    def is_empty(self):
        return not (self.__vk or self.__fb or self.__instagram or self.__twitter)

    def get_vk(self):
        return self.__vk

    def set_vk(self, vk):
        self.__vk = vk

    def contains_vk(self):
        return bool(self.__vk)

    def get_fb(self):
        return self.__fb

    def set_fb(self, fb):
        self.__fb = fb.replace('+', '')

    def contains_fb(self):
        return bool(self.__fb)

    def get_instagram(self):
        return self.__instagram

    def set_instagram(self, instagram):
        self.__instagram = instagram

    def contains_instagram(self):
        return bool(self.__instagram)

    def get_twitter(self):
        return self.__twitter

    def set_twitter(self, twitter):
        self.__twitter = twitter

    def contains_twitter(self):
        return bool(self.__twitter)