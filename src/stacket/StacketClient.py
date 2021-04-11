from .Service import Service
from .errors import *
from requests import post, get
from .config import base


class StacketClient:
    def __init__(self, token: str = None):
        if not token:
            raise MissingArgument("Token wasn't entered")
        self.__token__ = token

    def verify(self):
        result = post(f"{base}/auth/verify", {"token": self.__token__})
        if "state" in result.json() and result.json()["state"] == "verified":
            return True
        return False

    def getServices(self):
        result = get(f"{base}/services/", headers={"Authorization": self.__token__})
        Json = result.json()
        if not 200 <= result.status_code < 300:
            raise ClientException("Error: " + Json["error"])
        services = []
        for service in Json:
            services.append(Service(service["service"], self.__token__, ))
        return services

    def getService(self, id):
        result = get(f"{base}/services/{id}", headers={"Authorization": self.__token__})
        Json = result.json()
        if not 200 <= result.status_code < 300:
            raise ClientException("Error: " + Json["error"])
        return Service(Json["service"], self.__token__, Json["access"])

    def createService(self, settings):
        result = post(f"{base}/services/", settings, headers={"Authorization": self.__token__})
        Json = result.json()
        if not 200 <= result.status_code < 300:
            raise ClientException("Error: " + Json["error"])
        return Service(Json, self.__token__)