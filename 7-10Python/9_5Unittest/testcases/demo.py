import unittest


class Search:
    def search(self):
        print("search")
        return True


class Demo2(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")
        cls.search = Search()

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    def setUp(self) -> None:
        print("setUp")

    def tearDown(self) -> None:
        print("tearDown")

    def test_upper(self):
        self.search.search()
        self.assertEqual("foo".upper(), "FOO", "判断大小写一致")

    def test_a(self):
        print("a")

    def test_b(self):
        print("b")


class Demo3(unittest.TestCase):
    def test_c(self):
        print("c")

    def test_d(self):
        print("d")


# terminal 执行 python demo.py
# if __name__ == '__main__':
    """方法1：执行当前文件全部的unittest测试用例"""
    # unittest.main()

    """方法2:执行指定的测试用例，将要执行的测试用例添加到测试套件里面，批量执行测试方法"""
    # suite = unittest.TestSuite()
    # suite.addTest(Demo2("test_a"))
    # suite.addTest(Demo2("test_upper"))
    # unittest.TextTestRunner().run(suite)

    """方法3：执行某个测试类，将测试类添加到测试套件里，批量执行测试类"""
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(Demo2)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(Demo3)
    # suite = unittest.TestSuite([suite1, suite2])
    # unittest.TextTestRunner().run(suite)

    """方法4：run.py"""
