__author__ = 'emmanuel.ankutse'

"""NOTES:
dns.message is for higher level control message generation
dns.renderer is for lower level and finer control over message generation
dns.message calls dns.renderer
??dns.resolver is for transmitting the message??
"""

import dns.message
import dns.resolver
import dns.zone


def send_notify(zone_name, destination):

    """ Construct and send a NOTIFY to an (all) axfr clients name servers
    (in the notify set)
    """

    """
    TODO: create the notify message here by inserting the name of the
    incoming zone name in the message

    RFC 1995 section 4.5 Zone has Updated on Primary Master:

    Primary master sends a NOTIFY request to all servers named in Notify
    Set.  The NOTIFY request has the following characteristics:

    query ID:   (new)
    op:         NOTIFY (4)
    resp:       NOERROR
    flags:      AA
    qcount:     1
    qname:      (zone name)
    qclass:     (zone class)
    qtype:      T_SOA
    """

    """JUST THINKING HERE:
    Put it in text and take advantage of dns.message.from_text() to create
    the object
    """

    """TODO: now transmit the wire format message
    """
    """
    answers = dns.resolver.query('nominum.com', 'MX')
    for rdata in answers:
        print 'Host', rdata.exchange, 'has preference', rdata.preference
    print

    answers = dns.resolver.query('rackspace.com', 'A')
    for rdata in answers:
        print 'rackspace.com has address', rdata
    print

    answers = dns.resolver.query('google.com', 'A')
    print 'google.com has addresse(s):'
    for rdata in answers:
        rdata.address
    print

    answers = dns.resolver.query('rackspace.com', 'NS')
    print 'rackspace.com has nameserver(s):'
    for rdata in answers:
        print rdata
    print

    answers = dns.resolver.query('rackspace.com', 'SOA')
    print 'rackspace.com SOA:'
    for rdata in answers:
        print rdata
    print
    """
    notify_msg = dns.message.make_query(zone_name, 'SOA') #Question section QNAME, QTYPE=SOA, QCLASS=IN
    notify_msg.flags = 0 #clear flags
    notify_msg.set_opcode(dns.opcode.NOTIFY) #Set Header - Opcode=NOTIFY (4)
    notify_msg.set_rcode(dns.rcode.NOERROR) #Set Header - Rcode=NOERROR (0)
    notify_msg.flags = notify_msg.flags | dns.flags.AA #set AA bit
    print '--- NOTIFY QUERY message ---'
    print notify_msg
    print

    timeout = 30 #check RFC1996 for recommended timeout
    response = dns.query.udp(notify_msg, destination, timeout, ignore_unexpected=True)
    return response

#Possible response code (rcode): NOERROR, NOTAUTH