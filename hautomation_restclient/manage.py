import requests
import os
from hautomation_restclient import RestApiException
from simplejson import JSONDecodeError


DEVICE_URL = "rest/manage/device/"
DEVICE_BY_PROTOCOL_URL = "rest/manage/device?protocol={protocol}"
DEVICE_BY_ID_URL = "rest/manage/device/{protocol}/{did}"
PROTOCOL_URL = "rest/manage/protocol/"


def get_protocols(server_url, username, password):
    url = os.path.join(server_url, PROTOCOL_URL)
    r = requests.get(url, headers={"USERNAME": username, "PASSWORD": password}, allow_redirects=False)

    if r.status_code != 200:
        try:
            raise RestApiException(r.json(), r.status_code)
        except JSONDecodeError:
            raise RestApiException(r.text, r.status_code)

    return [x["name"] for x in r.json()]


def add_device(protocol, did, caption, device_type, server_url, username, password):

    url = os.path.join(server_url, DEVICE_URL)
    data = {
        "protocol": protocol,
        "did": did,
        "device_type": device_type,
        "caption": caption,
    }
    r = requests.post(url, data=data, headers={"USERNAME": username, "PASSWORD": password}, allow_redirects=False)
    if r.status_code != 302:
        try:
            raise RestApiException(r.json(), r.status_code)
        except JSONDecodeError:
            raise RestApiException(r.text, r.status_code)

    return True


def del_device(protocol, did, server_url, username, password):

    url = os.path.join(server_url, DEVICE_BY_ID_URL.format(**{"did": did, "protocol": protocol}))
    r = requests.delete(url, headers={"USERNAME": username, "PASSWORD": password})
    if r.status_code != 204:
        try:
            raise RestApiException(r.json(), r.status_code)
        except JSONDecodeError:
            raise RestApiException(r.text, r.status_code)
    return True


def get_device(protocol, did, server_url, username, password):

    url = os.path.join(server_url, DEVICE_BY_ID_URL.format(**{"did": did, "protocol": protocol}))
    r = requests.get(url, headers={"USERNAME": username, "PASSWORD": password})
    if r.status_code == 404:
        return []
    if r.status_code != 200:
        try:
            raise RestApiException(r.json(), r.status_code)
        except JSONDecodeError:
            raise RestApiException(r.text, r.status_code)
    return r.json()


def upd_device(protocol, did, server_url, changes, username, password):
    url = os.path.join(server_url, DEVICE_BY_ID_URL.format(**{"did": did, "protocol": protocol}))
    r = requests.put(url, headers={"USERNAME": username, "PASSWORD": password}, data=changes, allow_redirects=False)
    if r.status_code != 302:
        try:
            raise RestApiException(r.json(), r.status_code)
        except JSONDecodeError:
            raise RestApiException(r.text, r.status_code)
    return True


def list_devices(protocol, server_url, username, password):
    url = os.path.join(server_url, DEVICE_BY_PROTOCOL_URL.format(**{"protocol": protocol}))
    r = requests.get(url, headers={"USERNAME": username, "PASSWORD": password})
    if r.status_code == 404:
        return []
    if r.status_code != 200:
        try:
            raise RestApiException(r.json(), r.status_code)
        except JSONDecodeError:
            raise RestApiException(r.text, r.status_code)
    return r.json()
