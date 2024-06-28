# coding:utf-8
# import json
#
# # import wmic
#
# # # 获取主机名
# # import socket
# # print("主机名:" + socket.gethostname())
# #
# # # 获取ip
# # import socket
# # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# # s.connect(("114.114.114.114", 80))
# # print("ip:" + s.getsockname()[0])
# # s.close()
# #
# # # 获取mac地址
# # import uuid
# #
# # print("mac:" + ':'.join(("%012X" % uuid.getnode())[i:i + 2] for i in range(0, 12, 2)))
# #
# # # 获取操作系统相关信息
# # import platform
# # import subprocess
# #
# # # 获取操作系统类型
# # system_type = platform.system()
# # print("操作系统类型：", system_type)
# #
# # # 执行wmic命令获取操作系统名称
# # process = subprocess.Popen(['wmic', 'os', 'get', 'Caption'],
# # stdout=subprocess.PIPE)
# # output, _ = process.communicate()
# # # 打印结果
# # print("操作系统名称：", output.strip().decode('GBK').split('\n')[1])
# #
# # # 获取操作系统版本
# # print("操作系统版本：", platform.version())
# #
# # # 获取操作系统架构
# # print("操作系统架构：", platform.architecture()[0])
# #
# # # 获取cpu信息
# # import subprocess
# #
# # process = subprocess.Popen(['wmic', 'cpu', 'get', 'name'],
# # stdout=subprocess.PIPE)
# # output, _ = process.communicate()
# # print("cpu:" + output.strip().decode('utf-8').split('\n')[1])
# #
# # # 获取内存信息
# # import math
# #
# # import psutil as psutil
# #
# # print("内存:", math.ceil(psutil.virtual_memory().total / 1024 / 1024 / 1024))
#
# # 账号探测测试
# import pythoncom
# import wmi
# print("开始探测账号数据..........")
# pythoncom.CoInitialize()
# c = wmi.WMI()
# account_list = []
#
# # 获取所有用户
# for user in c.Win32_UserAccount():
#     user_dict = {
#         "name": user.Name,
#         "full_name": user.FullName,
#         "sid": user.SID,
#         "sid_type": user.SIDType,
#         "status": user.Status,
#         "disabled": user.Disabled,
#         "lockout": user.Lockout,
#         "password_changeable": user.PasswordChangeable,
#         "password_expires": user.PasswordExpires,
#         "password_required": user.PasswordRequired,
#     }
#     account_list.append(user_dict)
# # 去初始化
# pythoncom.CoUninitialize()
# # 转换成JSON字符串
# account_data = json.dumps(account_list)
# print(account_data)
import re
# # 应用探测测试
# import winreg
#
# # 从注册表获取软件信息
# print('开始探测app数据......!')
# registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
#                               r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall')
# # 获取软件数量
# number = winreg.QueryInfoKey(registry_key)[0]
# print("软件数量为：" + str(number))
#
# software_list = []
# for i in range(number):
#     try:
#         sub_key_name = winreg.EnumKey(registry_key, i)
#         sub_key = winreg.OpenKey(registry_key, sub_key_name)
#         software = {}
#         try:
#             software['display_name'] = winreg.QueryValueEx(sub_key,
#                                                            'DisplayName')[0]
#             software['install_location'] = winreg.QueryValueEx(sub_key,
#                                                                'InstallLocation')[0]
#             software['uninstall_string'] = winreg.QueryValueEx(sub_key,
#                                                                'UninstallString')[0]
#             software_list.append(software)
#         except WindowsError:
#             continue
#     except WindowsError:
#         break
# app_data = json.dumps(software_list)
# print(app_data)

# # 补丁探测测试
# import json
# import pythoncom
# import wmi
# print("开始补丁安全发现......!")
# # 初始化
# pythoncom.CoInitialize()
# # 创建WMI客户端
# c = wmi.WMI()
# # 获取补丁信息
# hotfixes = c.query("SELECT HotFixID FROM Win32_QuickFixEngineering")
# # 组装补丁ID
# hotfix_list = []
# for hotfix in hotfixes:
#     data = {
#         'hotfixId': hotfix.HotFixID
#     }
#     hotfix_list.append(data)
# # # 去初始化
# pythoncom.CoUninitialize()
# # 转换成JSON数据
# data = json.dumps(hotfix_list)
# print(hotfix_list)
# print("补丁安全发现结束")

# # 弱密码测试
# from impacket.examples.utils import parse_target
# from impacket.smbconnection import SMBConnection
# def smb_login():
#     # [[domain/]username[:password]@]<targetName or address>
#     target = 'test1:123123@127.0.0.1'
#     domain, username, password, address = parse_target(target)
#     target_ip = address
#     domain = ''
#     lmhash = ''
#     nthash = ''
#     try:
#         smbClient = SMBConnection(address, target_ip, sess_port=int(445))
#         smbClient.login(username, password, domain, lmhash, nthash)
#         print("登录成功！")
#     except Exception as e:
#         print(e)
#         print("登录失败!")
#
# smb_login()

# # 系统时间是否一致测试
# import ntplib
# from time import ctime
# from future.backports.datetime import timezone, timedelta
# from datetime import datetime
# from zoneinfo import ZoneInfo
#
#
# def get_server_time():
#     ntp_server = 'ntp7.aliyun.com'
#     c = ntplib.NTPClient()
#     response = c.request(ntp_server)
#     # 将NTP时间戳转换为datetime对象
#     ntptime = datetime.fromtimestamp(response.tx_time, timezone.utc)
#
#     # 如果需要，可以将UTC时间转换为本地时间
#     local_time = ntptime.astimezone()
#
#     return local_time
#
# def get_local_time():
#     # 获取当前时间并设置为指定时区（例如，北京时间）
#     beijing_tz = ZoneInfo('Asia/Shanghai')
#     return datetime.now(beijing_tz)
#
# def compare_times():
#     server_time = get_server_time()
#     local_time = get_local_time()
#     print("服务器时间：" + str(server_time))
#     print("本地时间：" + str(local_time))
#     if server_time:
#         time_diff = abs(server_time - local_time)
#         max_allowed_diff = timedelta(seconds=5)  # 定义一个可以接受的最大时间差，
#         if time_diff <= max_allowed_diff:
#             print("系统时间一致")
#             print("差值为:" + str(time_diff))
#         else:
#             print("系统时间不一致")
#             print("差值为:" + str(time_diff))
#
# compare_times()

# # 探测主机的路由转发功能是否开启
# import subprocess
# def check_routing_enabled():
#     try:
#         # 执行 netsh 命令来获取路由转发的状态
#         result = subprocess.run(['netsh', 'interface', 'ipv4', 'show', 'interface'], capture_output=True, text=True,
#                                 timeout=10)
#
#         # 检查输出中是否包含 "Forwarding" 字段
#         output_lines = result.stdout.splitlines()
#         for line in output_lines:
#             if "Forwarding" in line:
#                 status = line.split()[-1].strip()
#                 return status.lower() == "enabled"
#
#         # 如果未找到 "Forwarding" 字段，默认返回 False
#         return False
#
#     except Exception as e:
#         print(f"Error checking routing status: {e}")
#         return False
#
# # 测试函数
# def run():
#     routing_enabled = check_routing_enabled()
#     if routing_enabled:
#         print("Routing is enabled.")
#     else:
#         print("Routing is not enabled or could not be determined.")
#
# run()

# # 网卡是否处于混杂模式检测
# import subprocess
# import re
#
#
# def check_promiscuous_mode(interface_name):
#     # Windows系统检查混杂模式的命令
#     command = f'netsh interface show interface name="{interface_name}"'
#     try:
#         # 执行命令并获取输出
#         output = subprocess.check_output(command, shell=True, encoding='GBK')
#
#         # 使用正则表达式查找状态行
#         pattern = r'Status\s*:\s*(\w+)'
#         match = re.search(pattern, output, re.IGNORECASE)
#         if match:
#             status = match.group(1).strip().lower()
#             # 检查状态是否为"enabled"
#             if status == 'enabled':
#                 return True
#             else:
#                 return False
#         else:
#             return False
#     except subprocess.CalledProcessError as e:
#         print(f'Error: {e}')
#         return False
#
#
# def get_all_interfaces():
#     try:
#         # 使用wmic命令获取所有网络接口的信息
#         command = 'wmic nic get NetConnectionID /value'
#         output = subprocess.check_output(command, shell=True, encoding='GBK')
#
#         # 解析输出，获取所有接口名称
#         interface_names = []
#         lines = output.strip().split('\n')
#         for line in lines:
#             if line.startswith('NetConnectionID='):
#                 interface_names.append(line.split('=')[1].strip())
#
#         return interface_names
#     except subprocess.CalledProcessError as e:
#         print(f'Error: {e}')
#         return []
#
#
# # 获取所有网卡名称
# interface_names = get_all_interfaces()
#
# # 遍历所有网卡，检查混杂模式
# for interface_name in interface_names:
#     if interface_name != '':
#         is_promiscuous_mode = check_promiscuous_mode(interface_name)
#         if is_promiscuous_mode:
#             print(f'网卡 {interface_name} 处于混杂模式。')
#         else:
#             print(f'网卡 {interface_name} 未处于混杂模式。')

# # 日志查询
# # coding=utf-8
# # Author: HSJ
# # 2024/6/20 14:03
# from Evtx import PyEvtxParser
# import re
# import html
# from xml.dom import minidom
# def get_log_info(event_path, event_id_to_filter=None):
#     """
#     过滤自己想要的日志
#     :param event_path: 日志的路径
#     :param event_id_to_filter: 过滤的日志ID, 如果为None，则返回所有日志
#     :return:
#     """
#     # 创建一个EvtxParser对象来读取文件
#     parser = PyEvtxParser(event_path)
#     pattern = re.compile(r'<EventID.*?(\d+)</EventID>')
#     # 给一个容器，装最终的事件
#     event_list = []
#     # 遍历日志条目，筛选出特定事件ID的日志
#     for record in parser.records():
#         # print(record)
#         xml_data = record['data']
#         res = re.findall(pattern, xml_data)
#         event_id = int(res[0])
#         if event_id_to_filter is not None and event_id == event_id_to_filter:
#             r = {}
#             r['event_id'] = event_id
#             r['timestamp'] = record['timestamp']
#             xml_doc = minidom.parseString(xml_data)
#             data = xml_doc.getElementsByTagName('Data')
#             for d in data:
#                 try:
#                     name = d.getAttribute('Name')
#                     value = html.unescape(d.childNodes[0].data)
#                     r[name] = value
#                 except Exception as e:
#                     pass
#             event_list.append(r)
#         elif event_id_to_filter is None:
#             # 返回所有的日志
#             r = {}
#             r['event_id'] = event_id
#             r['timestamp'] = record['timestamp']
#             xml_doc = minidom.parseString(xml_data)
#             data = xml_doc.getElementsByTagName('Data')
#             for d in data:
#                 try:
#                     name = d.getAttribute('Name')
#                     value = html.unescape(d.childNodes[0].data)
#                     r[name] = value
#                 except Exception as e:
#                     pass
#             event_list.append(r)
#     return event_list
#
# if __name__ == '__main__':
#     # # 指定EVTX文件路径
#     # path = r"C:\Windows\system32\winevt\Logs\System.evtx"
#     # event_list = get_log_info(path, 7045)
#     # for event in event_list:
#     #     print(event)
#
#     """
#     常见的安全事件ID：
#     4624 - 成功登录事件，表示用户成功登录系统。
#     4625 - 登录失败事件，表示用户尝试但未能成功登录系统。
#     4634 - 注销事件，表示用户注销系统。
#     4647 - 用户注销事件，表示用户通过重新启动或关闭计算机来注销系统。
#     4720 - 创建用户事件，表示新用户帐户已创建。
#     4722 - 启用用户帐户事件，表示禁用的用户帐户已被启用
#     4723 - 更改用户密码事件，表示用户密码已更改。
#     4724 - 创建安全组事件，表示新安全组已创建。
#     4728 - 成功授权事件，表示用户获得了指定对象的权限。
#     4738 - 设置用户密码事件，表示用户密码已更改或重置。
#     常见的系统事件ID：
#     1074 - 通过这个事件ID查看计算机的开机、关机、重启的时间以及原因和注释。
#     6005 - 表示计算机日志服务已启动，如果出现了事件ID为6005，则表示这天正常启动了系统。
#     6006 - 系统关闭
#     6008 - 非正常关机
#     6009 - 系统已经重新启动
#     6013 - 系统已经重新启动，原因是操作系统版本升级
#     7036 - 服务状态更改
#     7040 - 启动或停止监视者通知
#     7045 - 安装服务
#     日志清除事件：
#     1102 - 这个事件ID记录所有审计日志清除事件，当有日志被清除时，出现此事件ID。
#     """
#
#     # 获取安全日志的键
#     path = r"F:\Security.evtx"
#     ids = [4624, 4625, 4634, 4647, 4720, 4722, 4723, 4724, 4728, 4738]
#     event_keys = []
#
#     # 遍历查询
#     for id in ids:
#         event_list = get_log_info(path, id)
#         print(event_list[0])
#         # 说明有数据
#         if len(event_list) > 0:
#             # 将键添加到列表中(不重复)
#             for key in event_list[0].keys():
#                 if key not in event_keys:
#                     event_keys.append(key)
#
#     print(event_keys)
#
#     # 获取系统日志的键
#     path = r"F:\System.evtx"
#     ids = [1074, 6005, 6006, 6008, 6009, 6013, 7036, 7040, 7045, 1102]
#     event_keys = []
#
#     # 遍历查询
#     for id in ids:
#         event_list = get_log_info(path, id)
#         print(event_list[0])
#         # 说明有数据
#         if len(event_list) > 0:
#             # 将键添加到列表中(不重复)
#             for key in event_list[0].keys():
#                 if key not in event_keys:
#                     event_keys.append(key)
#
#     print(event_keys)

# # 基线配置检测
#
# import subprocess
#
# # 执行powershell基线检测脚本
#
# # 清空base_line.log文件，因为脚本会自动追加日志，需要先清空之前的
# with open("baseLine.log", "w", encoding="utf-8") as file:
#     file.write("")
#
# # 定义PowerShell命令
# ps_command = 'powershell -ExecutionPolicy bypass -File ./powershell/windows.ps1'
# # 使用subprocess.run来运行PowerShell命令
# result = subprocess.run(['powershell', '-Command', ps_command],
#                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#
# # # 打印输出和错误信息
# # print(result.stdout)  # 输出信息
# # print(result.stderr)  # 错误信息
#
# # # 对基线检测结果进行处理
# # with open("baseLine.log", "r", encoding="utf-8") as file:
# #     # 遍历每一行
# #     for line in file:
# #         # 去除换行符
# #         line = line.strip()
# #         # 只取检测结果（带异常项和合格项的行）
# #         if "异常项" in line or "合格项" in line:
# #             # 第一步：根据空格切分，获取主要部分
# #             parts = re.sub(r'\s+', ' ', line).split(' ')
# #
# #             # 第二步：进一步处理第二部分，根据'|'切分获取具体数值和描述
# #             details = parts[1].split(']')
# #
# #             # 第三步：处理最后一部分，移除特殊字符后切分
# #             description_parts = details[1]
# #
# #             # # 输出结果
# #             policy_name = parts[0]
# #             qualification = details[0].replace('[', '')  # 提取“合格项”
# #             description_parts = description_parts
# #
# #             print(f"策略名称: {policy_name}")
# #             print(f"合规性: {qualification}")
# #             print(f"描述:{description_parts}")
#
# # 直接处理result,不去开文件了
# for line in result.stdout.splitlines():
#     # 去除换行符
#     line = line.strip()
#     # 只取检测结果（带异常项和合格项的行）
#     if "异常项" in line or "合格项" in line:
#
#         # 主要有两种输出结果，根据格式分别处理
#         # Registry::restrictanonymous = [异常项]|0|1|系统网络基配核查-关闭默认共享盘策略-【不符合】等级保护标准.
#         # [异常项]|HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer中DisableAutoplay不存在该项|1|禁止全部驱动器自动播放
#
#         if "=" in line:
#             # 第一步：根据[切分，获取主要部分(前后两部分)
#             parts = line.split('[')
#
#             # 第二步：进一步处理第一部分，去除" = "
#             name = parts[0].replace(' = ', '')
#
#             # 第三步：进一步切分第二部分，根据']'切分获取结论和描述
#             details = parts[1].split(']')
#
#             # 输出结果
#             policy_name = name # 提取策略名称
#             qualification = details[0] # 提取“合格项”和“异常项”
#             description_parts = details[1] # 提取描述
#         else:
#             # 第一步：根据]切分，获取主要部分
#             parts = line.split(']')
#
#             # 第二步：提取策略名称
#             policy_name = 'Registry::' + parts[1].split('中')[1].split('不存在')[0]
#
#             # 第三步：提取结论和描述
#             qualification = parts[0].replace('[', '')
#             description_parts = parts[1]
#
#         print(policy_name, qualification, description_parts)