output = """
Interface    IP-Address   Status   Protocol
Gi0/0        10.0.0.1     up       up
Gi0/1        unassigned   down     down
Lo0          192.168.1.1  up       up
"""
output1="""
Codes: I - IGRP derived, R - RIP derived, O - OSPF derived
       C - connected, S - static, E - EGP derived, B - BGP derived
       * - candidate default route, IA - OSPF inter area route
       E1 - OSPF external type 1 route, E2 - OSPF external type 2 route
Gateway of last resort is 131.119.254.240 to network 129.140.0.0
O E2 150.150.0.0 [160/5] via 131.119.254.6, 0:01:00, Ethernet2
E    192.67.131.0 [200/128] via 131.119.254.244, 0:02:22, Ethernet2
O E2 192.68.132.0 [160/5] via 131.119.254.6, 0:00:59, Ethernet2
O E2 130.130.0.0 [160/5] via 131.119.254.6, 0:00:59, Ethernet2
E    128.128.0.0 [200/128] via 131.119.254.244, 0:02:22, Ethernet2
E    129.129.0.0 [200/129] via 131.119.254.240, 0:02:22, Ethernet2
E    192.65.129.0 [200/128] via 131.119.254.244, 0:02:22, Ethernet2
E    131.131.0.0 [200/128] via 131.119.254.244, 0:02:22, Ethernet2
E    192.75.139.0 [200/129] via 131.119.254.240, 0:02:23, Ethernet2
E    192.16.208.0 [200/128] via 131.119.254.244, 0:02:22, Ethernet2
E    192.84.148.0 [200/129] via 131.119.254.240, 0:02:23, Ethernet2
E    192.31.223.0 [200/128] via 131.119.254.244, 0:02:22, Ethernet2
E    192.44.236.0 [200/129] via 131.119.254.240, 0:02:23, Ethernet2
E    140.141.0.0 [200/129] via 131.119.254.240, 0:02:22, Ethernet2
E    141.140.0.0 [200/129] via 131.119.254.240, 0:02:23, Ethernet2
  
"""

output2='{"interfaces": [{"name":"Gi0/0","status":"up","ip":"192.168.1.1"},{"name":"Gi0/1","status":"down","ip":null},{"name":"Gi0/2","status":"up","ip":"10.0.0.1"}]}'

import json

ppp=json.dumps(json.loads(output2), indent=4)
#print(ppp)
r=json.loads(output2)

for i in r['interfaces']:
    if i['status']=='up' and i['ip'] is not None:
        print(i)

def parse_routing_table(output):
    lines=output.strip().splitlines()
    routes = []
    for lin in lines:
        if lin and not lin.startswith('Codes:') and not lin.startswith('Gateway of last resort') :
            parts=lin.split()
            if len(parts) >= 5:
                routes.append({
                    "protocol": parts[0],
                    "network": parts[1],
                    "metric": parts[2].strip('[]'),
                    "next_hop": parts[4].rstrip(',')
                })
    return routes

def parse_interface_status(output):
    lines= output.strip().splitlines()
    interfaces = []
    for line in lines[1:]:
        parts=line.split()
        if len(parts) >= 4:
            if parts[2] == 'up' and parts[3] == 'up':
                interfaces.append({
                    "interface": parts[0],
                    "ip_address": parts[1]
                })
    return interfaces

result = parse_interface_status(output)
print(json.dumps(result))
result1 = parse_routing_table(output1)
print(json.dumps(result1))