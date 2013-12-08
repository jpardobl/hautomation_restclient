import requests
import os
from hautomation_restclient import RestApiException
from simplejson import JSONDecodeError

PL_SWITCH_URL = "rest/cmd/pl_switch/{protocol}/{did}"
PL_DIM_URL = "rest/cmd/pl_dim/{protocol}/{did}"
PL_BRI_URL = "rest/cmd/pl_bri/{protocol}/{did}"
PL_ALL_LIGHTS_OFF = "rest/cmd/pl_all_lights_off/{protocol}/{group}"
PL_ALL_LIGHTS_ON = "rest/cmd/pl_all_lights_on/{protocol}/{group}"


def pl_all_lights_on(protocol, group, server_url, username, password):
    #cmd/pl_all_lights_off/(?P<protocol>[a-z0-9A-Z]{3,4})/(?P<group>[\d\w]+)/
    url = os.path.join(server_url, PL_ALL_LIGHTS_ON.format(**{"protocol": protocol, "group": group}))
    r = requests.put(url, data={}, headers={"USERNAME": username, "PASSWORD": password}, allow_redirects=False)
    if r.status_code != 200:
        try:
            raise RestApiException(r.json(), r.status_code)
        except JSONDecodeError:
            raise RestApiException(r.text, r.status_code)
    return True


def pl_all_lights_off(protocol, group, server_url, username, password):
    #cmd/pl_all_lights_off/(?P<protocol>[a-z0-9A-Z]{3,4})/(?P<group>[\d\w]+)/
    url = os.path.join(server_url, PL_ALL_LIGHTS_OFF.format(**{"protocol": protocol, "group": group}))
    r = requests.put(url, data={}, headers={"USERNAME": username, "PASSWORD": password}, allow_redirects=False)
    if r.status_code != 200:
        try:
            raise RestApiException(r.json(), r.status_code)
        except JSONDecodeError:
            raise RestApiException(r.text, r.status_code)
    return True


def pl_switch(protocol, did, value, server_url, username, password):
    """
    >>> pl_switch("X10", "A5", "on", "http://localhost:8000", "r", "r")
    """

    url = os.path.join(server_url, PL_SWITCH_URL.format(**{"protocol": protocol, "did": did, }))
    r = requests.put(url, data={"value": value}, headers={"USERNAME": username, "PASSWORD": password}, allow_redirects=False)
    #print r.content
    if r.status_code != 302:
        try:
            raise RestApiException(r.json(), r.status_code)
        except JSONDecodeError:
            raise RestApiException(r.text, r.status_code)
    return True


def pl_dim(protocol, did, value, server_url, username, password):
    """
    >>> pl_dim("X10", "A5", 30, "http://localhost:8000", "r", "r")
    """
    #print username
    url = os.path.join(server_url, PL_DIM_URL.format(**{"protocol": protocol, "did": did, }))
    r = requests.post(url, data={"value": value}, headers={"USERNAME": username, "PASSWORD": password}, allow_redirects=False)
    if r.status_code != 302:
        try:
            raise RestApiException(r.json(), r.status_code)
        except JSONDecodeError:
            raise RestApiException(r.text, r.status_code)
    return True


def pl_bri(protocol, did, value, server_url, username, password):
    """
    >>> pl_bri("X10", "A5", 30, "http://localhost:8000", "r", "r")
    """

    url = os.path.join(server_url, PL_BRI_URL.format(**{"protocol": protocol, "did": did, }))
    r = requests.post(url, data={"value": value}, headers={"USERNAME": username, "PASSWORD": password}, allow_redirects=False)
    if r.status_code != 302:
        try:
            raise RestApiException(r.json(), r.status_code)
        except JSONDecodeError:
            raise RestApiException(r.text, r.status_code)
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()
