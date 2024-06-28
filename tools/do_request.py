# encoding:utf-8

import requests


class DoRequest:
    """
    专门用于发起请求
    """

    def __init__(self, path, method, data):
        self.__path = path
        self.__method = method
        self.__data = data

    def do_request(self):
        if self.__method == 'GET':
            return self.__do_get()
        elif self.__method == 'POST':
            return self.__do_post()
        else:
            return None

    def __do_get(self):
        """
        发起GET请求
        :return:
        """
        url = self.__path + self.__data

        try:
            print("url:" + url)
            # 发起请求
            response = requests.get(url)
            # 进行编码
            result = response.content.decode('utf-8')
            # 返回数据
            return result
        except Exception as e:
            print(e)
            return None

    def __do_post(self):
        """
        发起POST请求
        :return:
        """
        url = self.__path
        try:
            # 发起请求
            response = requests.post(url=url, data=self.__data)
            # 进行编码
            result = response.content.decode('utf-8')
            # 返回数据
            return result
        except Exception as e:
            print(e)
            return None
