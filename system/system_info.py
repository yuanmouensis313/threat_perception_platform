# coding=utf-8
import json
import math
import subprocess
import uuid
import socket
import platform

import psutil


class SystemInfo(object):
    """
    获取系统信息的类：主机名，主机Ip，mac地址，操作系统相关信息（os_name,version,架构），CPU相关信息，内存相关信息
    """

    # 构造器
    def __init__(self):
        # 加上下划线，无下划线表示public，单下划线表示protected，双下划线表示private
        # 初始化网络设备的主机名，为空字符串表示未设置
        self.__hostname = ""

        # 初始化网络设备的IP地址，为空字符串表示未设置
        self.__ip = ""

        # 初始化网络设备的MAC地址，为空字符串表示未设置
        self.__mac = ""

        # 初始化操作系统名称，为空字符串表示未设置
        self.__os_name = ""

        # 初始化操作系统版本，为空字符串表示未设置
        self.__os_version = ""

        # 初始化操作系统架构，为空字符串表示未设置
        self.__os_arch = ""

        # 初始化操作系统类型属性，用于存储设备的操作系统类型
        self.__os_type = ""

        # 初始化CPU属性，用于存储设备的CPU型号
        self.__cpu = ""

        # 初始化内存属性，用于存储设备的内存大小
        self.__ram = ""

    # 获取mac地址的方法
    @property
    def mac(self):
        """
        获取设备的MAC地址。

        该属性用于获取设备的物理地址，MAC地址是设备在局域网中唯一标识符。
        通过这个属性，可以方便地获取到设备的MAC地址，而不需要直接访问私有属性。

        Returns:
            str: 设备的MAC地址。
        """
        return self.__mac


    def __get_hostname(self):
        """
        获取当前机器的主机名。

        该方法通过调用socket库的gethostname函数来获取当前机器的主机名，并将结果存储在实例变量__hostname中。
        主机名是一个字符串，用于唯一标识网络上的设备。

        Returns:
            无显式返回值，但将主机名存储在实例变量__hostname中。
        """
        self.__hostname = socket.gethostname()

    def __get_ip(self):
        """
        获取当前设备的IP地址。

        由于Python的socket模块不提供直接获取本地IP地址的方法，因此通过连接一个已知的远程地址（如114.114.114.114）
        并查询返回的socket信息来获取本地IP地址。

        连接过程使用UDP协议，因为它比TCP协议更快，且足够用于这个简单的任务。
        """
        # 创建一个IPv4的UDP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # 连接到一个已知的远程地址和端口，以此来获取本地IP地址
        s.connect(("114.114.114.114", 80))

        # 从socket对象中获取本地IP地址
        self.__ip = s.getsockname()[0]

        # 关闭socket对象，释放资源
        s.close()

    def __get_mac(self):
        """
        获取机器的MAC地址。

        由于Python标准库中没有直接的方法来获取MAC地址，这里通过UUID模块获取本地机器的节点ID，
        并将其格式化为MAC地址的字符串格式。UUID模块的getnode方法返回一个随机的节点ID，如果系统支持，
        它会返回一个真实的硬件地址。

        返回:
            str: 格式化后的MAC地址字符串，以冒号分隔。
        """
        # 使用UUID模块获取本地机器的节点ID，并将其转换为MAC地址格式
        self.__mac = ':'.join(("%012X" % uuid.getnode())[i:i + 2] for i in range(0, 12, 2))

    def __get_system_info(self):
        """
        私有方法，用于获取系统的详细信息。

        这些信息包括操作系统名称、操作系统类型、操作系统版本和操作系统架构。
        使用platform模块和subprocess模块来获取和处理这些信息。
        """

        # 使用platform.system()获取操作系统名称
        # 获取操作系统类型
        self.__os_name = platform.system()

        # 使用wmic命令行工具获取操作系统类型
        # 执行wmic命令获取操作系统名称
        process = subprocess.Popen(['wmic', 'os', 'get', 'Caption'], stdout=subprocess.PIPE)
        # 从wmic命令输出中获取操作系统类型字符串
        output, _ = process.communicate()
        # 解码wmic命令的输出，从GBK编码转换为字符串，并去除首尾空格
        self.__os_type = output.strip().decode('GBK').split('\n')[1]

        # 使用platform.version()获取操作系统版本
        # 获取操作系统版本
        self.__os_version = platform.version()

        # 使用platform.architecture()获取操作系统架构
        # 获取操作系统架构
        self.__os_arch = platform.architecture()[0]

    def __get_cpu_info(self):
        """
        通过WMIC命令行工具获取CPU名称。

        使用subprocess.Popen执行WMIC命令，捕获输出以获取CPU信息。
        由于输出以UTF-8编码，需要进行解码处理。
        最终提取并保存CPU名称。
        """
        # 使用wmic命令获取cpu名称
        # 获取cpu信息
        process = subprocess.Popen(['wmic', 'cpu', 'get', 'name'], stdout=subprocess.PIPE)
        # 与进程通信，获取输出和错误信息，这里只关注输出
        output, _ = process.communicate()
        # 处理输出，去除首尾空格，解码为UTF-8，并分割为列表，取第二行（第一行为标题行）
        self.__cpu = output.strip().decode('utf-8').split('\n')[1]

    def __get_ram_info(self):
        """
        获取系统的RAM信息，计算总内存大小，并以吉字节（GB）为单位存储。

        由于内存大小通常以字节为单位给出，这里通过连续除以1024三次，将字节转换为吉字节。
        使用math.ceil函数确保向上取整，这样可以更保守地估计可用内存大小。

        属性:
        __ram: 私有属性，存储系统总内存大小（以GB为单位）。
        """
        self.__ram = math.ceil(psutil.virtual_memory().total / 1024 / 1024 / 1024)

    def get_system_info(self):
        """
        获取系统的详细信息。
        """
        self.__get_hostname()
        self.__get_ip()
        self.__get_mac()
        self.__get_system_info()
        self.__get_cpu_info()
        self.__get_ram_info()

        # 返回数据
        return json.dumps({
            "hostname": self.__hostname,
            "ip": self.__ip,
            "mac": self.__mac,
            "os_name": self.__os_name,
            "os_type": self.__os_type,
            "os_version": self.__os_version,
            "os_arch": self.__os_arch,
            "cpu": self.__cpu,
            "ram": self.__ram
        })
