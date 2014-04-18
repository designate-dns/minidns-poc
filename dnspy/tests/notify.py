__author__ = 'emmanuel.ankutse'

import unittest
from dnspy import notify

class NotifyTest(unittest.TestCase):
    def test_notify_on_authoritative_zone(self):
        print
        print '--ENTER test_notify_on_authoritative() --'
        zone_name = 'minidnspoc1.com'
        name_server = '198.61.196.44'
        resp = notify.send_notify(zone_name, name_server)
        self.assertIsNotNone(resp, "Response from notify for zone %s is None!" % zone_name)
        print
        print '--- RESPONSE to NOTIFY message ----'
        print resp

    def test_notify_on_NO_authoritative_zone_1(self):
        print
        print '--ENTER test_notify_on_NOT_authoritative_zone_1() --'
        zone_name = "somecrazyzone.com"
        name_server = '198.61.196.44'
        resp = notify.send_notify(zone_name, name_server)
        self.assertIsNotNone(resp, "Response from notify for zone %s is None!" % zone_name)
        print
        print '--- RESPONSE to NOTIFY message ----'
        print resp

    def test_notify_on_NO_authoritative_zone_2(self):
        print
        print '--ENTER test_notify_on_NOT_authoritative_zone_2() --'
        zone_name = '127.in-addr.arpa'
        name_server = '198.61.196.44'
        resp = notify.send_notify(zone_name, name_server)
        self.assertIsNotNone(resp, "Response from notify for zone %s is None!" % zone_name)
        print
        print '--- RESPONSE to NOTIFY message ----'
        print resp

if __name__ == '__main__':
    unittest.main()
