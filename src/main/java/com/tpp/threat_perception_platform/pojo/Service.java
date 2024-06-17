package com.tpp.threat_perception_platform.pojo;

import java.io.Serializable;

/**
 * 
 * @TableName service
 */
public class Service implements Serializable {
    /**
     * 主键ID
     */
    private Integer id;

    /**
     * mac地址
     */
    private String mac;

    /**
     * 协议
     */
    private String protocol;

    /**
     * 端口号
     */
    private String port;

    /**
     * 状态
     */
    private String state;

    /**
     * 服务名称
     */
    private String name;

    /**
     * 产品
     */
    private String product;

    /**
     * 服务版本
     */
    private String version;

    /**
     * 附加信息
     */
    private String extrainfo;

    private static final long serialVersionUID = 1L;

    /**
     * 主键ID
     */
    public Integer getId() {
        return id;
    }

    /**
     * 主键ID
     */
    public void setId(Integer id) {
        this.id = id;
    }

    /**
     * mac地址
     */
    public String getMac() {
        return mac;
    }

    /**
     * mac地址
     */
    public void setMac(String mac) {
        this.mac = mac;
    }

    /**
     * 协议
     */
    public String getProtocol() {
        return protocol;
    }

    /**
     * 协议
     */
    public void setProtocol(String protocol) {
        this.protocol = protocol;
    }

    /**
     * 端口号
     */
    public String getPort() {
        return port;
    }

    /**
     * 端口号
     */
    public void setPort(String port) {
        this.port = port;
    }

    /**
     * 状态
     */
    public String getState() {
        return state;
    }

    /**
     * 状态
     */
    public void setState(String state) {
        this.state = state;
    }

    /**
     * 服务名称
     */
    public String getName() {
        return name;
    }

    /**
     * 服务名称
     */
    public void setName(String name) {
        this.name = name;
    }

    /**
     * 产品
     */
    public String getProduct() {
        return product;
    }

    /**
     * 产品
     */
    public void setProduct(String product) {
        this.product = product;
    }

    /**
     * 服务版本
     */
    public String getVersion() {
        return version;
    }

    /**
     * 服务版本
     */
    public void setVersion(String version) {
        this.version = version;
    }

    /**
     * 附加信息
     */
    public String getExtrainfo() {
        return extrainfo;
    }

    /**
     * 附加信息
     */
    public void setExtrainfo(String extrainfo) {
        this.extrainfo = extrainfo;
    }

    @Override
    public boolean equals(Object that) {
        if (this == that) {
            return true;
        }
        if (that == null) {
            return false;
        }
        if (getClass() != that.getClass()) {
            return false;
        }
        Service other = (Service) that;
        return (this.getId() == null ? other.getId() == null : this.getId().equals(other.getId()))
            && (this.getMac() == null ? other.getMac() == null : this.getMac().equals(other.getMac()))
            && (this.getProtocol() == null ? other.getProtocol() == null : this.getProtocol().equals(other.getProtocol()))
            && (this.getPort() == null ? other.getPort() == null : this.getPort().equals(other.getPort()))
            && (this.getState() == null ? other.getState() == null : this.getState().equals(other.getState()))
            && (this.getName() == null ? other.getName() == null : this.getName().equals(other.getName()))
            && (this.getProduct() == null ? other.getProduct() == null : this.getProduct().equals(other.getProduct()))
            && (this.getVersion() == null ? other.getVersion() == null : this.getVersion().equals(other.getVersion()))
            && (this.getExtrainfo() == null ? other.getExtrainfo() == null : this.getExtrainfo().equals(other.getExtrainfo()));
    }

    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + ((getId() == null) ? 0 : getId().hashCode());
        result = prime * result + ((getMac() == null) ? 0 : getMac().hashCode());
        result = prime * result + ((getProtocol() == null) ? 0 : getProtocol().hashCode());
        result = prime * result + ((getPort() == null) ? 0 : getPort().hashCode());
        result = prime * result + ((getState() == null) ? 0 : getState().hashCode());
        result = prime * result + ((getName() == null) ? 0 : getName().hashCode());
        result = prime * result + ((getProduct() == null) ? 0 : getProduct().hashCode());
        result = prime * result + ((getVersion() == null) ? 0 : getVersion().hashCode());
        result = prime * result + ((getExtrainfo() == null) ? 0 : getExtrainfo().hashCode());
        return result;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(getClass().getSimpleName());
        sb.append(" [");
        sb.append("Hash = ").append(hashCode());
        sb.append(", id=").append(id);
        sb.append(", mac=").append(mac);
        sb.append(", protocol=").append(protocol);
        sb.append(", port=").append(port);
        sb.append(", state=").append(state);
        sb.append(", name=").append(name);
        sb.append(", product=").append(product);
        sb.append(", version=").append(version);
        sb.append(", extrainfo=").append(extrainfo);
        sb.append(", serialVersionUID=").append(serialVersionUID);
        sb.append("]");
        return sb.toString();
    }
}