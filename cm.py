
class SSHConnection:
    def __init__(self, host):
        self.host = host
        self.connected = False

    def __enter__(self):
        print(f"Opening SSH connection to {self.host}")
        self.connected = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing SSH connection to {self.host}")
        self.connected = False
        return False  # don't suppress exceptions

    def run(self, command):
        if not self.connected:
            raise RuntimeError("Not connected")
        print(f"Running: {command}")
        simulate_output = {
            "show version": "Cisco IOS Software, C2960X Software (C2960X-UNIVERSALK9-M), Version 15.2(2)E7, RELEASED",
            "show interfaces": "GigabitEthernet0/1 is up, line protocol is up"
        }
        return simulate_output.get(f"Output of '{command}'")
        return f"Output of '{command}'"


#with SSHConnection("10.0.0.1") as conn:#
 #   output = conn.run("show version")
 #   print(output)

output = SSHConnection("10.0.0.1")
e=output.__enter__()
p=output.run("show version")
print(p)
output.__exit__(None, None, None)
