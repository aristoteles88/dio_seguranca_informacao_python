import ipaddress

ip = "192.168.0.1"
address = ipaddress.ip_address(ip)

print(address + 2000)

ip2 = "192.168.0.100/32"
network = ipaddress.ip_network(ip2, strict=False)
print(network)

for ip in network:
    print(ip)