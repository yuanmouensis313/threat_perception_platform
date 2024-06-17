package com.tpp.threat_perception_platform.pojo;

import java.io.Serializable;

/**
 * 
 * @TableName application
 */
public class Application implements Serializable {
    /**
     * 主键ID
     */
    private Integer id;

    /**
     * MAC地址
     */
    private String mac;

    /**
     * 应用名称
     */
    private String displayName;

    /**
     * 应用安装位置
     */
    private String installLocation;

    /**
     * 应用卸载程序位置
     */
    private String uninstallString;

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
     * MAC地址
     */
    public String getMac() {
        return mac;
    }

    /**
     * MAC地址
     */
    public void setMac(String mac) {
        this.mac = mac;
    }

    /**
     * 应用名称
     */
    public String getDisplayName() {
        return displayName;
    }

    /**
     * 应用名称
     */
    public void setDisplayName(String displayName) {
        this.displayName = displayName;
    }

    /**
     * 应用安装位置
     */
    public String getInstallLocation() {
        return installLocation;
    }

    /**
     * 应用安装位置
     */
    public void setInstallLocation(String installLocation) {
        this.installLocation = installLocation;
    }

    /**
     * 应用卸载程序位置
     */
    public String getUninstallString() {
        return uninstallString;
    }

    /**
     * 应用卸载程序位置
     */
    public void setUninstallString(String uninstallString) {
        this.uninstallString = uninstallString;
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
        Application other = (Application) that;
        return (this.getId() == null ? other.getId() == null : this.getId().equals(other.getId()))
            && (this.getMac() == null ? other.getMac() == null : this.getMac().equals(other.getMac()))
            && (this.getDisplayName() == null ? other.getDisplayName() == null : this.getDisplayName().equals(other.getDisplayName()))
            && (this.getInstallLocation() == null ? other.getInstallLocation() == null : this.getInstallLocation().equals(other.getInstallLocation()))
            && (this.getUninstallString() == null ? other.getUninstallString() == null : this.getUninstallString().equals(other.getUninstallString()));
    }

    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + ((getId() == null) ? 0 : getId().hashCode());
        result = prime * result + ((getMac() == null) ? 0 : getMac().hashCode());
        result = prime * result + ((getDisplayName() == null) ? 0 : getDisplayName().hashCode());
        result = prime * result + ((getInstallLocation() == null) ? 0 : getInstallLocation().hashCode());
        result = prime * result + ((getUninstallString() == null) ? 0 : getUninstallString().hashCode());
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
        sb.append(", displayName=").append(displayName);
        sb.append(", installLocation=").append(installLocation);
        sb.append(", uninstallString=").append(uninstallString);
        sb.append(", serialVersionUID=").append(serialVersionUID);
        sb.append("]");
        return sb.toString();
    }
}