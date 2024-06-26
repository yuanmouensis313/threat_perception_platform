package com.tpp.threat_perception_platform.param;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class LogParam {
    // 要进行日志探测的主机名
    private String hostname;

    // 主机的MAC地址
    private String mac;

    // 表明是进行日志探测
    private String type = "log";
}
