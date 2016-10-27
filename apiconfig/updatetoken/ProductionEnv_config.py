# -*- coding: utf-8 -*-
from ApiClass import *

App_a = {
         "app_id": "10000920",
         "correct_err_code1": 401,
         "correct_err_code2": 4001,
         "device_token": "推送Token"
         }

CoreServer_url  = "https://cloudus.v5.cn"


###########################更新推送Token——账号未登录#####################
##########modules里迅增一个方法——token为空，session随意赋一个值##########
#********** TESTCASE **********
CoreServer_UpdateTokenTest_01                 = UpdateTokenTest()
# input
CoreServer_UpdateTokenTest_01.url                = CoreServer_url + "/api/device/token"
CoreServer_UpdateTokenTest_01.app_id             = App_a["app_id"]
CoreServer_UpdateTokenTest_01.device_type        = "2"
CoreServer_UpdateTokenTest_01.device_token       = App_a["device_token"]
CoreServer_UpdateTokenTest_01.provider           = "2"

# expect
CoreServer_UpdateTokenTest_01.error_code        = App_a["correct_err_code1"]

##########更新推送Token——缺少参数#########
###########传参device_type赋值为空##########
#********** TESTCASE **********
CoreServer_UpdateTokenTest_02                 = UpdateTokenTest()
# input
CoreServer_UpdateTokenTest_02.url                = CoreServer_url + "/api/device/token"
CoreServer_UpdateTokenTest_02.app_id             = App_a["app_id"]
CoreServer_UpdateTokenTest_02.device_type        = ""
CoreServer_UpdateTokenTest_02.device_token       = App_a["device_token"]
CoreServer_UpdateTokenTest_02.provider           = "2"

# expect
CoreServer_UpdateTokenTest_02.error_code        = App_a["correct_err_code2"]
