import dns.resolver

my_resolver = dns.resolver.Resolver()

# 8.8.8.8 is Google's public DNS server
my_resolver.nameservers = ['8.8.8.8']

answer = my_resolver.query('google.com')
'testing to make sure i can still commit without things going tits up'
