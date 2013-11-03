

class RestApiException(Exception):
    def __init__(self, message, status_code):
        super(RestApiException, self).__init__(message)
        self.status_code = status_code
        self.message = message

    def __unicode__(self, ):
        return "%s" % self.message

    def __repr__(self, ):
        return "%s" % self.message
