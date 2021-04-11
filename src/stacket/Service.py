import requests
from .config import base
from .errors import ServiceException


def control(id, state, token):
    return post(id, "control", {"state": state}, token)


def get(id, path, token):
    result = requests.get(f"{base}/services/{id}/{path}", headers={"Authorization": token})
    return result.json()


def post(id, path, body, token):
    result = requests.post(f"{base}/services/{id}/{path}", data=body, headers={"Authorization": token})
    if "error" in result.json() and result.json()["error"] is not None:
        raise ServiceException("Error: " + result.json()["error"])
    return result.json()


def _delete(id, path, token):
    result = requests.delete(f"{base}/services/{id}/{path}", headers={"Authorization": token})
    if (result.json()["error"]) is not None:
        raise ServiceException("Error: " + result.json()["error"])
    return result.json()


class Service:
    def __init__(self, props=None, token=None, access=None):
        self.props = props
        self.token = token
        self.access = access
        self.status = props["status"]

    def getId(self):
        return self.props["_id"]

    def getAccess(self):
        if self.access is not None:
            return self.access
        data = get(self.getId(), "", self.token)
        self.access = data["access"]
        return self.access

    def getName(self):
        return self.props["name"]

    def getType(self):
        return self.props["type"]

    def getVersion(self):
        return self.props["version"]

    def getAllocations(self):
        return self.props["allocations"]

    def getNetworks(self):
        return self.props["networks"]

    def getNode(self):
        return self.props["node"]

    def getStorage(self):
        return self.props["storage"]

    def getPackage(self):
        return self.props["package"]

    def getStatus(self):
        data = get(self.getId(), "", self.token)
        self.status = data["service"]["access"]
        return self.status

    def getPayment(self):
        return self.props["payment"]

    def getSubusers(self):
        return self.props["subusers"]

    def getEnvironment(self):
        return self.props["environment"]

    def getOwner(self):
        return self.props["owner"]

    def getDisk(self):
        return self.props["disks"]

    def getSettings(self):
        return self.props["settings"]

    def powerOn(self):
        return control(self.getId(), "start", self.token)

    def powerOff(self):
        return control(self.getId(), "stop", self.token)

    def kill(self):
        return control(self.getId(), "kill", self.token)

    def activate(self):
        return control(self.getId(), "activate", self.token)

    def reactivate(self):
        return control(self.getId(), "reactivate", self.token)

    def hibernate(self):
        return control(self.getId(), "hibernate", self.token)

    def update(self):
        return control(self.getId(), "update", self.token)

    def npminstall(self):
        return control(self.getId(), "npminstall", self.token)

    def getUsage(self):
        return get(self.getId(), "usage", self.token)

    def getIp(self):
        return get(self.getId(), "ip", self.token)

    def getActions(self):
        return get(self.getId(), "actions", self.token)

    def getAction(self, id):
        return get(self.getId(), f"actions/{id}", self.token)

    def delete(self):
        result = requests.delete(f"{base}/services/{self.getId()}", headers={"Authorization": self.token})
        if (result.json()["error"]) is not None:
            raise ServiceException("Error: " + result.json()["error"])
        return result.json()

    def setName(self, name):
        return post(self.getId(), "", {"name": name}, self.token)

    def setVersion(self, platform, version):
        return post(self.getId(), "", {"version": {"platform": platform, "version": version}}, self.token)

    def setPackage(self, package):
        return post(self.getId(), "", {"package": package}, self.token)

    def setAutoRestart(self, enabled):
        return post(self.getId(), "", {"settings": {"autorestart": enabled}}, self.token)

    def setFirmware(self, firmware):
        return post(self.getId(), "", {"settings": {"firmware": firmware}}, self.token)

    def setEnvironment(self, key, value):
        return post(self.getId(), "", {"environment": {"key": key, "value": value}}, self.token)

    def getFTP(self):
        return get(self.getId(), "ftp", self.token)

    def newFTP(self, name, password, path):
        return post(self.getId(), "ftp", {"name": name, "password": password, "path": path}, self.token)

