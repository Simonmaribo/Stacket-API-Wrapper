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

    def get_id(self):
        return self.props["_id"]

    def get_access(self):
        if self.access is not None:
            return self.access
        data = get(self.getId(), "", self.token)
        self.access = data["access"]
        return self.access

    def get_name(self):
        return self.props["name"]

    def get_type(self):
        return self.props["type"]

    def get_version(self):
        return self.props["version"]

    def get_allocations(self):
        return self.props["allocations"]

    def get_networks(self):
        return self.props["networks"]

    def get_node(self):
        return self.props["node"]

    def get_storage(self):
        return self.props["storage"]

    def get_package(self):
        return self.props["package"]

    def get_status(self):
        data = get(self.getId(), "", self.token)
        self.status = data['service']["status"]
        return self.status

    def get_payment(self):
        return self.props["payment"]

    def get_subusers(self):
        return self.props["subusers"]

    def get_environment(self):
        return self.props["environment"]

    def get_owner(self):
        return self.props["owner"]

    def get_disks(self):
        return self.props["disks"]

    def get_settings(self):
        return self.props["settings"]

    def console(self, command):
        return post(self.getId(), "control", {"state": "console", "command": command}, self.token)

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

    def npm_install(self):
        return control(self.getId(), "npminstall", self.token)

    def get_usage(self):
        return get(self.getId(), "usage", self.token)

    def get_ip(self):
        return get(self.getId(), "ip", self.token)

    def get_actions(self):
        return get(self.getId(), "actions", self.token)

    def get_action(self, id):
        return get(self.getId(), f"actions/{id}", self.token)

    def delete(self):
        result = requests.delete(f"{base}/services/{self.getId()}", headers={"Authorization": self.token})
        if (result.json()["error"]) is not None:
            raise ServiceException("Error: " + result.json()["error"])
        return result.json()

    def set_name(self, name):
        return post(self.getId(), "", {"name": name}, self.token)

    def set_version(self, platform, version):
        return post(self.getId(), "", {"version": {"platform": platform, "version": version}}, self.token)

    def set_package(self, package):
        return post(self.getId(), "", {"package": package}, self.token)

    def set_auto_restart(self, enabled):
        return post(self.getId(), "", {"settings": {"autorestart": enabled}}, self.token)

    def set_firmware(self, firmware):
        return post(self.getId(), "", {"settings": {"firmware": firmware}}, self.token)

    def set_environment(self, key, value):
        return post(self.getId(), "", {"environment": {"key": key, "value": value}}, self.token)

    def get_ftps(self):
        return get(self.getId(), "ftp", self.token)

    def new_ftp(self, name, password, path):
        return post(self.getId(), "ftp", {"name": name, "password": password, "path": path}, self.token)

