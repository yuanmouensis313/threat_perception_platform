package com.tpp.threat_perception_platform.service;

import com.tpp.threat_perception_platform.param.MyParam;
import com.tpp.threat_perception_platform.pojo.BaseLineResult;
import com.tpp.threat_perception_platform.response.ResponseResult;

import java.util.List;

public interface BaseLineResultService {

    /**
     * 添加基线检测结果
     * @param baseLineResult
     * @return
     */
    int addBaseLineResult(List<BaseLineResult> baseLineResult);

    /**
     * 查询基线检测结果
     * @param myParam
     * @return
     */
    ResponseResult findBaseLineResultList(MyParam myParam);

    /**
     * 删除基线检测结果
     * @param ids
     * @return
     */
    ResponseResult deleteBaseLineResult(Integer[] ids);

    /**
     * 查询所有基线检测结果,传回前端，用于饼图统计
     * @return
     */
    ResponseResult findAllBaseLineResult();

}
