# utf-8
# Author: AJNUY

from system.system_info import SystemInfo
from mq.rabbit_mq import RabbitMq
from work.base_line_discovery import BaseLineDiscovery
from work.heart_check import HeartCheck
from work.log_discovery import LogDiscovery
from work.receive_platform_instruction import ReceivePlatformInstruction

if __name__ == "__main__":
    print("程序初始化............")
    print("获取系统信息中............")
    system_info = SystemInfo()
    print(system_info.get_system_info())
    print("发送系统信息中............")
    rabbit_mq = RabbitMq()
    rabbit_mq.produce_system_info(system_info.get_system_info())
    print("消息发送成功............")
    print("程序结束............")

    # 心跳检测
    print("开始进行心跳检测............")
    heart_check = HeartCheck(rabbit_mq, system_info.mac)
    heart_check.start()

    # 接收平台指令
    print("开始接收平台指令............")
    # 在rabbitmq中，接收消息的连接和发送消息的连接不能是同一个，会报错，所以重新初始化一个rabbitmq对象
    rabbit_mq = RabbitMq()
    receive_platform_instruction = ReceivePlatformInstruction(rabbit_mq, system_info.mac)
    receive_platform_instruction.start()

    # # 开始进行日志检测
    # print("开始进行日志检测............")
    # rabbit_mq = RabbitMq()
    # log_discovery = LogDiscovery(rabbit_mq, system_info.mac)
    # log_discovery.start()
