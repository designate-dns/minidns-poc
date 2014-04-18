__author__ = 'emmanuel.ankutse'

import unittest
from dnspy import axfr

class ClientSideAXFRTest(unittest.TestCase):
    def test_existing_zone_AXFR_from_server_1(self):
        #Test dns.query.xfr() - client side.
        name_server="198.61.196.44"
        zone_name="minidnspoc1.com"
        zone = axfr.from_server(name_server, zone_name)
        self.assertIsNotNone(zone, "Response from AXFR for zone %s is None!" % zone_name)
        print '-- AXFR Response ---'
        names = zone.nodes.keys()
        names.sort()
        for n in names:
            print zone[n].to_text(n)
        print

    def test_existing_zone_AXFR_from_server_2(self):
        #Test dns.query.xfr() - client side.
        name_server="198.61.196.44"
        zone_name='127.in-addr.arpa'
        zone = axfr.from_server(name_server, zone_name)
        self.assertIsNotNone(zone, "Response from AXFR for zone %s is None!" % zone_name)
        print '-- AXFR Response ---'
        names = zone.nodes.keys()
        names.sort()
        for n in names:
            print zone[n].to_text(n)
        print

if __name__ == '__main__':
    unittest.main()
