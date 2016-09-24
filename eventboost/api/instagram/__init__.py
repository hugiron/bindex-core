class InstagramApi:
    @staticmethod
    def get_base_uri():
        return 'https://instagram.com'

    @staticmethod
    def get_pattern_uri_in_status():
        return '\"external_url\":\\s*\"([^\"]+)\"'