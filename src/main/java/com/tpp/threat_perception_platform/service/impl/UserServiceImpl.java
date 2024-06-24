package com.tpp.threat_perception_platform.service.impl;

import com.github.pagehelper.PageHelper;
import com.github.pagehelper.PageInfo;
import com.tpp.threat_perception_platform.dao.UserMapper;
import com.tpp.threat_perception_platform.param.ChangePwdParam;
import com.tpp.threat_perception_platform.param.MyParam;
import com.tpp.threat_perception_platform.pojo.User;
import com.tpp.threat_perception_platform.response.ResponseResult;
import com.tpp.threat_perception_platform.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Service;

import java.sql.Timestamp;
import java.util.List;

@Service
public class UserServiceImpl implements UserService {

    @Autowired
    private UserMapper userMapper;

    @Autowired
    private BCryptPasswordEncoder bCryptPasswordEncoder;
    /**
     * 用户列表数据
     * @param param
     * @return
     */
    @Override
    public ResponseResult userList(MyParam param) {
        // 设置分页参数
        PageHelper.startPage(param.getPage(), param.getLimit());
        // 查询所有
        List<User> userList = userMapper.findAll(param);
        // 构架pageInfo
        PageInfo<User> pageInfo = new PageInfo<>(userList);

        return new ResponseResult<>(pageInfo.getTotal(), pageInfo.getList());
    }

    /**
     * 用户更新
     * @param user
     */
    @Override
    public void updateUser(User user) {
        userMapper.updateByPrimaryKeySelective(user);
    }

    /**
     * 保存用户
     * @param user
     * @return
     */
    @Override
    public ResponseResult save(User user) {
        // 先查询 是否有用户
        User db_user = userMapper.selectByUserName(user.getUserName());
        if ( db_user!= null){
            return new ResponseResult<>(1003, "用户已存在！");
        }
        // 处理密码
        user.setUserPwd(bCryptPasswordEncoder.encode(user.getUserPwd()));
        user.setUserRole(2);
        user.setCreateTime(new Timestamp(System.currentTimeMillis()));
        // 添加
        userMapper.insertSelective(user);
        return new ResponseResult<>(0, "添加成功！");
    }

    /**
     * 编辑用户
     * @param user
     * @return
     */
    @Override
    public ResponseResult edit(User user) {
        // 先确定这个用户是否是管理员
        User db_user = userMapper.selectByPrimaryKey(Long.valueOf(user.getId()));
        if ("admin".equals(db_user.getUserName())){
            return new ResponseResult<>(1003, "管理员不能修改！");
        }
        // 设置修改时间
        user.setUpdateTime(new Timestamp(System.currentTimeMillis()));
        userMapper.updateByPrimaryKeySelective(user);
        return new ResponseResult<>(0, "更新成功！");
    }

    /**
     * 删除用户
     * @param ids
     * @return
     */
    @Override
    public ResponseResult delete(Integer[] ids) {
        userMapper.delete(ids);
        return new ResponseResult<>(0, "删除成功！");
    }

    /**
     * 修改密码
     *
     * @param changePwdParam
     * @return
     */
    @Override
    public ResponseResult changePwd(ChangePwdParam changePwdParam) {
        // 1. 验证旧密码正确
        // 旧密码加密
        String oldPwd = bCryptPasswordEncoder.encode(changePwdParam.getOldPwd());
        // 获取数据库中的密码,根据用户名查询
        User db_user = userMapper.selectByUserName(changePwdParam.getUsername());
        String db_pwd = db_user.getUserPwd();

        if (bCryptPasswordEncoder.matches(changePwdParam.getOldPwd(), db_pwd)){
            // 2. 两者相等，说明旧密码正确，修改密码
            User user = new User();
            user.setUserName(changePwdParam.getUsername());
            user.setUserPwd(bCryptPasswordEncoder.encode(changePwdParam.getNewPwd()));
            user.setId(db_user.getId());
            userMapper.updateByPrimaryKeySelective(user);
            return new ResponseResult<>(0, "修改成功！");
        }
        // 否则说明旧密码不对，返回错误信息
        return new ResponseResult(200, "旧密码错误！");
    }
}
