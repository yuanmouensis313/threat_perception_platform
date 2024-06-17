package com.tpp.threat_perception_platform.param;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;


// 作为承载资产探测参数数据的类
@Data
@AllArgsConstructor
@NoArgsConstructor
public class AssetsParam {
    // 要进行资产探测的主机名称
    private String hostname;

    // 要进行资产探测的主机MAC地址
    private String mac;

    // 账号探测，默认为0，0表示不进行探测，1表示进行探测
    private Integer account = 0;

    // 服务探测，默认为0，0表示不进行探测，1表示进行探测
    private Integer service = 0;

    // 应用探测，默认为0，0表示不进行探测，1表示进行探测
    private Integer application = 0;

    // 进程探测，默认为0，0表示不进行探测，1表示进行探测
    private Integer process = 0;

    // 探测类型，用于区分：资产探测和威胁探测
    private String type = "assets";
}
