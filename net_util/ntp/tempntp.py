import ntplib
from time import ctime
import argparse

parser = argparse.ArgumentParser( description="test-ntp.py - Test a set of IP addresses for NTP " )
parser.add_argument("--ip", action="append", help="IP address to check for NTP")
a = parser.parse_args()
if a.ip is not None:
    c = ntplib.NTPClient()
    for ip in a.ip:
        try:
            response = c.request(ip)
            print("Response: ", str(response))
            if response:
                print (ip+" NTP Active "+ ctime(response.tx_time))
        except:
            # print("Exception block ...")
            print (ip+" NTP Deactivated")
else:
    parser.print_help()
    exit(1)