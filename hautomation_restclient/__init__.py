

class RestApiException(Exception):
    def __init__(self, message, status_code):
        super(RestApiException, self).__init__(message)
        self.status_code = status_code

