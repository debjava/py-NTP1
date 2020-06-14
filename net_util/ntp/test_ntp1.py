import ntplib

ntpClient = ntplib.NTPClient()


def isValidNTP(ipAddress):
    checkFlag = False
    try:
        response = ntpClient.request(ipAddress)
        if response:
            checkFlag = True
    except:
        checkFlag = False

    return checkFlag

if __name__ == "__main__":
    pass
    # ipAddres = "5.103.139.163" # Valid
    ipAddres = "0.pool.ntp.org" # Valid
    ipAddres = "10.10.20.9" # Invalid
    ntpFlag = isValidNTP(ipAddres)
    value = "{} - {}".format(ipAddres, str(ntpFlag))
    print(value)
