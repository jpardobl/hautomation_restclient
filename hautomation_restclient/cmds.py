import requests
import os

PL_SWITCH_URL = "rest/cmd/pl_switch/{protocol}/{did}"
PL_DIM_URL = "rest/cmd/pl_dim/{protocol}/{did}"
PL_BRI_URL = "rest/cmd/pl_bri/{protocol}/{did}"


def pl_switch(protocol, did, value, server_url, username, password):
    """
    >>> pl_switch("X10", "A1", "on", "http://localhost:8000", "r", "raaa")
    """

    url = os.path.join(server_url, PL_SWITCH_URL.format(**{"protocol": protocol, "did": did, }))

    return requests.put(url, data={"value": value}, headers={"USERNAME": username, "PASSWORD": password})


def pl_dim(protocol, did, value, server_url, username, password):
    """
    >>> pl_dim("X10", "A1", 30, "http://localhost:8000", "r", "r")
    """
    url = os.path.join(server_url, PL_DIM_URL.format(**{"protocol": protocol, "did": did, }))
    return requests.post(url, data={"value": value}, headers={"USERNAME": username, "PASSWORD": password})


def pl_bri(protocol, did, value, server_url, username, password):
    """
    >>> pl_bri("X10", "A1", 30, "http://localhost:8000", "r", "r")
    """

    url = os.path.join(server_url, PL_BRI_URL.format(**{"protocol": protocol, "did": did, }))
    return requests.post(url, data={"value": value}, headers={"USERNAME": username, "PASSWORD": password})


if __name__ == "__main__":
    import doctest
    doctest.testmod()
