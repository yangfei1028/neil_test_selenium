# !/usr/bin/python
#coding: utf-8

"""
@Author: Well
@Date: 2014 - 06 - 25
"""


from selenium import webdriver
from time import sleep

# base_url = "http://www.sohu.com/"
# browser = webdriver.Chrome()
# browser.get(base_url)
# browser.find_elements_by_xpath("//li[@class='red']/a[@href='http://2014.sohu.com/']").click()
# sleep(5)
# browser.quit()

base_url = "http://file.ws.126.net/3g/client/netease_newsreader_android.apk"
browser = webdriver.Chrome()
webdriver.ChromeOptions
browser.get(base_url)
