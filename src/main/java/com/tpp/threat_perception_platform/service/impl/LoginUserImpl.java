package com.tpp.threat_perception_platform.service.impl;

import com.alibaba.fastjson.JSON;
import com.tpp.threat_perception_platform.pojo.LoginUser;
import com.tpp.threat_perception_platform.pojo.User;
import com.tpp.threat_perception_platform.response.ResponseResult;
import com.tpp.threat_perception_platform.service.LoginServcie;
import com.tpp.threat_perception_platform.service.UserService;
import com.tpp.threat_perception_platform.utils.JwtUtil;
import com.tpp.threat_perception_platform.utils.RedisCache;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Service;

import java.sql.Timestamp;
import java.util.HashMap;
import java.util.Objects;
import java.util.concurrent.TimeUnit;

@Service
public class LoginUserImpl implements LoginServcie {

    @Autowired
    private AuthenticationManager authenticationManager;
    @Autowired
    private RedisCache redisCache;

    @Autowired
    private UserService userService;

    @Override
    /**
     * 用户登录方法
     *
     * @param user 登录用户的信息，包含用户名和密码
     * @return 返回登录结果，包括状态码、消息和令牌
     *
     * 方法流程：
     * 1. 创建认证令牌
     * 2. 尝试认证用户
     * 3. 如果认证失败，返回认证失败消息
     * 4. 如果认证成功，生成JWT令牌并存储用户登录信息到Redis
     * 5. 更新用户登录时间
     * 6. 返回登录成功消息和令牌
     */
    public ResponseResult<Object> login(User user) {
        // 创建基于用户名和密码的认证令牌
        // AuthenticationManager的authenticate方法进行用户认证
        UsernamePasswordAuthenticationToken authenticationToken = new UsernamePasswordAuthenticationToken(user.getUserName(), user.getUserPwd());
        // 尝试认证用户
        Authentication authenticate = authenticationManager.authenticate(authenticationToken);

        // 检查认证是否成功
        // 如果认证没通过，给出对应提示
        if (Objects.isNull(authenticate)) {
            return new ResponseResult<Object>(1001, "认证失败！");
        }
        // 获取认证成功的用户信息
        // 如果认证通过了，使用UUID(用户ID)生成JWT
        LoginUser loginUser = (LoginUser) authenticate.getPrincipal();
        // 生成UUID作为JWT的唯一标识
        String uuid = JwtUtil.getUUID();
        // 根据UUID创建JWT
        String jwt = JwtUtil.createJWT(uuid);
        // 设置用户的UUID，用于JWT验证
        loginUser.setUuid(uuid);
        // 将登录用户信息存储到Redis，有效期1小时
        redisCache.setCacheObject("login_" + uuid, JSON.toJSONString(loginUser), 60 * 60, TimeUnit.SECONDS);

        // 更新用户的登录时间
        // 防止更新到密码，将密码设置为空
        user.setUserPwd(null);
        user.setId(loginUser.getId());
        user.setLastLoginTime(new Timestamp(System.currentTimeMillis()));
        // 调用UserService更新用户信息
        userService.updateUser(user);

        // 准备登录成功返回的数据，包括JWT令牌
        // 把token响应给前端
        HashMap<String, String> map = new HashMap<>();
        map.put("token", jwt);
        // 返回登录成功结果，包括状态码、消息和令牌
        return new ResponseResult<Object>(200, "登录成功！", map);
    }

    @Override
    public ResponseResult logout() {
        // 获取SecurityContextHolder中的用户ID
        Authentication authentication = SecurityContextHolder.getContext().getAuthentication();
        LoginUser loginUser = (LoginUser) authentication.getPrincipal();
        String uuid = loginUser.getUuid();
        // 删除redis中的值
        redisCache.deleteObject("login_" + uuid);
        return new ResponseResult<Object>(200, "退出成功！");
    }


}

