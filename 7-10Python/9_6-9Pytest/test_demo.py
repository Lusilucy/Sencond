import allure
import pytest
import yaml


@pytest.fixture()
def login():
    print("start_login")
    yield "I'm logining!"
    print("end_login")


def get_data():
    with open("./testdemodata.yaml") as f:
        return yaml.safe_load(f)


@allure.feature("Demo1")
class TestDemo:
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("a")
    @allure.title("a_title")
    @allure.testcase("https://www.baidu.com", "测试案例链接")
    def test_a(self, login):
        with allure.step("a"):
            print("a")
        with allure.step("login"):
            print(f"The login message is '{login}'")
        with allure.step("aa"):
            print("aa")

    @allure.story("b")
    @pytest.mark.usefixtures("login")
    def test_b(self):
        allure.attach('测试attach', 'attach文件', allure.attachment_type.TEXT)
        print("b")

    def test_c(self):
        print("c")

    @pytest.mark.parametrize("a,b", [[1, 2], [3, 4]])
    def test_add(self, a, b):
        return print(a+b)

    @pytest.mark.parametrize(
        "a,b",
        get_data()["argvalues"],
        ids=get_data()["ids"]
    )
    def test_add2(self, a, b):
        return print(a+b)


class TestDemo2:
    @pytest.mark.parametrize(
        "env",
        yaml.safe_load(open("./env.yml"))
    )
    def test_demo(self, env):
        if "test" in env:
            print("这是在测试环境")
            print(f"测试环境的IP是：{env['test']}")
        elif "dev" in env:
            print("这是在开发环境")
            print(f"开发环境的IP是：{env['dev']}")


if __name__ == '__main__':
    pytest.main(["-vs", "-k test_"])
    pytest.main(["demo.py::TestDemo::test_add2", "-vs"])
