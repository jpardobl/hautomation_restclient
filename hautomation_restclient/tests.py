#This file mainly exists to allow python setup.py test to work.
import unittest
from manage import *
from cmds import *

SERVER_URL = "http://localhost:8000"


class TestClient(unittest.TestCase):
    def test_uno(self):
        print "Adding device"
        did = "A5"
        r = add_device("X10", did, "terrace", "switch", SERVER_URL, "r", "r")

        self.assertEquals(r.status_code, 302, "Not creating devices properly, response: %s, response code: %s" % (r.content, r.status_code))

        print "updating device"
        r = upd_device("X10", did, SERVER_URL, {"device_type": "dimmer"}, "r", "r")

        self.assertEquals(r.status_code, 302, "Not updating device info, server response: %s, response code: %s" % (r.content, r.status_code))

        print "sending switch on command"
        r = pl_switch("X10", did, "on", SERVER_URL, "r", "r")

        self.assertEquals(r.status_code, 200, "pl_switch failed, server response: %s, response code: %s" % (r.content, r.status_code))
        print "sending dim command"
        r = pl_dim("X10", did, 20, SERVER_URL, "r", "r")
        self.assertEquals(r.status_code, 200, "pl_dim failed, server response: %s, response code: %s" % (r.content, r.status_code))

        print "sending bri command"
        r = pl_bri("X10", did, 20, SERVER_URL, "r", "r")
        self.assertEquals(r.status_code, 200, "pl_bri failed, server response: %s, response code: %s" % (r.content, r.status_code))
        print "deleting device"
        r = del_device("X10", did, SERVER_URL, "r", "r")
        self.assertEquals(r.status_code, 204, "not deleting devices, server response: %s, response code: %s" % (r.content, r.status_code))



def main():
    unittest.main()

if __name__ == "__main__":
    unittest.main()
