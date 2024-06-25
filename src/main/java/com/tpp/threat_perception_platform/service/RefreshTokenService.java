package com.tpp.threat_perception_platform.service;

import com.tpp.threat_perception_platform.response.ResponseResult;

public interface RefreshTokenService {
    ResponseResult refreshToken(String token) throws Exception;
}
