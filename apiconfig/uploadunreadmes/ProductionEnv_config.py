# -*- coding: utf-8 -*-
from ApiClass import *

# xuchaoxuan version 2.0
# yanglei    version 1.0  2.1

App_a = {
         "unread":     10,
         "unread1":   "",
         "correct_err1_code": 2000,
         "correct_err2_code": 4001,
         "correct_err3_code": 401,
        }
CoreServer_url  = "https://cloudus.v5.cn"

#############上传未读消息数量#######
#*******TESTCASE账号未登录*************、
#场景：token，sessionid传空
CoreServer_UploadUnreadMesTest_01                  = UploadUnreadMesTest()
#input
CoreServer_UploadUnreadMesTest_01.url                 = CoreServer_url+"/api/user/message/unread"
CoreServer_UploadUnreadMesTest_01.unread              =App_a["unread"]
#expect
CoreServer_UploadUnreadMesTest_01.error_code            =App_a["correct_err3_code"]

#*******TESTCASE参数错误*************
#场景：未读数传空
CoreServer_UploadUnreadMesTest1_01                  = UploadUnreadMesTest()
#input
CoreServer_UploadUnreadMesTest1_01.url                 = CoreServer_url+"/api/user/message/unread"
CoreServer_UploadUnreadMesTest1_01.unread              =App_a["unread1"]
#expect
CoreServer_UploadUnreadMesTest1_01.error_code            =App_a["correct_err2_code"]


