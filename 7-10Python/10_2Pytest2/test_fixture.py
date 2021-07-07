import pytest


@pytest.fixture(params=["tom", "jerry", "Kitty"], ids=["name1", "name2", "name3"])
def login(request):
    print("开始登录")
    print(f"登录用户为{request.param}")
    yield request.param
    print("结束登录")


@pytest.fixture
def connect_db():
    print("连接数据库")
    yield "数据库用户名，密码"
    print("关闭数据库")


@pytest.fixture(autouse=True)
def auto():
    print("我要在开始之前自动执行一下子")
    yield
    print("秀完了")


@pytest.fixture(scope="module")
def module():
    print("不管谁调我，我都只在整个模块module秀一遍就完事")
    yield
    print("还想看？没有了！跪安吧！")


def perform():
    for i in range(1, 10):
        print("楼上的太秀了")
        yield print(i, "我只想做个安静的美女子")
        print("hahahaha")


class TestFixture:
    @pytest.mark.run(order=3)
    def test_demo1(self, login, connect_db, session):
        print("一顿操作猛如虎")
        print(connect_db)

    @pytest.mark.run(order=1)
    @pytest.mark.usefixtures("connect_db")
    def test_demo2(self):
        print("装饰器方法")

    @pytest.mark.run(order=2)
    def test_demo3(self):
        print("我什么都没加")

    def test_demo4(self, session, module):
        print("看秀儿")

    def test_demo5(self, module):
        print("继续看秀儿")

    def test_yield(self):
        p = perform()
        next(p)
        print("---------我是个分割线----------")
        next(p)
        print("---------我是个分割线----------")
        next(p)
        print("---------我是个分割线----------")
        next(p)
        print("---------我是个分割线----------")
        next(p)
        print("---------我是个分割线----------")
        next(p)
        print("---------我是个分割线----------")
        next(p)
        print("---------我是个分割线----------")
        next(p)
        print("---------我是个分割线----------")
        next(p)