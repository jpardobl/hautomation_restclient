#This file mainly exists to allow python setup.py test to work.
import unittest
from manage import *
from cmds import *

SERVER_URL = "http://raspberry:8000"
USERNAME = "pi"
PASSWORD = "pi"


class TestClient(unittest.TestCase):
    def test_uno(self):
        print "testing protocol retrieval"

        r = get_protocols(SERVER_URL, USERNAME, PASSWORD)

        for x in r:
            print x

        print "Adding device"
        did = "A2"
        r = add_device("X10", did, "terrace", "switch", SERVER_URL, USERNAME, PASSWORD)
        self.assertTrue(r, "Not creating devices properly")

        print "updating device"
        r = upd_device("X10", did, SERVER_URL, {"device_type": "dimmer"}, USERNAME, PASSWORD)

        self.assertTrue(r, "Not updating device info")

        print "sending switch on command"
        r = pl_switch("X10", did, "on", SERVER_URL, USERNAME, PASSWORD)

        self.assertTrue(r, "pl_switch failed")
        print "sending dim command"
        r = pl_dim("X10", did, 20, SERVER_URL, USERNAME, PASSWORD)
        self.assertTrue(r, "pl_dim failed")

        print "sending bri command"
        r = pl_bri("X10", did, 20, SERVER_URL, USERNAME, PASSWORD)
        self.assertTrue(r, "pl_bri failed")
        print "deleting device"
        r = del_device("X10", did, SERVER_URL, USERNAME, PASSWORD)
        self.assertTrue(r, "not deleting devices")


def main():
    unittest.main()

if __name__ == "__main__":
    unittest.main()
