package com.tpp.threat_perception_platform.service.impl;

import com.alibaba.fastjson.JSON;
import com.tpp.threat_perception_platform.pojo.LoginUser;
import com.tpp.threat_perception_platform.response.ResponseResult;
import com.tpp.threat_perception_platform.service.RefreshTokenService;
import com.tpp.threat_perception_platform.utils.RedisCache;
import com.tpp.threat_perception_platform.utils.JwtUtil;
import io.jsonwebtoken.Claims;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.HashMap;
import java.util.concurrent.TimeUnit;

@Service
public class RefreshTokenServiceImpl implements RefreshTokenService {

    @Autowired
    private RedisCache redisCache;

    /**
     * @param token
     * @return
     * @throws Exception
     */
    @Override
    public ResponseResult refreshToken(String token) throws Exception {
        // 解析token
        String uuid = "";
        Claims claims = JwtUtil.parseJWT(token);
        uuid = claims.getSubject();

        // 从redis中获取用户信息
        String redisKey = "login_" + uuid;
        String cachedUserInfo = redisCache.getCacheObject(redisKey);
        LoginUser loginUser = JSON.parseObject(cachedUserInfo, LoginUser.class);

        // 生成新的JWT
        String newJwt = JwtUtil.createJWT(uuid);
        // 更新Redis中的JWT
        redisCache.setCacheObject("login_" + uuid, JSON.toJSONString(loginUser), 60*60, TimeUnit.SECONDS);
        // 将新的JWT返回给前端
        HashMap<String, String> map = new HashMap<>();
        map.put("token", newJwt);
        return new ResponseResult<Object>(0, "JWT已更新！", map);
    }


}
