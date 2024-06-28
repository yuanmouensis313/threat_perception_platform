package com.tpp.threat_perception_platform.controller;

import com.tpp.threat_perception_platform.response.ResponseResult;
import com.tpp.threat_perception_platform.service.RefreshTokenService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class RefreshTokenController {
    @Autowired
    private RefreshTokenService refreshTokenService;

    /**
     * 刷新token
     * @param token
     * @return
     * @throws Exception
     */
    @PostMapping("/refreshToken")
    public ResponseResult refreshToken(@RequestParam("token") String token) throws Exception {
        return refreshTokenService.refreshToken(token);
    }
}
