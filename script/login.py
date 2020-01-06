import unittest, logging

import app
from api.login_api import LoginApi
from utils import assert_common


class Login(unittest.TestCase):
    def setUp(self) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:
        # 初始化登入类
        cls.login_api = LoginApi()

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_login(self):
        # 调用封装的登录接口
        response = self.login_api.login("13800000002", "123456")
        # 接收放回的json数据
        jsondata = response.json()
        # 调试输出登入接口放回的数据
        logging.info("登入成功接口返回的数据为：{}".format(jsondata))

        # 断言

        assert_common(self, response, 200, True, 10000, "操作成功")
        # 获取令牌，并拼接成以Bearer 开头的令牌字符串
        token = jsondata.get("data")
        # 保存令牌到全局变量
        app.HEADERS['Authorization'] = "Bearer " + token
        logging.info("保存的令牌是：{}".format(app.HEADERS))