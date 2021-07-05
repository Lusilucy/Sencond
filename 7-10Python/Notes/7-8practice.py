# ✅TODO Python 基础语法
import json
import random

# 实战部分
import sys

"""三目表达式✅"""
# x = 1
# # if x > 0 :
# #     print("x>0")
# # else:
# #     print("x<=0")
# print("x>0") if x > 0 else print("x<=0")

"""random随机数✅"""
# a = random.random()
# b = random.randint(1, 10)
# c = random.randrange(2, 10, 2)
# list1 = ["a", "b", "c"]
# d = random.choice(list1)
# print(a)
# print(b)
# print(c)
# print(d)


"""调用父类方法（super()）✅"""


class Father:
    def father(self):
        print("a")


class Son(Father):
    def father(self):
        print("b")
        Father().father()
        super().father()


# Son().father()


"""查看元素开辟的空间位置（id）✅"""
# a = 1
# b = "bbb"
# c = ["a", 2, [1, "b"]]
# d = {"a": 1, "b": 2}
# print(id(a))
# print(id(b))
# print(id(c))
# print(id(d))


"""闭包函数✅"""


def out_func():
    print("out_func")

    def in_func():
        print("in_func")

    return in_func


# out_func()
# print("--------")
# print(out_func())
# print("--------")
# out_func()()
# print("--------")
# print(out_func()())


# 基础课程
"""字符串转译符、忽略转译符、索引、切片✅"""
# a = "niofaif\njflak;dfk"
# b = "japjgkonfjk\\njfoeijfiao"
# c = r"fjolij\njlfkdjlj"
#
# print(a)
# print("------------")
# print(b)
# print("------------")
# print(c)
# print("------------")
# print(a[7])
# print("------------")
# print(a[3:5])
# print("------------")
# print(a[1:16:2])
# print("------------")
# print(a[0::2])
# print("------------")
# print(a[::2])

"""while，else✅"""
# a = 0
# while a < 6:
#     a += 1
#     print(a)
# else:
#     print(f"a的值{a} > 5")

"""仅限关键字参数✅"""
# def fun1(a, b, *, c):
#     return print(a, b, c)
#
# fun1(1, 2, c=3)

"""lambda表达式✅❓"""
# fun2 = lambda a, b: print(a + b)
# fun2(3, 4)

"""列表✅"""
# list1 = [-1] * 3
# print(list1)
# list1[0] = 1
# print(list1)
# print(list1.count(-1))
# list1[-1] = 3
# print(list1)
# list1.append("a")
# print(list1)
# list1.insert(0, "top")
# print(list1)
# b = list1[:]
# # b = list1.copy()
# list1.remove("top")
# print(list1)
# print(list1.pop(-1))
# print(list1)
# print(list1.reverse())
# print(list1)
# print(list1.sort())
# print(list1)
# list1.sort(reverse=True)
# print(list1)
# print(list1.index(-1, 1, 3))
# # del list1[:]
# list1.clear()
# print(list1)
# print(b)
# list1.extend(i for i in range(5))
# # a =[]
# # def fun3():
# #     for i in range(5):
# #         a.append(i)
# #     return a
#
# # list1[len(list1):] = fun3()
# print(list1)

"""列表推导式✅"""
# list2 = [i for i in range(10)]
# list3 = [i**2 for i in range(10)]
# list4 = [i**3 for i in range(0, 5) if i != 1]
#
# print(list2)
# print(list3)
# print(list4)

"""集合✅"""
# set1 = set()
# set2 = {1, 2}
# a = {1, 2, 3}
# b = {2, 4, 3}
# # 并集
# print(a.union(b))
# # 交集
# print(a.intersection(b))
# # 差集
# print(a.difference(b))
#
# print(type(set1))
# print(type(set2))
# print(len(set1))
# print(len(set2))
# print(set1)
# print(set2)
# # 不重复的无序集合
# print({i for i in "hiauhgoijofigapj"})
# # 取字符串中不重复集合
# c = "oiajofijapjpgnpivajtuoiepurtonjcpjvpigj"
# print(set(c))

"""字典✅"""
# dict1 = {"a": 1, "b": 2}
# dict2 = dict(a="aa", b=2)
#
#
# print(type(dict1))
# print(dict1)
# print(type(dict2))
# print(dict2)
# print(dict1.keys())
# print(dict1.values())
# print(dict1.pop("a"))
# print(dict1)
# print(dict2.popitem())
# print(dict2)
#
# a = {}
# b = a.fromkeys([1, 2, 3], "a")
# print(b)

"""字典推导式✅"""
# print({i: i**2 for i in range(1, 10)})

"""sys.path✅"""
# print(sys.path)

"""字面量插值 upper、lambda表达式✅"""
# # &1
# a = 111
# b = "abc"
# c = 1.111
# print("my name is %s,my age is %d,%f" % (b, a, c))
# # &2
# name = "lili"
# age = 20
# list4 = [1, 2, 3]
# dic4 = {"name": "tom", "gender": "male"}
# print("my name is {}, age is {}".format(name, age))
# print("my name is {0}, age is {1},{0}{1}".format(name, age))
# print("my name is {}, age is {}".format(list4, dic4))
# print("we name: {}、{} and {}".format(*list4))
# print("my name is {name}, age is {gender}".format(**dic4))
# # &3
# print(f"my name is \n {name}, age is {age}")
# print(f"my name is {name.upper()}")
# print(f"result is {(lambda x:x+1)(2)}")

"""json格式转化✅"""
# a = json.dumps([1, 2, 3])
# print(a)
# print(json.loads(a))
# json.dump("abc", open("./data.json", "w"))
# print(json.load(open("./data.json")))

"""try、except、else、finally、raise✅"""


def div(a, b):
    return a / b


# # 未捕获异常走else分支，再finally
# try:
#     print(div(1, 1))
# except:
#     print("This is a exception!")
#     raise ZeroDivisionError("被除数不能为0")
# else:
#     print("另一分支")
# finally:
#     print("结束啦")

# try:
#     list1 = [1, 2, 3]
#     print(list1[3])
#     print(div(1, 0))
# except ZeroDivisionError as e:
#     print(e)
#     print("This is a exception!")
#     # raise ZeroDivisionError("被除数不能为0")
# except IndexError as e1:
#     print(e1)
# else:
#     print("另一分支")
# finally:
#     print("结束啦")

# try:
#     list1 = [1, 2, 3]
#     print(list1[3])
#     print(div(1, 0))
# except Exception as e:
#     print("There is a exception!")
#     print(e)
# else:
#     print("另一分支")
# finally:
#     print("结束啦")

"""自定义异常✅"""
# class MyError(Exception):
#     def __init__(self, value):
#         self.value = value
#
#     def __str__(self):
#         return repr(self.value)
#
# raise MyError("This is my Error")

"""类方法（装饰器+cls）✅"""

# class ClassFun:
#     def fun1(self):
#         print("fun1")
#
#     @classmethod
#     def fun2(cls):
#         print("fun2")
#
#
# ClassFun.fun2()
# ClassFun().fun2()
# ClassFun().fun1()


"""查看类中所有属性及方法(dir)✅"""
# # 找出当前模块定义的对象
# print(dir())
# print(dir(Son))
# print(dir(Son().father()))
# # 找出参数模块定义的对象
# print(dir(random))

"""查看python内置函数（locals()）✅"""
# print(locals())
