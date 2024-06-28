import threading

"""
本类专门用于接收平台指令
"""


class ReceivePlatformInstruction(threading.Thread):
    def __init__(self, rabbitmq, mac):
        super().__init__()
        # rabbitmq对象，用于与队列进行交互
        self.rabbitmq = rabbitmq
        # mac地址，用于标识设备和确定queue
        self.mac = mac

    def run(self):
        # 调用rabbitmq对象的consume_message方法，接收消息
        # 队列名称为agent_mac地址_queue

        # 拼接队列名称
        queue_name = "agent_" + self.mac.replace(":", "") + "_queue"
        # 调用consume_message方法，消费消息
        self.rabbitmq.consume_queue(queue_name)