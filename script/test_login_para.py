import unittest, logging
from api.login_api import LoginApi
from utils import assert_common, read_login_data
from parameterized.parameterized import parameterized


class TestIHRMLoginPara(unittest.TestCase):
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

    @parameterized.expand(read_login_data)
    def test_login(self, mobile, password, http_code, success, code, message):
        # 调用封装的登录接口
        response = self.login_api.login(mobile, password)
        # 接收放回的json数据
        jsondata = response.json()
        # 调试输出登入接口放回的数据
        logging.info("登入成功接口返回的数据为：{}".format(jsondata))

        # 断言

        assert_common(self, response, http_code, success, code, message)
