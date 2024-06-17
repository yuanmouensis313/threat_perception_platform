package com.tpp.threat_perception_platform.service;

public interface RabbitmqService {

    // 动态创建消息队列
    void createAgentQueue(String exchangeName, String queueName, String routingKey);

    // 发送消息到队列中
    void sendMessage(String exchangeName, String routingKey, String message);
}
