# Author:Kali Yu
import pywifi
from pywifi import const

# 判断是否已经连接WIFI
def gic():
    # 创建一个无线对象
    wifi = pywifi.PyWiFi()
    # 获取到第一个无线网卡
    ifaces = wifi.interfaces()[0]
    # 打印网卡名称
    # ifaces.name()

    print(ifaces.status())
# gic()

# 扫描附近的WIFI

def bies():
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    # 扫面WiFi
    ifaces.scan()
    # 获取扫描结果
    result = ifaces.scan_results()
    for name in result:
        print(name.ssid)
bies()