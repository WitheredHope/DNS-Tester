'''
MLH Local Hack Day 01/12/2018
Tom Atkins & Josh D-Kemp
DNS Update Checker
'''
import dns.resolver

#DNS dictionary
primaryDNS = {'Google' : '8.8.8.8', 'Comodo Secure DNS' : '8.26.56.26', 'FreeDNS' : '37.235.1.174', 'Alternate DNS' : '198.101.242.72', 'Dyn' : '216.146.35.35', 'DNS.WATCH' : '84.200.69.80', 'Cloudflare' : '1.1.1.1', 'GreenTeamDNS' : '81.218.119.11', 'Norton ConnectSafe' : '199.85.126.10', 'Hurricane Electric' : '74.82.42.42', 'Level3' : '209.244.0.3', 'Neustar Security' : '156.154.70.1', 'OpenNIC' : '23.94.60.240', 'OpenDNS Home' : '208.67.222.222', 'Quad9' : '9.9.9.9', 'Yandex.DNS' : '77.88.8.8', 'SafeDNS' : '195.46.39.39', 'puntCAT' : '109.69.8.51', 'Verisign' : '64.6.46.6', 'UncensoredDNS' : '91.239.100.100'}
secondaryDNS = {'Google' : '8.8.4.4', 'Comodo Secure DNS' : '8.20.247.20', 'FreeDNS' : '37.245.1.177', 'Alternate DNS' : '23.253.163.53', 'Dyn' : '216.146.36.36', 'DNS.WATCH' : '84.200.70.40', 'Cloudflare' : '1.0.0.1', 'GreenTeamDNS' : '209.88.198.133', 'Norton ConnectSafe' : '199.85.127.10', 'Level3' : '209.244.0.4', 'Neustar Security' : '156.154.71.1', 'OpenNIC' : '128.52.130.209', 'OpenDNS Home' : '208.67.220.220', 'Quad9' : '149.112.122.122', 'Yandex.DNS' : '77.88.8.1', 'SafeDNS' : '195.46.39.40', 'Verisign' : '64.6.65.6', 'UncensoredDNS' : '89.233.43.71'}

#get IP from a domain & specified DNS
def get_ip(domain, dnsIP):
    my_resolver = dns.resolver.Resolver()
    my_resolver.nameservers = [dnsIP]
    try:
        answer = my_resolver.query(domain)
        return str(answer[0])
    except:
        return None

#checks if an IP on a specified doomain and DNS has changed
def check_if_updated(domain, dnsName, dnsIP, oldIP = None):
    '''
    takes the domain and dns being tested
    if oldIP is given returns true if the ip given by the dns is different
    otherwise returns true if the domain resolves
    '''
    ip = get_ip(domain, dnsIP)

    if not oldIP:
        print("For DNS: {} (IP: {}), domain: {} has been updated to the new IP address.".format(dnsName, dnsIP, domain))
        return not not ip
    else:
        print("For DNS '{}' (IP: {}), domain: '{} has not been updated to the new IP address.".format(dnsName, dnsIP, doomain))
    return ip != oldIP

#cycle through primary DNSs
def check_primary_DNS_updated(domain, oldIP = None):
    for item in primaryDNS:
        item.split()
        check_if_updated(domain, item, primaryDNS[item], oldIP)

#cylce through secondary DNSs
def check_secondary_DNS_updated(domain, oldIP = None):
    for item in secondaryDNS:
        check_if_updated(domain, item, secondaryDNS[item], oldIP)

#cycle through all DNS
def check_all_DNS_updated(domain, oldIP = None):
    check_primary_DNS_updated(domain, oldIP = None)
    check_secondary_DNS_updated(domain, oldIP = None)

#tested
check_all_DNS_updated('boltandcounter.co.uk','82.15.145.212')
