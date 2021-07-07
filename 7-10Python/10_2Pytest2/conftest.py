import pytest


@pytest.fixture(scope="session")
def session():
    print("我是来自conftest的天秀！\n不管谁调我，我都只在整个测试最开始秀一遍就完事")
    yield
    print("886~")
