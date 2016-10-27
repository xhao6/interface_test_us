# -*- coding: utf-8 -*-
from ApiClass import *

App_a = {
         "tcp_server": ["54.186.79.170:5223", "52.33.180.199:443", "54.186.79.170:8080", "52.33.180.199:5223",
                        "54.186.79.170:443", "52.33.180.199:8080"],
         "file_server": ["https://api.chatgame.me"],
         "device_token": "推送Token",
         "correct_err_code1": 401
         }

CoreServer_url  = "https://cloudus.v5.cn"

################获取可用的TCP服务器、文件服务器——账号未登录##############
##########modules里迅增一个方法——token为空，session随意赋一个值##########
#********** TESTCASE **********
CoreServer_GetServerTest_01                 = GetServerTest()
# input
CoreServer_GetServerTest_01.url                = CoreServer_url + "/api/server/addr"

# expect
CoreServer_GetServerTest_01.error_code            = App_a["correct_err_code1"]

