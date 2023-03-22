# -*- coding: utf-8 -*-
"""
@Time    : 2023/3/22 22:00
@Author  : WJC
@File    : RealTimeConNet.py
@Desc    : 
"""

import os
import time
import pywifi
from pywifi import const
import psutil


def wifi_connect_status(iface):
    '''
    判断此时的WIFI连接状态
    :param iface: 传入pywifi获取的电脑网卡
    :return: 1 | 0
    '''
    if iface.status() in [const.IFACE_CONNECTED, const.IFACE_INACTIVE]:
        print("wifi connected!")
        return 1
    else:
        print("wifi not connected!")
    return 0



def ifProcessRunning(process_name):
    '''
    判断某个程序是否在运行
    原理：获取正在运行程序的pid，通过pid获取程序名，再按程序名进行判断
    :param process_name: 程序名字符串
    :return: True | False
    '''
    pl = psutil.pids()
    for pid in pl:
        if psutil.Process(pid).name() == process_name:
            return True
    else:
        return False


def start_xrk():
    '''
    判断向日葵是否已经启动，如果已经启动不做任何操作，如果没有启动则启动软件
    :return: None
    '''
    while True:
        if ifProcessRunning('SunloginClient.exe'):
            print('--向日葵已启动')
            break
        else:
            cmd3 = r'call start /min "n" "D:\向日葵\SunloginClient\SunloginClient.exe"'
            # cmd4 = r'taskkill /f /im SunloginClient.exe'
            # print('--kill 向日葵软件')
            # os.system(cmd4)
            print('--启动向日葵软件')
            os.system(cmd3)
            time.sleep(3)


def con_wifi(wifi_name):
    '''
    连接指定wifi
    :param wifi_name:需要连接的wifi
    :return: None
    '''
    cmd2 = r'netsh wlan connect name="{wifi_name}"'.format(wifi_name=wifi_name)
    print('--外网链接失败，重新连接')
    print('--执行命令：连接WiFi')
    os.system(cmd2)
    print('--睡眠10s...')
    time.sleep(10)


def main():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # acquire the first Wlan card,maybe not
    while True:
        if wifi_connect_status(iface):
            print('--外网连接正常')
            start_xrk()
            print('=====================================================')
            time.sleep(5)
        else:
            wifi_name = '大熊猫基地'
            con_wifi(wifi_name)
            print('=====================================================')


if __name__ == '__main__':
    main()