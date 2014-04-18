__author__ = 'emmanuel.ankutse'

#This is the Handler for and AXFR session. The mdns-service receives and
#decodes and AXFR request from a client (slave nameserver) then passes it
#on here for the session to be handled
#See section 2.2 of RFC5936 for what is expected of the server in response
#to AXFR request

#First send the SOA. Should have a copy of the question section from the
#client in the question section of this first message fo the response series

#Then send all other Resource Records (not including SOA)
#May leave out the original question on this (these) messages in the series
#As many Resource Records will be sent in message as will fit in message
#and still respect the size limit for tcp message. Old clients that will
#one RR per message are not supported at this point.


#Finally send the SOA. May leave out the original question this time

#ERROR at any point in time will be indicated by sending a single DNS message
#upon detection of error condition with teh response code set to the value
#for the condition. The message must contain a copy of the Question section
#from the original query. This will terminate the AXFR session.

#Also See dns.query.xfr()for client-side initiation of axfr

#TODO: ability to handle multiple AXFR sessions simultaneously - i.e., from
#TODO: different clients as well as from same client. Probably this is handled
#TODO: in the mdns-service? Ref section 4 and 4.1.2 of RFC5936

import dns.query
import dns.zone

def from_server(where, zone_name):
    resp = None
    print 'AXFR zone %s from server %s' % (zone_name, where)
    print
    resp = dns.zone.from_xfr(dns.query.xfr(where, zone_name, rdtype="AXFR"))
    return resp

def to_server(where, zone_name):
    resp = None
    print 'AXFR zone %s TO server %s' % (zone_name, where)
    print
    #TODO: make the call here
    return resp
