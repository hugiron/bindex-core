import json
from datetime import datetime
from mongoengine import DynamicDocument, StringField, DateTimeField, DynamicField
from eventboost.search.tools.validator import *


class Profile(DynamicDocument):
    last_modified = DateTimeField(db_field='last_modified', default=datetime.now())
    vk = StringField(db_field='vk', default=None)
    fb = StringField(db_field='fb', default=None)
    instagram = StringField(db_field='instagram', default=None)
    twitter = StringField(db_field='twitter', default=None)
    other = DynamicField(db_field='other', default=dict())
    meta = {
        'collection': 'profiles',
        'indexes': [
            'last_modified',
            'vk',
            'fb',
            'instagram',
            'twitter',
            'other.skype',
            'other.phone',
            'other.email'
        ]
    }

    @staticmethod
    def create(vk=None, fb=None, instagram=None, twitter=None, skype=None, phone=None, email=None, **kwargs):
        profile = Profile()
        profile.set_vk(vk if vk else kwargs.get('vk'))
        profile.set_fb(fb if fb else kwargs.get('fb'))
        profile.set_instagram(instagram if instagram else kwargs.get('instagram'))
        profile.set_twitter(twitter if twitter else kwargs.get('twitter'))
        profile.set_skype(skype if skype else kwargs.get('skype'))
        profile.set_phone(phone if phone else kwargs.get('phone'))
        profile.set_email(email if email else kwargs.get('email'))
        return profile

    def dumps(self):
        return json.dumps(dict(
            vk=self.vk,
            fb=self.fb,
            instagram=self.instagram,
            twitter=self.twitter,
            other=self.other
        ))

    def __str__(self):
        return 'User\nVK: {0}\nFacebook: {1}\nInstagram: {2}\nTwitter: {3}\n' \
               'Skype: {4}\nPhone: {5}\nEmail: {6}'.format(self.vk,
                                                           self.fb,
                                                           self.instagram,
                                                           self.twitter,
                                                           self.other.get('skype'),
                                                           self.other.get('phone'),
                                                           self.other.get('email'))

    def is_empty(self):
        return not (self.vk or self.fb or self.instagram or self.twitter)

    def modify(self):
        self.last_modified = datetime.now()

    def get_vk(self):
        return self.vk

    def set_vk(self, vk):
        self.modify()
        self.vk = str(vk) if vk else None

    def contains_vk(self):
        return bool(self.vk)

    def get_fb(self):
        return self.fb

    def set_fb(self, fb):
        self.modify()
        self.fb = str(fb.replace('+', '')) if fb else None

    def contains_fb(self):
        return bool(self.fb)

    def get_instagram(self):
        return self.instagram

    def set_instagram(self, instagram):
        self.modify()
        self.instagram = str(instagram) if instagram else None

    def contains_instagram(self):
        return bool(self.instagram)

    def get_twitter(self):
        return self.twitter

    def set_twitter(self, twitter):
        self.modify()
        self.twitter = str(twitter) if twitter else None

    def contains_twitter(self):
        return bool(self.twitter)

    def get_skype(self):
        return self.other.get('skype')

    def set_skype(self, skype):
        if not skype or validate_skype(skype):
            self.modify()
            self.other['skype'] = skype

    def contains_skype(self):
        return 'skype' in self.other

    def get_phone(self):
        return self.other.get('phone')

    def set_phone(self, phone):
        self.modify()
        if 'phone' not in self.other:
            self.other['phone'] = list()
        if type(phone) == list:
            self.other['phone'].extend(phone)
        elif type(phone) == str:
            self.other['phone'].append(phone)
        self.other['phone'] = list(set(self.other['phone']))

    def contains_phone(self):
        return 'phone' in self.other

    def get_email(self):
        return self.other.get('email')

    def set_email(self, email):
        if email:
            self.modify()
            self.other['email'] = email

    def contains_email(self):
        return 'email' in self.other

    def get_other(self):
        return self.other

    def contains_other(self):
        return bool(self.other)
