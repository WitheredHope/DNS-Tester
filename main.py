'''
MLH Local Hack Day 01/12/2018
Tom Atkins & Josh D-Kemp
DNS Update Checker
'''

import dns.resolver

my_resolver = dns.resolver.Resolver()

# 8.8.8.8 is Google's public DNS server
my_resolver.nameservers = ['8.8.8.8']

answer = my_resolver.query('google.com')

print(str(answer[0]))
