class MethodApiException(Exception):
    def __init__(self, code, message=''):
        self.code = code
        self.message = message

    def __str__(self):
        return 'VK API Error #{0}: {1}'.format(self.code, self.message)
