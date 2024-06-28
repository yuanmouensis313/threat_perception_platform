import json
import threading
import time


class HeartCheck(threading.Thread):
    """
    心跳检查线程类，用于定期向服务器发送心跳信息，以保持连接 alive。

    Attributes:
        rabbit_mq: RabbitMQ 客户端对象，用于发送心跳消息。
        mac: 设备的 MAC 地址，作为心跳消息的一部分。
    """

    def __init__(self, rabbit_mq, mac):
        """
        初始化心跳检查线程。

        Args:
            rabbit_mq: RabbitMQ 客户端对象。
            mac: 设备的 MAC 地址。
        """
        super().__init__()
        # 私有属性，存储 RabbitMQ 客户端对象
        # rabbitmq对象
        self.__rabbit_mq = rabbit_mq
        # 私有属性，存储设备的 MAC 地址
        # mac地址
        self.__mac = mac


    def run(self):
        """
        不断发送心跳消息的循环。

        此函数在一个无限循环中运行，定期构建并发送心跳消息，以通知服务器该设备仍然活跃。
        心跳消息包含设备的MAC地址和一个表示状态的字段，这里始终设置为1，表示设备正常。
        """
        # 开始一个无限循环，用于定期发送心跳消息
        # 开始一个心跳检测线程，每3秒发送一次心跳消息
        while True:
            # 构建心跳消息的字典，包含设备MAC地址和状态
            # 开始心跳检测
            # 构建心跳消息
            heart_data = {
                'mac': self.__mac,
                'status': 1
            }
            # 将心跳消息的字典转换为JSON字符串，以便通过消息队列发送
            heart_data = json.dumps(heart_data)

            # 发送心跳消息
            # 发送消息
            self.__rabbit_mq.produce_heart_check(heart_data)

            # 暂停3秒，然后继续循环，发送下一次心跳消息
            # 停止三秒
            time.sleep(3)

