package com.tpp.threat_perception_platform.config;


import org.springframework.amqp.rabbit.connection.ConnectionFactory;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * 配置类，用于配置RabbitMQ的相关设置。
 */
@Configuration
public class RabbitMQConfig {

    /**
     * 创建并配置RabbitTemplate bean，用于简化与RabbitMQ的消息交互。
     *
     * @param connectionFactory 提供与RabbitMQ服务器连接的ConnectionFactory。
     * @return 配置好的RabbitTemplate实例。
     */
    @Bean
    public RabbitTemplate rabbitTemplate(ConnectionFactory connectionFactory){
        return new RabbitTemplate(connectionFactory);
    };
}
