class MissingArgument(BaseException):
    def __init__(self, *args, **kwargs):
        pass


class UnauthorizedToken(BaseException):
    def __init__(self, *args, **kwargs):
        pass


class ClientException(BaseException):
    def __init__(self, *args, **kwargs):
        pass


class ServiceException(BaseException):
    def __init__(self, *args, **kwargs):
        pass
