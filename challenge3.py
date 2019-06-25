#!/usr/bin/env python3

hosts = [{"server": "North", "ip": "10.1.2.3"}, {"server": "South", "ip": "10.4.5.6"}, {"server": "West", "ip": "10.7.8.9"}]

print(hosts)

hosts.append({"server": "East", "ip": "10.10.11.12"})
print(hosts)
print(hosts[0]["server"], hosts[0]["ip"])
print(hosts[1]["server"], hosts[0]["ip"])
print(hosts[2]["server"], hosts[0]["ip"])
print(hosts[3]["server"], hosts[0]["ip"])

# this is format version
#print('The server is {} the ip is {}'.format(host0=[0]["server"], hosts[0]["ip"]))

# for loop in dictionaries
for info in hosts:
    print(info['server'], info['ip'])

