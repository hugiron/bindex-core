from mongoengine import Document, StringField


class Profile(Document):
    vk = StringField(db_field='vk', default=None)
    fb = StringField(db_field='fb', default=None)
    instagram = StringField(db_field='instagram', default=None)
    twitter = StringField(db_field='twitter', default=None)
    meta = {
        'collection': 'profiles',
        'indexes': [
            {
                'fields': ['vk', 'fb', 'instagram', 'twitter']
            }
        ]
    }

    @staticmethod
    def create(vk=None, fb=None, instagram=None, twitter=None, **kwargs):
        profile = Profile()
        profile.set_vk(vk if vk else kwargs.get('vk'))
        profile.set_fb(fb if fb else kwargs.get('fb'))
        profile.set_instagram(instagram if instagram else kwargs.get('instagram'))
        profile.set_twitter(twitter if twitter else kwargs.get('twitter'))
        return profile

    def __str__(self):
        return 'User\nVK: {0}\nFacebook: {1}\nInstagram: {2}\nTwitter: {3}'.format(self.vk,
                                                                                   self.fb,
                                                                                   self.instagram,
                                                                                   self.twitter)

    def is_empty(self):
        return not (self.vk or self.fb or self.instagram or self.twitter)

    def get_vk(self):
        return self.vk

    def set_vk(self, vk):
        self.vk = str(vk)

    def contains_vk(self):
        return bool(self.vk)

    def get_fb(self):
        return self.fb

    def set_fb(self, fb):
        self.fb = str(fb.replace('+', '')) if fb else None

    def contains_fb(self):
        return bool(self.fb)

    def get_instagram(self):
        return self.instagram

    def set_instagram(self, instagram):
        self.instagram = str(instagram)

    def contains_instagram(self):
        return bool(self.instagram)

    def get_twitter(self):
        return self.twitter

    def set_twitter(self, twitter):
        self.twitter = str(twitter)

    def contains_twitter(self):
        return bool(self.twitter)