import json

import pika

from work.assets_detect import AssetsDetect
from work.base_line_discovery import BaseLineDiscovery
from work.log_discovery import LogDiscovery
from work.threat_detect import ThreatDetect


class RabbitMq(object):
    """
    专门用于发送rabbitMQ消息的类
    """

    def __init__(self):
        self.__host = '111.231.191.94'
        self.__port = '4567'
        self.__user = 'admin'
        self.__password = '20240606'
        self.__virtual_host = 'my_vhost'
        self.__connection = ''
        self.__channel = ''

        # 初始化连接
        self.__get_connection()

    def __get_connection(self):
        # 获取认证对象
        credentials = pika.PlainCredentials(self.__user, self.__password)
        # 获取连接
        self.__connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.__host,
                                      port=self.__port,
                                      virtual_host=self.__virtual_host,
                                      credentials=credentials))
        # 获取通道
        self.__channel = self.__connection.channel()

    def __produce_message(self, exchange, routing_key, message):
        """
        作为队列中的生产者，生产消息
        :param exchange: 交换机
        :param routing_key: 绑定键
        :param message: 要发送的消息
        :return:
        """
        # 发送消息
        self.__channel.basic_publish(exchange=exchange,
                                     routing_key=routing_key,
                                     body=message)

    def produce_system_info(self, message):
        """
        负责调用私有方法发送数据到rabbitmq消息队列中
        发送系统探测信息
        :param message: 要发送的消息
        :return:
        """
        exchange = 'sysinfo_exchange'
        routing_key = 'sysinfo'
        # 发送消息
        self.__produce_message(exchange, routing_key, message)

    def produce_account_data(self, message):
        """
        负责调用私有方法发送数据到rabbitmq消息队列中
        发送账号探测的数据
        :param message: 要发送的消息
        :return:
        """
        exchange = 'sysinfo_exchange'
        routing_key = 'account'
        # 发送消息
        print("开始向account_queue队列中发送探测到的账号信息..........")
        self.__produce_message(exchange, routing_key, message)
        print("向account_queue队列中发送探测到的账号信息成功..........")

    def produce_service_data(self, message):
        """
        负责调用私有方法发送数据到rabbitmq消息队列中
        发送服务探测的数据
        :param message: 要发送的消息
        :return:
        """
        exchange = 'sysinfo_exchange'
        routing_key = 'service'
        # 发送消息
        print("开始向service_queue队列中发送探测到的服务信息..........")
        self.__produce_message(exchange, routing_key, message)
        print("向service_queue队列中发送探测到的服务信息成功..........")

    def produce_process_data(self, message):
        """
        负责调用私有方法发送数据到rabbitmq消息队列中
        发送进程探测的数据
        :param message: 要发送的消息
        :return:
        """
        exchange = 'sysinfo_exchange'
        routing_key = 'process'
        # 发送消息
        print("开始向process_queue队列中发送探测到的进程信息..........")
        self.__produce_message(exchange, routing_key, message)
        print("向process_queue队列中发送探测到的进程信息成功..........")

    def produce_application_data(self, message):
        """
        负责调用私有方法发送数据到rabbitmq消息队列中
        发送应用探测的数据
        :param message: 要发送的消息
        :return:
        """
        exchange = 'sysinfo_exchange'
        routing_key = 'application'
        # 发送消息
        print("开始向application_queue队列中发送探测到的进程信息..........")
        self.__produce_message(exchange, routing_key, message)
        print("向application_queue队列中发送探测到的进程信息成功..........")

    def produce_hotfix_data(self, data):
        """
        负责调用私有方法发送数据到rabbitmq消息队列中
        发送补丁信息
        :param message: 要发送的消息
        :return:
        """
        exchange = 'sysinfo_exchange'
        routing_key = 'hotfix'
        # 发送消息
        print("开始向hotfix_queue队列中发送补丁信息..........")
        self.__produce_message(exchange, routing_key, data)
        print("向hotfix_queue队列中发送补丁信息成功..........")

    def produce_vul_data(self, data):
        """
        负责调用私有方法发送数据到rabbitmq消息队列中
        发送漏洞探测信息
        :param message: 要发送的消息
        :return:
        """
        exchange = 'sysinfo_exchange'
        routing_key = 'vulnerability'
        # 发送消息
        print("开始向hotfix_queue队列中发送补丁信息..........")
        self.__produce_message(exchange, routing_key, data)
        print("向hotfix_queue队列中发送补丁信息成功..........")

    def produce_weak_pwd_data(self, data):
        """
        负责调用私有方法发送数据到rabbitmq消息队列中
        发送弱口令探测信息
        :param message: 要发送的消息
        :return:
        """
        exchange = 'sysinfo_exchange'
        routing_key = 'weakPwd'
        # 发送消息
        print("开始向weak_pwd_queue队列中发送弱口令信息..........")
        self.__produce_message(exchange, routing_key, data)
        print("向weak_pwd_queue队列中发送弱口令信息成功..........")

    def produce_app_vul_data(self, data):
        """
        负责调用私有方法发送数据到rabbitmq消息队列中
        发送应用风险探测信息
        :param message: 要发送的消息
        :return:
        """
        exchange = 'sysinfo_exchange'
        routing_key = 'appVul'
        # 发送消息
        print("开始向weak_pwd_queue队列中发送应用风险信息..........")
        self.__produce_message(exchange, routing_key, data)
        print("向weak_pwd_queue队列中发送应用风险信息成功..........")

    def produce_system_vul_data(self, data):
        """
        负责调用私有方法发送数据到rabbitmq消息队列中
        发送系统风险探测信息
        :param message: 要发送的消息
        :return:
        """
        exchange = 'sysinfo_exchange'
        routing_key = 'system_vul'
        # 发送消息
        print("开始向system_vul_queue队列中发送系统风险信息..........")
        self.__produce_message(exchange, routing_key, data)
        print("向system_vul_queue队列中发送系统风险信息成功..........")

    def produce_log_data(self, data):
        """
        负责调用私有方法发送数据到rabbitmq消息队列中
        发送日志探测信息
        :param message: 要发送的消息
        :return:
        """
        exchange = 'sysinfo_exchange'
        routing_key = 'logs'
        # 发送消息
        print("开始向logs_queue队列中发送日志探测信息..........")
        self.__produce_message(exchange, routing_key, data)
        print("向logs_queue队列中发送日志探测信息成功..........")

    def produce_base_line_data(self, data):
        """
        负责调用私有方法发送数据到rabbitmq消息队列中
        发送基线探测信息
        :param message: 要发送的消息
        :return:
        """
        exchange = 'sysinfo_exchange'
        routing_key = 'base_line'
        # 发送消息
        print("开始向base_line_queue队列中发送基线探测信息..........")
        self.__produce_message(exchange, routing_key, data)
        print("向base_line_queue队列中发送基线探测信息成功..........")

    def produce_heart_check(self, message):
        """
        负责调用私有方法发送数据到rabbitmq消息队列中
        发送心跳检测消息
        :param message: 要发送的消息
        :return:
        """
        exchange = 'sysinfo_exchange'
        routing_key = 'status'
        # 发送消息
        self.__produce_message(exchange, routing_key, message)

    def __process_message(self, ch, method, properties, message):
        """
        处理消息
        :param ch:
        :param properties:
        :param message:
        :return:
        """

        # JSON字符串转换成字典
        data = json.loads(message)
        print("接收到消息：", data)
        # 判断类型
        if data['type'] == 'assets':
            # 资产探测
            assetsDetect = AssetsDetect(self, data)
            assetsDetect.start()
        elif data['type'] == 'threat':
            # 威胁探测
            threatDetect = ThreatDetect(self, data)
            threatDetect.start()
        elif data['type'] == 'log':
            # 补丁探测
            log_discovery = LogDiscovery(self, data['mac'])
            log_discovery.start()
        elif data['type'] == 'baseLine':
            # 基线探测
            base_line_discovery = BaseLineDiscovery(self, data['mac'])
            base_line_discovery.start()


    def consume_queue(self, queue_name):
        """
        消费队列数据
        :param queue_name:
        :return:
        """

        # 消费队列
        self.__channel.basic_consume(queue=queue_name,
                                     on_message_callback=self.__process_message, auto_ack=True)

        # 开始监听
        self.__channel.start_consuming()
