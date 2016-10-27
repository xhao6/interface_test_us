# -*- coding: utf-8 -*-

# NEED TO CHANGE LIKE PRODUCTIONENC_CONFIG.PY
from workspace.cgcloud.apiconfig.mainprocess.ApiClass import *

DemoApi_url                 = "http://opentest.v5.cn:9015"
#1.##########登录##########
#********** TESTCASE **********
DemoApi_login_01            = login()
# input
DemoApi_login_01.url        = DemoApi_url + "/users/login"
DemoApi_login_01.account    = "TEST_testAccount111"

# expect
DemoApi_login_01.err_code                = 2000
DemoApi_login_01.user_id                 = 10250
DemoApi_login_01.user_v5_id              = "1b484820586211e6ba0e07a0e6f66521"
DemoApi_login_01.user_account            = "TEST_testAccount111"
DemoApi_login_01.user_sessionId          = "len of expect = 32"
DemoApi_login_01.user_nickName           = "TEST_testAccount111"
DemoApi_login_01.user_createTimeMillis   = "expect is not None"
DemoApi_login_01.user_avatar             = "http://cn.file.chatgame.me/api/file/download/2016/7/26/2/e52838d3-57f5-497a-b1ee-85cd7731fb5b.jpg"

#********** TESTCASE **********
DemoApi_login_02            = login()
# input
DemoApi_login_02.url        = DemoApi_url + "/users/login"
DemoApi_login_02.account    = "TEST_testAccount222"
DemoApi_login_02.nickName   = "Iam_login_02"

# expect
DemoApi_login_02.err_code                = 2000
DemoApi_login_02.user_id                 = 10255
DemoApi_login_02.user_v5_id              = "1c105310586211e6ba0e07a0e6f66521"
DemoApi_login_02.user_account            = "TEST_testAccount222"
DemoApi_login_02.user_sessionId          = "len of expect = 32"
DemoApi_login_02.user_nickName           = "Iam_login_02"
DemoApi_login_02.user_createTimeMillis   = "expect is not None"
DemoApi_login_02.user_avatar             = "http://cn.file.chatgame.me/api/file/download/2016/7/26/2/53398e36-4fcd-4372-bf73-c3db2b958e5b.jpg"

#********** TESTCASE **********
DemoApi_login_03            = login()
# input
DemoApi_login_03.url        = DemoApi_url + "/users/login"
DemoApi_login_03.account    = "TEST_testAccount222"
DemoApi_login_03.nickName   = "Iam_login_03"

# expect
DemoApi_login_03.err_code                = 2000
DemoApi_login_03.user_id                 = 10255
DemoApi_login_03.user_v5_id              = "1c105310586211e6ba0e07a0e6f66521"
DemoApi_login_03.user_account            = "TEST_testAccount222"
DemoApi_login_03.user_sessionId          = "len of expect = 32"
DemoApi_login_03.user_nickName           = "Iam_login_03"
DemoApi_login_03.user_createTimeMillis   = "expect is not None"
DemoApi_login_03.user_avatar             = "http://cn.file.chatgame.me/api/file/download/2016/7/26/2/53398e36-4fcd-4372-bf73-c3db2b958e5b.jpg"

#2.##########查找账户##########
#********** TESTCASE **********
DemoApi_findAccount_01         = FindAccountTest()
# input
DemoApi_findAccount_01.url     = DemoApi_url + "/users"
DemoApi_findAccount_01.account = "TEST_testAccount222"

# expect
DemoApi_findAccount_01.err_code               = 2000
DemoApi_findAccount_01.user_id                = 10255
DemoApi_findAccount_01.user_v5_id             = "1c105310586211e6ba0e07a0e6f66521"
DemoApi_findAccount_01.user_account           = "TEST_testAccount222"
DemoApi_findAccount_01.user_sessionId         = "len of expect = 32"
DemoApi_findAccount_01.user_nickName          = "Iam_login_03"
DemoApi_findAccount_01.user_createTimeMillis  = "expect is not None"
DemoApi_findAccount_01.user_avatar            = "http://cn.file.chatgame.me/api/file/download/2016/7/26/2/53398e36-4fcd-4372-bf73-c3db2b958e5b.jpg"

#3.##########创建群组##########
#********** TESTCASE **********
DemoApi_createGroup_01                  = createGroup()
# input
DemoApi_createGroup_01.url              = DemoApi_url + "/groups/"
DemoApi_createGroup_01.members_v5_id    = "1b484820586211e6ba0e07a0e6f66521" + "," + "a3766230586311e6ba0e07a0e6f66521"

# expect
DemoApi_createGroup_01.err_code             = 2000
DemoApi_createGroup_01.result_id            = "not None"
DemoApi_createGroup_01.result_v5_id         = "not None"
DemoApi_createGroup_01.result_number        = 3
DemoApi_createGroup_01.result_creator       = "generate when run testcase"
DemoApi_createGroup_01.result_name          = "defaultGroupName"
DemoApi_createGroup_01.result_createTime    = "not None"
DemoApi_createGroup_01.result_updateTime    = "not None"
DemoApi_createGroup_01.result_desc          = "defaultGroupDesc"
DemoApi_createGroup_01.result_avatar        = "http://new.image.chatgame.me/api/file/avatar/2015/11/24/8/9d6463ab-4083-4b01-a416-65e4e382ad00"
DemoApi_createGroup_01.result_member_v5_id  = DemoApi_createGroup_01.members_v5_id  #will be add the creator when run the testcase

#4.##########拉人进群##########
DemoApi_joinGroup_01                = joinGroup()
# input
DemoApi_joinGroup_01.url            = DemoApi_url + "/groups/join"
DemoApi_joinGroup_01.groupId        = "1de70ee0586211e6ba0e07a0e6f66521"
DemoApi_joinGroup_01.members_v5_id  = "a3766230586311e6ba0e07a0e6f66521"

# expect
DemoApi_joinGroup_01.err_code           = 2000
DemoApi_joinGroup_01.result_id          = 10778
DemoApi_joinGroup_01.result_v5_id       = "1de70ee0586211e6ba0e07a0e6f66521"
DemoApi_joinGroup_01.join_members_v5_id = []


CoreServer_url                  = "http://opentest.v5.cn:9102"
#1.##########获取token##########
#********** TESTCASE **********
CoreServer_getToken_01                 = getToken()
# input
CoreServer_getToken_01.url             = CoreServer_url + "/oauth/token"
CoreServer_getToken_01.client_id       = 202311
CoreServer_getToken_01.client_secret   = "9692bb155492a0c2fbc21bd9192dfdeb"
CoreServer_getToken_01.grant_type      = "client_credentials"

# expect
CoreServer_getToken_01.access_token    = "len of expect = 36"
CoreServer_getToken_01.token_type      = "bearer"
CoreServer_getToken_01.expires_in      = "not None"
CoreServer_getToken_01.scope           = "read"

#2.##########获取v5_id with sessionId##########
#********** TESTCASE **********
CoreServer_getUserIdSessionId_01    = getUserIdSessionId()
# input
CoreServer_getUserIdSessionId_01.app_user_id         = "test_testaccount123"
CoreServer_getUserIdSessionId_01.app_user_nick_name  = "IamNickName"
CoreServer_getUserIdSessionId_01.url                 = CoreServer_url + "/open/api/user/auth?"
CoreServer_getUserIdSessionId_01.header              = {}    #need Token

# expect
CoreServer_getUserIdSessionId_01.error_code          = 2000
CoreServer_getUserIdSessionId_01.user_id             = "len of expect = 32"
CoreServer_getUserIdSessionId_01.user_session_id     = "len of expect = 32"

#3.##########获取sessionId##########
#********** TESTCASE **********
CoreServer_getSessionID_01              = getSessionID()
# input
CoreServer_getSessionID_01.app_user_id  = "1b39c510553411e68dca07a0e6f66521"
CoreServer_getSessionID_01.url          = CoreServer_url + "/open/api/session/auth?"
CoreServer_getSessionID_01.header       = {}        #need Token

# expect
CoreServer_getSessionID_01.error_code       = 2000
CoreServer_getSessionID_01.user_id          = "len of expect = 32"
CoreServer_getSessionID_01.user_session_id  = "len of expect = 32"

