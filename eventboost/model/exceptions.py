class MethodApiException(Exception):
    def __init__(self, code, message=None):
        self.code = code
        self.message = message

    def __str__(self):
        return 'VK API Error #{0}: {1}'.format(self.code, self.message)


class RequestLimitException(Exception):
    def __init__(self, message=''):
        self.message = message


class InstagramException(Exception):
    def __init__(self, message=''):
        self.message = message


class InstagramNotFoundException(InstagramException):
    def __init__(self, message=''):
        self.message = message
