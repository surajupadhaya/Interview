import re
ip_list = ['260.36.145.29','95.253.17.166','228.132.182.39','71.65.77.93','221.91.30.129','15.110.72.161','137.28.154.76','253.77.48.43','120.74.246.138','227.164.180.165']

pattern = re.compile(r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$')

for ip in ip_list:
    if pattern.match(ip):
        parts=ip.split('.')
        for part in parts:
            if int(part) < 0 or int(part) > 255:
                print(f"{ip} is NOT a valid IP address.")
                break
        else:
            print(f"{ip} is a valid IP address.")
    else:
        print(f"{ip} is NOT a valid IP address.")
