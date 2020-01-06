import logging
import unittest
from api.emp_api import EmpApi
from utils import assert_common, read_add_emp_data, read_query_emp_data, read_modify_emp_data, read_delete_emp_data, \
    DBUtils
import app
from parameterized.parameterized import parameterized


class TestIHRMEmp(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 初始化登录类
        cls.emp_api = EmpApi()

    @parameterized.expand(read_add_emp_data)
    def test01_add_emp(self, username, mobile, success, code, message, http_code):
        response = self.emp_api.add_emp(username, mobile)
        jsonDate = response.json()
        logging.info('添加员工接口返回数据为：{}'.format(jsonDate))
        # 获取员工ID保存在全局变量
        app.EMP_ID = jsonDate.get('data').get('id')
        logging.info('员工ID为：{}'.format(app.EMP_ID))
        # 断言
        assert_common(self, response, code, http_code, success, message)



    @parameterized.expand(read_query_emp_data)
    def test02_query_emp(self, success, code, message, http_code):
        # 调用查询员工接口
        response = self.emp_api.query_emp()
        jsonData = response.json()
        logging.info('查询员工接口返回数据{}'.format(jsonData))
        #         断言
        assert_common(self, response, http_code, success, code, message)

    @parameterized.expand(read_modify_emp_data)
    def test03_update_emp(self, username, success, code, message, http_code):
        response = self.emp_api.update_emp(username)
        jsonData = response.json()
        logging.info('修改员工接口返回数据{}'.format(jsonData))

        with DBUtils() as db_utis:
            # 执行查询语句，查询出添加的员工的username 是不是修改的username
            sql = "select username form bs_user where id={}".format(app.EMP_ID)
            db_utis.execute(sql)
            # 获取执行结果
            result = db_utis.fetchone()[0]
            logging.info("从数据库中查询出的员工用户名是：{}".format(result))
        # 断言
        assert_common(self, response, code, success, http_code, message)

    @parameterized.expand(read_delete_emp_data)
    def test04_delete_emp(self, success, code, message, http_code):
        response = self.emp_api.delete_emp()
        jsonData = response.json()
        logging.info('删除员工接口返回数据{}'.format(jsonData))
        assert_common(self, response, code, http_code, success, message)
