import json
from mongoengine import Document, StringField


class Profile(Document):
    vk = StringField(db_field='vk', default=None)
    fb = StringField(db_field='fb', default=None)
    instagram = StringField(db_field='instagram', default=None)
    twitter = StringField(db_field='twitter', default=None)
    skype = StringField(db_field='skype', default=None)
    phone = StringField(db_field='phone', default=None)
    meta = {
        'collection': 'profiles',
        'indexes': [
            'vk',
            'fb',
            'instagram',
            'twitter',
            'skype',
            'phone'
        ]
    }

    @staticmethod
    def create(vk=None, fb=None, instagram=None, twitter=None, skype=None, phone=None, **kwargs):
        profile = Profile()
        profile.set_vk(vk if vk else kwargs.get('vk'))
        profile.set_fb(fb if fb else kwargs.get('fb'))
        profile.set_instagram(instagram if instagram else kwargs.get('instagram'))
        profile.set_twitter(twitter if twitter else kwargs.get('twitter'))
        profile.set_skype(skype if skype else kwargs.get('skype'))
        profile.set_phone(phone if phone else kwargs.get('phone'))
        return profile

    def dumps(self):
        return json.dumps(dict(
            vk=self.vk,
            fb=self.fb,
            instagram=self.instagram,
            twitter=self.twitter,
            skype=self.skype,
            phone=self.phone
        ))

    def __str__(self):
        return 'User\nVK: {0}\nFacebook: {1}\nInstagram: {2}\nTwitter: {3}\nSkype: {4}\nPhone: {5}'.format(self.vk,
                                                                                                           self.fb,
                                                                                                           self.instagram,
                                                                                                           self.twitter,
                                                                                                           self.skype,
                                                                                                           self.phone)

    def is_empty(self):
        return not (self.vk or self.fb or self.instagram or self.twitter)

    def get_vk(self):
        return self.vk

    def set_vk(self, vk):
        self.vk = str(vk) if vk else None

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
        self.instagram = str(instagram) if instagram else None

    def contains_instagram(self):
        return bool(self.instagram)

    def get_twitter(self):
        return self.twitter

    def set_twitter(self, twitter):
        self.twitter = str(twitter) if twitter else None

    def contains_twitter(self):
        return bool(self.twitter)

    def get_skype(self):
        return self.skype

    def set_skype(self, skype):
        self.skype = skype

    def contains_skype(self):
        return bool(self.skype)

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

    def contains_phone(self):
        return bool(self.phone)
