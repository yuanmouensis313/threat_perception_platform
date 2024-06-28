"""
专门用于资产探测的类
"""
import json
import threading
import winreg

import nmap
import pythoncom
import wmi


class AssetsDetect(threading.Thread):
    def __init__(self, rabbitmq, data):
        super().__init__()
        self.__rabbitmq = rabbitmq
        self.__data = data

    def run(self):
        self.__detect()

    def __detect(self):
        # 进行资产探测

        # 获取探测哪种资产的类型标识
        account = self.__data["account"]
        service = self.__data["service"]
        application = self.__data["application"]
        process = self.__data["process"]

        # 进行类型判断
        if account == 1:
            # 账号探测
            self.__account_detect()
        if service == 1:
            # 服务探测
            self.__service_detect()
        if application == 1:
            # 应用探测
            self.__application_detect()
        if process == 1:
            # 进程探测
            self.__process_detect()

    # 账号探测方法
    def __account_detect(self):
        """
        探测账号
        :return:
        """

        # 创建wmi客户端对象
        # 初始化
        print("开始探测账号数据..........")
        pythoncom.CoInitialize()
        c = wmi.WMI()
        account_list = []
        # 获取所有用户
        for user in c.Win32_UserAccount():
            user_dict = {
                "mac": self.__data['mac'],
                "name": user.Name,
                "full_name": user.FullName,
                "sid": user.SID,
                "sid_type": user.SIDType,
                "status": user.Status,
                "disabled": user.Disabled,
                "lockout": user.Lockout,
                "password_changeable": user.PasswordChangeable,
                "password_expires": user.PasswordExpires,
                "password_required": user.PasswordRequired,
            }
            account_list.append(user_dict)
        # 去初始化
        pythoncom.CoUninitialize()
        # 转换成JSON字符串
        account_data = json.dumps(account_list)
        # 发送给队列
        self.__rabbitmq.produce_account_data(account_data)
        print("探测账号数据结束！")

    # 服务探测的方法
    def __service_detect(self):
        """
        探测服务
        :return:
        """

        print('开始探测服务数据......!')
        # 创建一个扫描仪对象
        nm = nmap.PortScanner()
        # 扫描目标主机
        nm.scan(hosts='127.0.0.1', arguments='-sTV')  # 指定扫描端口范围
        # 获取扫描结果
        state = nm.all_hosts()
        # 装最终结果的
        res_list = []
        if state:
            for host in nm.all_hosts():
                for proto in nm[host].all_protocols():
                    lport = nm[host][proto].keys()
                    for port in lport:
                        # 接收nmap扫描结果
                        nmap_res = {
                            'mac': self.__data['mac'],
                            'protocol': proto,
                            'port': port,
                            'state': nm[host][proto][port]['state'],
                            'name': nm[host][proto][port]['name'],
                            'product': nm[host][proto][port]['product'],
                            'version': nm[host][proto][port]['version'],
                            'extrainfo': nm[host][proto][port]['extrainfo']}
                        res_list.append(nmap_res)
        # 转换成JSON字符串
        res_json = json.dumps(res_list)
        # 发送到队列
        self.__rabbitmq.produce_service_data(res_json)
        print("服务数据探测结束！")


    # 进程探测的方法
    def __process_detect(self):

        # 获取进程信息
        # 初始化
        print('开始探测进程数据......!')
        pythoncom.CoInitialize()
        c = wmi.WMI()
        process_list = []
        for process in c.Win32_Process():
            process_info = {
                'mac': self.__data['mac'],
                'pid': process.ProcessId,
                'ppid': process.ParentProcessId,
                'name': process.Name,
                'cmd': process.CommandLine,
                'priority': process.Priority,
                'description': process.Description,
            }
            process_list.append(process_info)
        # 去初始化
        pythoncom.CoUninitialize()
        # 转换成JSON
        process_data = json.dumps(process_list)
        # 发送到队列
        self.__rabbitmq.produce_process_data(process_data)
        print("进程数据探测结束！")


    # 应用探测的方法
    def __application_detect(self):

        # 从注册表获取软件信息
        print('开始探测app数据......!')
        registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                      r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall')
        software_list = []
        # 获取软件数量
        number = winreg.QueryInfoKey(registry_key)[0]
        for i in range(number):
            try:
                sub_key_name = winreg.EnumKey(registry_key, i)
                sub_key = winreg.OpenKey(registry_key, sub_key_name)
                software = {}
                try:
                    software['mac'] = self.__data['mac']
                    software['display_name'] = winreg.QueryValueEx(sub_key,
                                                                   'DisplayName')[0]
                    software['install_location'] = winreg.QueryValueEx(sub_key,
                                                                       'InstallLocation')[0]
                    software['uninstall_string'] = winreg.QueryValueEx(sub_key,
                                                                       'UninstallString')[0]
                    software_list.append(software)
                except WindowsError:
                    continue
            except WindowsError:
                break
        # 转换成JSON字符串
        app_data = json.dumps(software_list)
        # 发送到队列
        self.__rabbitmq.produce_application_data(app_data)
        print("app数据探测结束！")

