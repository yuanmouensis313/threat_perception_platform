// 定义一个函数用于定时执行任务
function callBackendWithRefreshToken() {
    // 发送请求到后端接口
    $.ajax({
        url: '/refreshToken', // 替换为你的后端接口地址
        method: 'POST', // 或者 'GET'，根据你的后端接口需求
        headers: {
            'Authorization': localStorage.getItem('token') // 设置 Authorization 头部，传递 refresh token
        },
        data:{token : localStorage.getItem('token')},
        success: function(response) {
            if (response.code === 0){
                // 更新成功
                localStorage.setItem('token', response.data.token);
                console.log('Refresh token updated successfully!')
            }
        },
        error: function(xhr, status, error) {
            console.error('Error calling backend API:', error);
            // 在这里处理错误响应的逻辑
        }
    });
}

// 每 50 分钟执行一次任务
setInterval(callBackendWithRefreshToken, 50 * 60 * 1000); // 50分钟转换为毫秒数

// 页面加载后立即执行一次，确保页面刚加载时也会执行一次
$(document).ready(function() {
    callBackendWithRefreshToken();
});

