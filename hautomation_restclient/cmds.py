import requests
import os
from hautomation_restclient import RestApiException


PL_SWITCH_URL = "rest/cmd/pl_switch/{protocol}/{did}"
PL_DIM_URL = "rest/cmd/pl_dim/{protocol}/{did}"
PL_BRI_URL = "rest/cmd/pl_bri/{protocol}/{did}"


def pl_switch(protocol, did, value, server_url, username, password):
    """
    >>> pl_switch("X10", "A5", "on", "http://localhost:8000", "r", "r")
    """

    url = os.path.join(server_url, PL_SWITCH_URL.format(**{"protocol": protocol, "did": did, }))
    r = requests.put(url, data={"value": value}, headers={"USERNAME": username, "PASSWORD": password}, allow_redirects=False)
    print r.content
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
    print username
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
