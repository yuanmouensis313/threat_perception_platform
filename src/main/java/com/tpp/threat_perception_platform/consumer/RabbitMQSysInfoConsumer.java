package com.tpp.threat_perception_platform.consumer;

import com.alibaba.fastjson.JSON;
import com.rabbitmq.client.Channel;
import com.tpp.threat_perception_platform.dao.ProcessMapper;
import com.tpp.threat_perception_platform.pojo.*;
import com.tpp.threat_perception_platform.pojo.Process;
import com.tpp.threat_perception_platform.service.*;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.amqp.support.AmqpHeaders;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.messaging.handler.annotation.Headers;
import org.springframework.stereotype.Component;

import java.io.IOException;
import java.util.List;
import java.util.Map;

@Component
public class RabbitMQSysInfoConsumer {
    @Autowired
    private HostService hostService;

    @Autowired
    private AccountService accountService;

    @Autowired
    private ServiceService serviceService;

    @Autowired
    private ProcessService processService;

    @Autowired
    private ApplicationService applicationService;

    @Autowired
    private HotfixService hotfixService;

    @RabbitListener(queues = {"sysinfo_queue"})

    public void receive_message(String message, @Headers Map<String,Object> headers,
                               Channel channel) throws IOException {
        // 接收消息
        System.out.println("receive_message:" + message);

        // 将json字符串类型的消息转化为host对象
        Host host = JSON.parseObject(message, Host.class);

        // 消息入库,res用于接收返回的信息，返回的信息为影响的行数
        int res = hostService.pushHost(host);

        if (res > 0){
            // res>0，说明影响行数不为0，入库成功
            // 手动 ACK, 先获取 deliveryTag
            Long deliveryTag = (Long)headers.get(AmqpHeaders.DELIVERY_TAG);
            // ACK
            channel.basicAck(deliveryTag,false);
        }


    }

    @RabbitListener(queues = {"status_queue"})

    public void receive_status_message(String message, @Headers Map<String,Object> headers,
                                Channel channel) throws IOException {
        // 接收消息
        System.out.println("receive_message:" + message);

        // 将json字符串类型的消息转化为host对象
        Host host = JSON.parseObject(message, Host.class);

        // 消息入库,res用于接收返回的信息，返回的信息为影响的行数
        int res = hostService.heartbeat(host);

        // 手动 ACK, 先获取 deliveryTag
        Long deliveryTag = (Long)headers.get(AmqpHeaders.DELIVERY_TAG);
        // ACK
        channel.basicAck(deliveryTag,false);

    }

    @RabbitListener(queues = {"account_queue"})

    public void account(String message, @Headers Map<String,Object> headers,
                                Channel channel) throws IOException {
        // 将json字符串类型的消息转化为Account对象
        List<Account> accounts = JSON.parseArray(message, Account.class);

        // 消息入库,res用于接收返回的信息，返回的信息为影响的行数
        int res = accountService.addAccount(accounts);

        if (res > 0){
            // res>0，说明影响行数不为0，入库成功
            // 手动 ACK, 先获取 deliveryTag
            Long deliveryTag = (Long)headers.get(AmqpHeaders.DELIVERY_TAG);
            // ACK
            channel.basicAck(deliveryTag,false);
        }


    }

    @RabbitListener(queues = {"service_queue"})

    public void service(String message, @Headers Map<String,Object> headers,
                        Channel channel) throws IOException {
        // 将json字符串类型的消息转化为Service对象
        List<Service> services = JSON.parseArray(message, Service.class);

        // 消息入库,res用于接收返回的信息，返回的信息为影响的行数
        int res = serviceService.addService(services);

        if (res > 0){
            // res>0，说明影响行数不为0，入库成功
            // 手动 ACK, 先获取 deliveryTag
            Long deliveryTag = (Long)headers.get(AmqpHeaders.DELIVERY_TAG);
            // ACK
            channel.basicAck(deliveryTag,false);
        }


    }

    @RabbitListener(queues = {"process_queue"})

    public void process(String message, @Headers Map<String,Object> headers,
                        Channel channel) throws IOException {
        // 将json字符串类型的消息转化为Process对象
        List<Process> processes = JSON.parseArray(message, Process.class);

        // 消息入库,res用于接收返回的信息，返回的信息为影响的行数
        int res = processService.addProcess(processes);

        if (res > 0){
            // res>0，说明影响行数不为0，入库成功
            // 手动 ACK, 先获取 deliveryTag
            Long deliveryTag = (Long)headers.get(AmqpHeaders.DELIVERY_TAG);
            // ACK
            channel.basicAck(deliveryTag,false);
        }


    }

    @RabbitListener(queues = {"application_queue"})

    public void application(String message, @Headers Map<String,Object> headers,
                        Channel channel) throws IOException {
        // 将json字符串类型的消息转化为Application对象
        List<Application> applications = JSON.parseArray(message, Application.class);

        // 消息入库,res用于接收返回的信息，返回的信息为影响的行数
        int res = applicationService.addApplication(applications);

        if (res > 0){
            // res>0，说明影响行数不为0，入库成功
            // 手动 ACK, 先获取 deliveryTag
            Long deliveryTag = (Long)headers.get(AmqpHeaders.DELIVERY_TAG);
            // ACK
            channel.basicAck(deliveryTag,false);
        }


    }

    @RabbitListener(queues = {"hotfix_queue"})

    public void hotfix(String message, @Headers Map<String,Object> headers,
                            Channel channel) throws IOException {
        // 将json字符串类型的消息转化为Hotfix对象
        List<Hotfix> hotfixes = JSON.parseArray(message, Hotfix.class);

        // 消息入库,res用于接收返回的信息，返回的信息为影响的行数
        int res = hotfixService.addHotfix(hotfixes);

        if (res > 0){
            // res>0，说明影响行数不为0，入库成功
            // 手动 ACK, 先获取 deliveryTag
            Long deliveryTag = (Long)headers.get(AmqpHeaders.DELIVERY_TAG);
            // ACK
            channel.basicAck(deliveryTag,false);
        }
    }
}