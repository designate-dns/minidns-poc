__author__ = 'emmanuel.ankutse'

#This is the Handler for and AXFR session. The mdns-service receives and
#decodes and AXFR request from a client (slave nameserver) then passes it
#on here for the session to be handled
#See section 2.2 of RFC5936 for what is expected of the server in response
#to AXFR request

#First send the SOA. Should have a copy of the question section from the
#client in the question section of this first message of the response series

#Then send all other Resource Records (not including SOA)
#May leave out the original question on this (these) messages in the series
#As many Resource Records will be sent in message as will fit in message
#and still respect the size limit for tcp message. Old clients that will
#one RR per message are not supported at this point.

#Finally send the SOA. May leave out the original question this time

#ERROR at any point in time will be indicated by sending a single DNS message
#upon detection of error condition with the response code set to the value
#for the condition. The message must contain a copy of the Question section
#from the original query. This will terminate the AXFR session.

#Also See dns.query.xfr()for client-side initiation of axfr

#TODO: ability to handle multiple AXFR sessions simultaneously - i.e., from
#TODO: different clients as well as from same client. Probably this is handled
#TODO: in the mdns-service? Ref section 4 and 4.1.2 of RFC5936

import dns.query
import dns.zone
import dns.message

def from_server(where, zone_name):
    resp = None
    print 'AXFR zone %s from server %s' % (zone_name, where)
    print
    resp = dns.zone.from_xfr(dns.query.xfr(where, zone_name, rdtype="AXFR"))
    return resp

def send_non_soa_resource_records(where, zone_name):
    '''Send all resource records except the soa record.

    This may take a series of one or more messages to send the entire
    collection of resource records.
    As many Resource Records will be sent in each message as will fit in the
    message and still respect the size limit for tcp message.
    Old clients that will one RR per message are not supported at this point.

    May leave out the original question on this (these) messages in the series
    '''
    pass

def send_initial_soa_resource_record(where, zone_name):
    '''Send the starting message (the SOA record) for the zone axfr to the
    indicated destination

    Must have a copy of the question section from the client in the
    question section of this message
    '''
    pass

def send_final_soa_resource_record(where, zone_name, client_axfr_request):
    '''Send the terminal message (the SOA record) for the zone axfr to the indicated destination

    Optional to have a copy of the question section from the client in the
    question section of this message
    '''

    #get a skeleton of Message object that already has a copy of the question
    #that is in the request passed in as well as the id. Additionally,
    #sets the basics for doing EDNS and TSIG if necessary
    # (see dns.message.make-response())
    soa_msg = dns.message.make_response(client_axfr_request)
    #set headers
    soa_msg = set_axfr_response_message_headers(client_axfr_request, soa_msg)
    #send the message
    #   TODO: query.tcp might not be the way to go as that
    #   TODO: implies a response is expected
    dns.query.tcp(soa_msg,)


def set_axfr_response_message_headers(client_axfr_request, a_response_msg):
    '''Set headers for messages for the current axfr session

    See section 2.2.1 of RFC 5936
    :rtype : dns.message.Message
    :param client_axfr_request: dns.message.Message
    :param a_response_msg: dns.message.Message
    '''

    #add header values the response message adn return
    assert isinstance(a_response_msg, dns.message.Message)

    #TODO verify that the id and question sections are not None
    #TODO add header values

    return a_response_msg

def handle_axfr_exception(where, zone, error):
    '''Handle any errors that occurs during the axfr session

    ERROR at any point in time will be indicated by sending a single DNS
    message upon detection of error condition with the response code set
    to the value for the condition. The message must contain a copy of
    the Question section from the original query. This will terminate the
     AXFR session.
    '''
    pass

def to_server(where, zone_name):
    resp = None
    print 'AXFR zone %s TO server %s' % (zone_name, where)
    print

    #Send the initial SOA
    print 'Sending initial SOA of the axfr'
    #TODO: put this in try-catch
    send_initial_soa_resource_record(where, zone_name)

    #Send as many messages as it takes to send all other resource records
    print 'Sending all other Resource Records of the axfr'
    #TODO: put this in try-catch
    send_non_soa_resource_records(where, zone_name)

    #Send the final SOA
    print 'Sending the final SOA of the axfr'
    #TODO: put this in try-catch
    send_final_soa_resource_record(where, zone_name)

    print
    return resp
