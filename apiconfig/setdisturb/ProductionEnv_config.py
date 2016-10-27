# -*- coding: utf-8 -*-
from ApiClass import *
App_a = {
         "correct_err_code": 2000,
         "correct_err1_code":401,
        }
CoreServer_url  = "https://cloudus.v5.cn"

#########设置免打扰##########
#*********不开启免打扰*********
#*********TESTCASE账户未登录*********
#场景：token，sessionid传空
CoreServer_SetDisturbTest_01                     = SetDisturbTest()
#input
CoreServer_SetDisturbTest_01.url            = CoreServer_url+"/api/user/disturb"
CoreServer_SetDisturbTest_01.disable        ="no"

#expect
CoreServer_SetDisturbTest_01.error_code      =App_a["correct_err1_code"]

#########设置免打扰##########
#*********开启免打扰*********
#*********TESTCASE账户未登录*********
#场景：token，sessionid传空
CoreServer_SetDisturbTest_02                     = SetDisturbTest()
#input
CoreServer_SetDisturbTest_02.url            = CoreServer_url+"/api/user/disturb"
CoreServer_SetDisturbTest_02.disable        ="yes"

#expect
CoreServer_SetDisturbTest_02.error_code      =App_a["correct_err1_code"]