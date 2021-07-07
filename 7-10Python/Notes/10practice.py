# TODO Pytest 实战2✅
"""1、fixture用法✅"""
# 10_2Pytest2/test_fixture.py

"""2、autouse✅"""
# 同上

"""3、作用域✅"""
# 同上+10_2Pytest2/test_sessin

"""4、yield✅"""
# 同../上

"""5、conftest✅"""
# 10_2Pytest2/conftest.py

"""6、fixture参数化✅"""
# 同../上

"""7、实用插件"""
# 1）ordering✅
# @pytest.mark.run(order=1)

# 2）pytest-ramdom-order✅
# pytest test_fixture.py -v --random-order
# Using --random-order-bucket=module
# Using --random-order-seed=421109

# todo pytest插件
# 3）dependency❓
# 4）xdist❓

"""8、测试报告✅"""
# 1）pytest-html✅
#  pytest -v --html report.html --self-contained-html

# 2）allure✅

"""9、其他"""
# pytest.ini✅
# 10_2Pytest2/test_ini/

# todo pytest插件
# pytest高级用法（自制插件）❓

"""作业"""
"""课堂练习✅"""
# 将上节课的作业，setup/teardown 改造成fixture的形式。
# 10_2Pytest2/HomeWork

"""
课后作业✅
1、上节课的作业，使用fixture 实现setup/teardown 功能，
2、实现 参数化的功能
3、生成测试 报告
"""
# 10_2Pytest2/HomeWork
