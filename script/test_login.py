import unittest, logging
from api.login_api import LoginApi
from utils import assert_common


class TestIHRMLogin(unittest.TestCase):
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

    def test01_login_success(self):
        # 调用封装的登录接口
        response = self.login_api.login("13800000002", "123456")
        # 接收放回的json数据
        jsondata = response.json()
        # 调试输出登入接口放回的数据
        logging.info("登入成功接口返回的数据为：{}".format(jsondata))

        # 断言
        # self.assertEqual(200, response.status_code)  # 断言状态响应码
        # self.assertEqual(True, jsondata.get("success"))  # 断言success
        # self.assertEqual(10000, jsondata.get("code"))  # 断言code
        # self.assertIn("操作成功", jsondata.get("message"))  # 断言message
        assert_common(self, response, 200, True, 10000, "操作成功")

    def test02_username_is_not_exist(self):
        # 调用封装的登录接口
        response = self.login_api.login("13900000002", "123456")
        # 接收放回的json数据
        jsonData = response.json()
        # 输出
        logging.info("账号不存在时输入的数据为：{}".format(jsonData))
        # 断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    def test03_password_is_error(self):
        # 调用封装的登录接口
        response = self.login_api.login("13800000002", "error")
        # 接收放回的json数据
        jsonData = response.json()
        # 输出
        logging.info("密码错误时输入的数据为：{}".format(jsonData))
        # 断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    def test04_username_have_special_char(self):
        # 调用封装的登录接口
        response = self.login_api.login("@#!$#%^&", "123456")
        # 接收放回的json数据
        jsonData = response.json()
        # 输出
        logging.info("账号输入特殊字符时输入的数据为：{}".format(jsonData))
        # 断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    def test05_username_is_empty(self):
        # 调用封装的登录接口
        response = self.login_api.login("", "123456")
        # 接收放回的json数据
        jsonData = response.json()
        # 输出
        logging.info("账号为空时输入的数据为：{}".format(jsonData))
        # 断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    def test06_password_is_emptr(self):
        # 调用封装的登录接口
        response = self.login_api.login("13900000002", "")
        # 接收放回的json数据
        jsonData = response.json()
        # 输出
        logging.info("密码为空时输入的数据为：{}".format(jsonData))
        # 断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    def test07_username_have_chinese(self):
        # 调用封装的登录接口
        response = self.login_api.login("13900三毛0002", "123456")
        # 接收放回的json数据
        jsonData = response.json()
        # 输出
        logging.info("账号中有中文时输入的数据为：{}".format(jsonData))
        # 断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    def test08_username_have_space(self):
        # 调用封装的登录接口
        response = self.login_api.login("139000 0002", "123456")
        # 接收放回的json数据
        jsonData = response.json()
        # 输出
        logging.info("账号中有空格时输入的数据为：{}".format(jsonData))
        # 断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")
