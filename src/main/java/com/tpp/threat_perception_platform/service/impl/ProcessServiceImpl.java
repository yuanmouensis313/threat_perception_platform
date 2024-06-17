package com.tpp.threat_perception_platform.service.impl;

import com.github.pagehelper.PageHelper;
import com.github.pagehelper.PageInfo;
import com.tpp.threat_perception_platform.dao.ProcessMapper;
import com.tpp.threat_perception_platform.param.MyParam;
import com.tpp.threat_perception_platform.pojo.Account;
import com.tpp.threat_perception_platform.pojo.Process;
import com.tpp.threat_perception_platform.response.ResponseResult;
import com.tpp.threat_perception_platform.service.ProcessService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ProcessServiceImpl implements ProcessService {

    @Autowired
    private ProcessMapper processMapper;
    /**
     * 将探测到的进程信息入库
     * @param processes
     * @return
     */
    @Override
    public int addProcess(List<Process> processes) {
        // 1.将数据库中原有的数据删除，以免重复
        // 根据探测到的主机的mac地址，将该主机在数据库中已有的信息全部删除，以免重复
        // 获取mac地址
        String mac = processes.get(0).getMac();
        // 删除数据
        processMapper.deleteByMac(mac);

        // 2. 将数据入库
        return processMapper.insertBatch(processes);
    }

    /**
     * 获取进程信息的列表
     * @param param
     * @return
     */
    @Override
    public ResponseResult getAllProcess(MyParam param) {
        // 1.进行分页
        PageHelper.startPage(param.getPage(), param.getLimit());

        // 2.获取进程列表
        List<Process> processList = processMapper.selectAll(param);

        // 3.获取分页信息
        PageInfo pageInfo = new PageInfo(processList);

        // 4.返回数据
        return new ResponseResult(pageInfo.getTotal(), pageInfo.getList());
    }

    /**
     * @param ids
     * @return
     */
    @Override
    public ResponseResult deleteProcess(Integer[] ids) {
        // 待删除ID数组
        // 遍历删除
        processMapper.delete(ids);

        // 返回表示删除成功的结果对象
        // 返回表示删除成功的结果对象
        return new ResponseResult(0, "删除成功!");
    }
}
