package com.tpp.threat_perception_platform.param;


import com.tpp.threat_perception_platform.pojo.Vulnerability;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class ThreatParam {
    // 要进行资产探测的主机名称
    private String hostname;

    // 要进行资产探测的主机MAC地址
    private String mac;

    // 安全补丁风险探测，默认为0，0表示不进行探测，1表示进行探测
    private Integer hotfix = 0;

    // 漏洞探测，默认为0，0表示不进行探测，1表示进行探测
    private Integer vulnerability = 0;

    // 弱口令探测，默认为0，0表示不进行探测，1表示进行探测
    private Integer weekPassword = 0;

    // 应用风险探测，默认为0，0表示不进行探测，1表示进行探测
    private Integer application = 0;

    // 系统风险探测，默认为0，0表示不进行探测，1表示进行探测
    private Integer system = 0;

    // 漏洞数据库列表，传送到客户端进行测试
    private List<Vulnerability>  vulnerabilities;

    // 探测类型，用于区分：资产探测和威胁探测
    private String type = "threat";
}
