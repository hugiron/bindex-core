import re


def validate_skype(username):
    return bool(re.findall(pattern="^[a-zA-Z][a-zA-Z0-9\\._-]{5,31}",
                           string=username))
