"""
    组织测试套件实现 登录 与员工增删改查 接口的串联
"""
# 导包
import unittest

import app
from case.TestIHRMEmploye import TestEmployee
from case.TestIHRMUser import TestUser

# 组织测试套件对象
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
suite.addTest(TestUser("test_login_success"))  # 登录成功
suite.addTest(TestEmployee("test_emp_add"))
suite.addTest(TestEmployee("test_emp_update"))
suite.addTest(TestEmployee("test_emp_get"))
suite.addTest(TestEmployee("test_emp_delete"))

# 执行套件对象
with open(app.PRO_PATH + "/report/rep.html","wb") as f:
    runner = HTMLTestRunner(f,title="hello",description="v1.0")
    runner.run(suite)
    print("+++++")
    print("-----")
    print("_____")