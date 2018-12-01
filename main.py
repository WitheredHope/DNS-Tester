'''
MLH Local Hack Day 01/12/2018
Tom Atkins & Josh D-Kemp
DNS Update Checker
'''

import dns.resolver

def get_ip(domain, dnsIP):
    my_resolver = dns.resolver.Resolver()
    my_resolver.nameservers = [dnsIP]
    try:
        answer = my_resolver.query(domain)
        return str(answer[0])
    except:
        return None


def check_if_updated(domain, dnsIP, oldIP = None):
    '''
    takes the domain and dns being tested
    if oldIP is given returns true if the ip given by the dns is different
    otherwise returns true if the domain resolves
    '''
    ip = get_ip(domain, dnsIP)

    if not oldIP:
        return not not ip

    return ip != oldIP

print(check_if_updated('boltandcounter.co.uk','8.8.8.8','82.15.145.212'))
