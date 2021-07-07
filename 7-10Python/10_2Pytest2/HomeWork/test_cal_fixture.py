import allure


@allure.link("https://github.com/Lusilucy/Sencond/tree/master/7-10Python/10_2Pytest2/HomeWork", name="源码链接")
@allure.feature("计算器")
class TestCal:
    @allure.story("加法")
    def test_add_int(self, cal, get_add_i):
        with allure.step("判断整数相加结果正确"):
            assert cal.add(get_add_i[0], get_add_i[1]) == get_add_i[2]

    @allure.story("加法")
    @allure.title("加法-小数-{get_add_f[3]}")
    def test_add_float(self, cal, get_add_f):
        with allure.step("判断小数相加结果正确"):
            assert round(cal.add(get_add_f[0], get_add_f[1]), 2) == get_add_f[2]

    @allure.story("除法")
    def test_div(self, cal, get_div):
        try:
            with allure.step("判断相除结果正确"):
                assert cal.div(get_div[0], get_div[1]) == get_div[2]
        except ZeroDivisionError as z:
            with allure.step("除数为0"):
                print(z)
