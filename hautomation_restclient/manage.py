import requests
import os


DEVICE_URL = "rest/manage/device/"
DEVICE_BY_ID_URL = "rest/manage/device/{protocol}/{did}"


def add_device(protocol, did, caption, device_type, server_url, username, password):

    url = os.path.join(server_url, DEVICE_URL)
    data = {
        "protocol": protocol,
        "did": did,
        "device_type": device_type,
        "caption": caption,
    }
    r = requests.post(url, data=data, headers={"USERNAME": username, "PASSWORD": password}, allow_redirects=False)
    return r


def del_device(protocol, did, server_url, username, password):

    url = os.path.join(server_url, DEVICE_BY_ID_URL.format(**{"did": did, "protocol": protocol}))
    return requests.delete(url, headers={"USERNAME": username, "PASSWORD": password})



def get_device(protocol, did, server_url, username, password):

    url = os.path.join(server_url, DEVICE_BY_ID_URL.format(**{"did": did, "protocol": protocol}))
    r = requests.get(url, headers={"USERNAME": username, "PASSWORD": password})
    if r.status_code == 200:
        return r.json()
    return r


def upd_device(protocol, did, server_url, changes, username, password):
    url = os.path.join(server_url, DEVICE_BY_ID_URL.format(**{"did": did, "protocol": protocol}))
    return requests.put(url, headers={"USERNAME": username, "PASSWORD": password}, data=changes, allow_redirects=False)
