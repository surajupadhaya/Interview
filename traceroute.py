routing_table = {"10.0.0.0/24": "10.0.1.0/24",
    "10.0.1.0/24": "192.168.1.0/24",
    "192.168.1.0/24": "1.1.1.1.1",    # Final IP
    "172.16.0.0/16": "172.17.0.0/16",
    "172.17.0.0/16": "172.16.0.0/16", # Loop!
    "10.5.0.0/16": "10.6.0.0/16"    # Dead End (10.6.0.0/16 not in table)}
}
def get_nexthop(routing_table, destination):
    visited = set()
    current =destination
    while current in routing_table:
        if current in visited:
            return "Loop detected"
        visited.add(current)
        current = routing_table[current]
    return current

    

#destination = get_nexthop(routing_table, "172.16.0.0/16")
destination = get_nexthop(routing_table, "10.5.0.0/16")
print(destination)



'''
if destination in routing_table:
        if "/" not in routing_table[destination]:
            return routing_table[destination]
        else:
            if routing_table[destination] in routing_table:
                if routing_table[routing_table[destination]] in routing_table:
                    return "Loop detected: " + routing_table[destination]
                return routing_table[routing_table[destination]]

    else:
        return None
'''