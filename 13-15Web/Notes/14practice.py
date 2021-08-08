# TODO Selenium 1 基础+进阶✅
"""14-2 selenium IDE 录制✅"""
# 13-15Web/14BasicSelenium/test_ide.py

"""14-4 等待✅"""
# 显示等待、隐式等待、直接等待
# 显示等待自定义until函数
# ../14BasicSelenium/test_selenium1.py

"""14-5 定位✅"""
# xpath定位->console✅
# $x("//*[id='s_tab']//a(1)")
# $x("//*[id='s_tab']//a(last())")

# CSS定位->console✅
# $("#s_tab a:nth-child(2)")

"""14-6 进阶✅️"""
# ActionChains
# 1 click、double_click、context_click✅
# 13-15Web/14BasicSelenium/test_js.py

# 2 move_to_element✅
# 13-15Web/14BasicSelenium/test_selenium1.py

# 3 drag_and_drop✅
# 13-15Web/14BasicSelenium/test_js.py
from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
action = ActionChains(driver)
ele1 = driver.find_element_by_id("dragger")
ele2 = driver.find_element_by_css_selector(".item:nth-child(4)")
action.drag_and_drop(ele1, ele2).perform()
sleep(3)
driver.quit()

# 4 key_down、key_up、Keys.CONTROL…✅
# 13-15Web/14BasicSelenium/test_js.py

# TouchActions✅
# 13-15Web/14BasicSelenium/test_selenium1.py

"""14-7 frame✅"""
# 多窗口✅
# 13-15Web/14BasicSelenium/test_selenium1.py
# test_window

# frame✅
# 13-15Web/15_1-3Notes/test_inputfile_alert.py

"""14-8 兼容性测试✅"""
# 13-15Web/14BasicSelenium/test_selenium2.py

"""14-9 js✅"""
# console✅
"""
1.页面弹窗
window.alert("hello world")
2.页面性能
JSON.stringify(performance.timing)
3.页面标题
document.title
4.页面属性值
document.getElementById("kw").value
5.滑动页面
document.documentElement.scrollTop
6.去掉属性值
a = document.getElementById("train_date")
a.removeAttribute("readonly")
a.value = "2000-02-02"
"""
# selenium脚本✅
# 13-15Web/14BasicSelenium/test_js.py
