import requests

from .errors import ServiceException

base = "https://domains_devapi.stacket.net/"


def get(id, path, token):
    result = requests.get(f"{base}/{id}/{path}", headers={"Authorization": token})
    return result.json()


def post(id, path, body, token):
    result = requests.post(f"{base}/{id}/{path}", data=body, headers={"Authorization": token})
    if "error" in result.json() and result.json()["error"] is not None:
        raise ServiceException("Error: " + result.json()["error"])
    return result.json()


def _delete(id, path, token):
    result = requests.delete(f"{base}/{id}/{path}", headers={"Authorization": token})
    if (result.json()["error"]) is not None:
        raise ServiceException("Error: " + result.json()["error"])
    return result.json()


class Domain:
    def __init__(self, domain_id, token, props):
        self.id = domain_id
        self.token = token
        self.props = props

    def addProxy(self, service: str, subdomain: str):
        result = post(self.id, "proxy", {"subdomain": subdomain, "service": service}, self.token)
        Json = result.json()
        return Json

    def deleteProxy(self, subdomain: str):
        result = _delete(self.id, "proxy" + subdomain, self.token)
        Json = result.json()
        return Json

    def getDomainInfo(self):
        result = get(self.id, "", self.token)
        Json = result.json()
        return Json

    def getDomain(self):
        return self.props["domain"]

    def getDomainKey(self):
        return self.props["domainKey"]

    def isVerified(self):
        return bool(self.props["verified"])

    def isRegistered(self):
        return bool(self.props["registered"])

    def getSubdomains(self):
        return self.props["proxypass"]

    def getOwner(self):
        return self.props["owner"]
