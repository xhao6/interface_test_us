# -*- coding: utf-8 -*-
from ApiClass import *

# xuchaoxuan version 2.0
# yanglei    version 1.0  2.1

App_a = {"app_id": "10000920",
         "app_secret": "7499453344773ceed176118398dcdcc9",
         "grant_type": "client_credentials",
         "unread": 10,
         "file": "v5vcloud_api_main_tests.py",
         "region_code": "0001",
         "app_id": "10000920",
         "md5": "014CAF6FF12D0E3E0CA2E43AD498AD9A",
         "accounts":
             {"account_01": {"id": "TEST_testAccount111",
                             "nickName": "Iam_login_05",
                             "user_avatar": "http://cn.file.chatgame.me/api/file/download/2016/7/26/2/b999baff-45b4-4147-957e-8c05d2c55b16.jpg"
                             },
              "account_02": {"id": "TEST_testAccount222",
                             "nickName": "Iam_login_03",
                             "user_avatar": "http://cn.file.chatgame.me/api/file/download/2016/7/26/2/5c3d14cc-9fc0-40d5-8b04-9b02ca69f5ff.jpg"
                             },
              "account_03": {"id": "TEST_testAccount333",
                             "nickName": "Iam_login_33",
                             }
              },
         "groups":
             {"group_01": {"members": "TEST_testAccount222" + "," + "TEST_testAccount333",
                           "creator": "TEST_testAccount111",
                           "group_name": "test_groupName",
                           "group_desc": "test_groupDesc",
                           "group_avatar": "http://new.image.chatgame.me/api/file/avatar/2015/11/24/8/9d6463ab-4083-4b01-a416-65e4e382ad00",
                           "group_id": "c1b657e0805f11e6a3e37ddd1535be6d",
                           "group_id1": "c0e40610736111e6abbb819403d79ace1",
                           "group_detail":1,
                           }
              },
         "correct_err_code": 2000,
         "messages":
             {"last_message_id": 6167584608000294912,
              "messages_id": "6166846405551210496",
              "messages_type": "SYSTEM_NOTIFY",
              "messages_create_time": "1470290757551",
              "messages_sender": "643a2d6059f611e6afa2819403d79ace",
              "messages_conversation_id": "defaultGroupName：Iam_login_03 invites  to join the group chat",
              "messages_meta_push_content": "Iam_login_05",
              "messages_meta_cmsgid": "826a30ce-1cc6-4c8b-a243-61f944e173e6",
              "messages_receiver": "b3d590c0595c11e6afa2819403d79ace"
              },
         "chatrooms":
             {"live": "",
              "count": "",
              "id": "init",
              "desc": "新人直播, 求关注 进来的宝宝点关注 谢谢",
              "cover_url": "http://cn.file.chatgame.me/api/file/download/2016/7/26/7/98a0249c-8b5f-4171-90c4-df1e7b18b226.png",
              },

         "tcp_server": ["54.186.79.170:5223", "52.33.180.199:443", "54.186.79.170:8080", "52.33.180.199:5223",
                        "54.186.79.170:443", "52.33.180.199:8080"],
         "file_server": ["https://api.chatgame.me"],
         "device_token": "推送Token"

         }


CoreServer_url  = "https://cloudus.v5.cn"
File_url = "http://cn.api.chatgame.me"
#1.##########获取token##########
#********** TESTCASE **********
CoreServer_getToken_01                 = getToken()
# input
CoreServer_getToken_01.url             = CoreServer_url + "/oauth/token"
CoreServer_getToken_01.client_id       = App_a["app_id"]
CoreServer_getToken_01.client_secret   = App_a["app_secret"]
CoreServer_getToken_01.grant_type      = App_a["grant_type"]

# expect
CoreServer_getToken_01.access_token    = "len of expect = 36"
CoreServer_getToken_01.token_type      = "bearer"
CoreServer_getToken_01.expires_in      = "not None"
CoreServer_getToken_01.scope           = "read"

#2.##########获取id with sessionId##########
#********** TESTCASE **********
CoreServer_getUserIdSessionId_01    = getUserIdSessionId()
# input
CoreServer_getUserIdSessionId_01.app_user_id         = App_a["accounts"]["account_01"]["id"]
CoreServer_getUserIdSessionId_01.app_user_nick_name  = App_a["accounts"]["account_01"]["nickName"]
CoreServer_getUserIdSessionId_01.url                 = CoreServer_url + "/open/api/user/auth?"
CoreServer_getUserIdSessionId_01.header              = {}    #need Token

# expect
CoreServer_getUserIdSessionId_01.error_code          = App_a["correct_err_code"]
CoreServer_getUserIdSessionId_01.user_id             = App_a["accounts"]["account_01"]["id"]
CoreServer_getUserIdSessionId_01.user_session_id     = "len of expect = 32"

#3.##########获取sessionId##########
#********** TESTCASE **********
CoreServer_getSessionID_01              = getSessionID()
# input
CoreServer_getSessionID_01.app_user_id  = App_a["accounts"]["account_01"]["id"]
CoreServer_getSessionID_01.url          = CoreServer_url + "/open/api/session/auth?"
CoreServer_getSessionID_01.header       = {}        #need Token

# expect
CoreServer_getSessionID_01.error_code       = App_a["correct_err_code"]
CoreServer_getSessionID_01.user_id          = App_a["accounts"]["account_01"]["id"]
CoreServer_getSessionID_01.user_session_id  = "len of expect = 32"

#********** TESTCASE **********
CoreServer_getSessionID_03              = getSessionID()
# input
CoreServer_getSessionID_03.app_user_id  = App_a["accounts"]["account_03"]["id"]
CoreServer_getSessionID_03.url          = CoreServer_url + "/open/api/session/auth?"
CoreServer_getSessionID_03.header       = {}        #need Token

# expect
CoreServer_getSessionID_01.error_code       = App_a["correct_err_code"]
CoreServer_getSessionID_01.user_id          = App_a["accounts"]["account_01"]["id"]
CoreServer_getSessionID_01.user_session_id  = "len of expect = 32"

##########获取可用的TCP服务器、文件服务器#########
#********** TESTCASE **********
CoreServer_GetServerTest_01                 = GetServerTest()
# input
CoreServer_GetServerTest_01.url                = CoreServer_url + "/api/server/addr"

# expect
CoreServer_GetServerTest_01.tcp_server      = App_a["tcp_server"]
CoreServer_GetServerTest_01.file_server     = App_a["file_server"]

##########更新推送Token#########
#********** TESTCASE **********
CoreServer_UpdateTokenTest_01                 = GetServerTest()
# input
CoreServer_UpdateTokenTest_01.url                = CoreServer_url + "/api/device/token"
CoreServer_UpdateTokenTest_01.app_id             = App_a["app_id"]
CoreServer_UpdateTokenTest_01.device_type        = "2"
CoreServer_UpdateTokenTest_01.device_token       = App_a["device_token"]
CoreServer_UpdateTokenTest_01.provider           = "2"

# expect
CoreServer_UpdateTokenTest_01.file_server        = App_a["correct_err_code"]

#########获取IP###########
CoreServer_GetLocationTest_01                 = GetLocationTest()
#input
CoreServer_GetLocationTest_01.url            = CoreServer_url+"/api/user/location"

#expect
CoreServer_GetLocationTest_01.lat            =""
CoreServer_GetLocationTest_01.lon            =""

###########更新用户昵称#########
#********** TESTCASE ************
CoreServer_UpdateNicknameTest_01           = UpdateNicknameTest()
#input
CoreServer_UpdateNicknameTest_01.url       = CoreServer_url + "/open/api/user/update"
CoreServer_UpdateNicknameTest_01.app_user_id = App_a["accounts"]["account_01"]["id"]
CoreServer_UpdateNicknameTest_01.app_user_nick_name = App_a["accounts"]["account_01"]["nickName"]

#expect
CoreServer_UpdateNicknameTest_01.error_code   = App_a["correct_err_code"]

##########创建群组##########
#********** TESTCASE **********
CoreServer_CreatGroupTest_02                    = CreatGroupTest()
# input
CoreServer_CreatGroupTest_02.url                = CoreServer_url + "/open/api/group/create"

CoreServer_CreatGroupTest_02.groupInfo          = App_a["groups"]["group_01"]
# CoreServer_CreatGroupTest_02.members_user_id    = App_a["groups"]["group_01"]["members"]
# CoreServer_CreatGroupTest_02.name               = App_a["groups"]["group_01"]["group_name"]
# CoreServer_CreatGroupTest_02.desc               = App_a["groups"]["group_01"]["group_desc"]

# expect
CoreServer_CreatGroupTest_02.result_id            = "not None"
CoreServer_CreatGroupTest_02.result_number        = 3
CoreServer_CreatGroupTest_02.result_creator       = App_a["groups"]["group_01"]["creator"]
CoreServer_CreatGroupTest_02.result_name          = App_a["groups"]["group_01"]["group_name"]
CoreServer_CreatGroupTest_02.result_createTime    = "not None"
CoreServer_CreatGroupTest_02.result_updateTime    = "not None"
CoreServer_CreatGroupTest_02.result_desc          = App_a["groups"]["group_01"]["group_desc"]
CoreServer_CreatGroupTest_02.result_member_user_id  = CoreServer_CreatGroupTest_02.result_member_user_id

##########加入群组##########
#********** TESTCASE **********
CoreServer_JoinGroupTest_01                 = JoinGroupTest()
# input
CoreServer_JoinGroupTest_01.url             = CoreServer_url + "/open/api/group/join"


CoreServer_JoinGroupTest_01.groupInfo         = App_a["groups"]["group_01"]
# CoreServer_JoinGroupTest_01.groupId         = App_a["groups"]["group_01"]["group_id"]

CoreServer_JoinGroupTest_01.members_user_id = App_a["accounts"]["account_01"]["id"]

# expect
CoreServer_JoinGroupTest_01.error_code            = App_a["correct_err_code"]
CoreServer_JoinGroupTest_01.join_members_user_id  = App_a["accounts"]["account_01"]["id"]
#CoreServer_JoinGroupTest_01.nickname            = "TEST_testAccount114"
#CoreServer_JoinGroupTest_01.createTime          = "1470387712169"

##########更新群组##########
#********** TESTCASE **********
CoreServer_UpdateGroupTest_01                = UpdateGroupTest()
#input
CoreServer_UpdateGroupTest_01.groupInfo     =App_a["groups"]["group_01"]
CoreServer_UpdateGroupTest_01.url          =CoreServer_url + "/open/api/group/update"


#expect
CoreServer_UpdateGroupTest_01.error_code   = App_a["correct_err_code"]

###########获取群组信息##########
#********** TESTCASE *************
CoreServer_GetGroupInforTest_01                      = GetGroupInforTest()
#input
CoreServer_GetGroupInforTest_01.url                  = CoreServer_url + "/open/api/group/get?"
CoreServer_GetGroupInforTest_01.groupInfo             = App_a["groups"]["group_01"]
#CoreServer_GetGroupInforTest_01.detail               = 1
#expect
CoreServer_GetGroupInforTest_01.error_code             = App_a["correct_err_code"]
CoreServer_GetGroupInforTest_01.result_id            = "not None"
CoreServer_GetGroupInforTest_01.result_creator       = App_a["groups"]["group_01"]["creator"]
CoreServer_GetGroupInforTest_01.result_create_time   = "not None"
CoreServer_GetGroupInforTest_01.result_update_time   = "not None"
CoreServer_GetGroupInforTest_01.result_desc          = App_a["groups"]["group_01"]["group_desc"]
CoreServer_GetGroupInforTest_01.result_name          = App_a["groups"]["group_01"]["group_name"]
CoreServer_GetGroupInforTest_01.result_number        = 3
CoreServer_GetGroupInforTest_01.result_memeber_user_id = CoreServer_GetGroupInforTest_01.result_memeber_user_id

##########拉取用户的离线消息#########
#********** TESTCASE **********
CoreServer_GetOfflineMessagesTest_01                 = GetOfflineMessagesTest()
# input
CoreServer_GetOfflineMessagesTest_01.url                = CoreServer_url + "/api/user/message/msg_snap?"
CoreServer_GetOfflineMessagesTest_01.last_message_id    = App_a["messages"]["last_message_id"]
CoreServer_GetOfflineMessagesTest_01.length             = "1"

# expect
CoreServer_GetOfflineMessagesTest_01.messages_id                  = App_a["messages"]["messages_id"]
CoreServer_GetOfflineMessagesTest_01.messages_content             = ""
CoreServer_GetOfflineMessagesTest_01.messages_type                = App_a["messages"]["messages_type"]
CoreServer_GetOfflineMessagesTest_01.messages_create_time         = App_a["messages"]["messages_create_time"]
CoreServer_GetOfflineMessagesTest_01.messages_sender              = App_a["messages"]["messages_sender"]
CoreServer_GetOfflineMessagesTest_01.messages_receiver_type       = "2"
CoreServer_GetOfflineMessagesTest_01.messages_conversation_id     = App_a["messages"]["messages_conversation_id"]
CoreServer_GetOfflineMessagesTest_01.messages_meta_entity_format  = "2"
CoreServer_GetOfflineMessagesTest_01.messages_meta_push_content  = App_a["messages"]["messages_meta_push_content"]
CoreServer_GetOfflineMessagesTest_01.messages_meta_cmsgid         = App_a["messages"]["messages_meta_cmsgid"]
CoreServer_GetOfflineMessagesTest_01.messages_receiver            = App_a["messages"]["messages_receiver"]
CoreServer_GetOfflineMessagesTest_01.messages_secret              = "0"
CoreServer_GetOfflineMessagesTest_01.messages_room_id             = ""

#############上传未读消息数量#######
#*******TESTCASE*************
CoreServer_UploadUnreadMesTest_01                  = UploadUnreadMesTest()
#input
CoreServer_UploadUnreadMesTest_01.url                 = CoreServer_url+"/api/user/message/unread"
CoreServer_UploadUnreadMesTest_01.unread              =App_a["unread"]

#expect
CoreServer_UploadUnreadMesTest_01.error_code            =App_a["correct_err_code"]

##########判断上传的文件是否已经存在####
###########TESTCASE####################
CoreServer_IsFileExistTest_01 = IsFileExistTest()
#input
CoreServer_IsFileExistTest_01.url = File_url+"/api/file/exist?"
CoreServer_IsFileExistTest_01.md5 = App_a["md5"]
CoreServer_IsFileExistTest_01.app_id = App_a["app_id"]
CoreServer_IsFileExistTest_01.region_code = App_a["region_code"]
#expect
CoreServer_IsFileExistTest_01.is_exist = 0
# CoreServer_IsFileExistTest_01.file_url = "not None"
CoreServer_IsFileExistTest_01.error_code = App_a["correct_err_code"]

###########上传语音，文件#########
#********** TESTCASE ************
CoreServer_UploadFileTest_01     =  UploadFileTest()
#input
CoreServer_UploadFileTest_01.url   = CoreServer_url + "/api/file/upload"
CoreServer_UploadFileTest_01.file  = App_a["file"]
CoreServer_UploadFileTest_01.app_id = App_a["app_id"]
CoreServer_UploadFileTest_01.region_code = App_a["region_code"]
#expect
CoreServer_UploadFileTest_01.file_id  = "not None"
CoreServer_UploadFileTest_01.file_url = "not None"

#########设置免打扰##########
#*********不开启免打扰*********
CoreServer_SetDisturbTest_01                     = SetDisturbTest()
#input
CoreServer_SetDisturbTest_01.url            = CoreServer_url+"/api/user/disturb"
CoreServer_SetDisturbTest_01.disable        ="no"

#expect
CoreServer_SetDisturbTest_01.error_code      =App_a["correct_err_code"]

#########设置免打扰##########
#*********开启免打扰*********
CoreServer_SetDisturbTest_02                     = SetDisturbTest()
#input
CoreServer_SetDisturbTest_02.url            = CoreServer_url+"/api/user/disturb"
CoreServer_SetDisturbTest_02.disable        ="yes"

#expect
CoreServer_SetDisturbTest_02.error_code      =App_a["correct_err_code"]

#########移除群成员#########
#*********TESTCASE************
CoreServer_removeGroupMemberTest_01                     = RemoveGroupMemberTest()
#input
CoreServer_removeGroupMemberTest_01.url                 = CoreServer_url + "/open/api/group/remove"
CoreServer_removeGroupMemberTest_01.groupInfo            = App_a["groups"]["group_01"]
CoreServer_removeGroupMemberTest_01.member_v5_id        = App_a["accounts"]["account_02"]["id"]

#expect
CoreServer_removeGroupMemberTest_01.error_code            = App_a["correct_err_code"]
CoreServer_removeGroupMemberTest_01.error               = None

##########解散群组##########
#********** TESTCASE **********
CoreServer_DissolveGroupTest_01                 = DissolveGroupTest()
# input
CoreServer_DissolveGroupTest_01.url             = CoreServer_url + "/open/api/group/exit"
CoreServer_DissolveGroupTest_01.groupInfo         = App_a["groups"]["group_01"]

# expect
CoreServer_DissolveGroupTest_01.error_code            = App_a["correct_err_code"]

############退出群组#########
CoreServer_ExitGroupTest_01                     = ExitGroupTest()
#input
CoreServer_ExitGroupTest_01.url             = CoreServer_url + "/open/api/group/exit"
CoreServer_ExitGroupTest_01.groupInfo        = App_a["groups"]["group_01"]

# expect
CoreServer_ExitGroupTest_01.error_code           = App_a["correct_err_code"]

#############创建聊天室##########
CoreServer_CreatChatroomTest_01                   =CreatChatroomTest()
#input
CoreServer_CreatChatroomTest_01.url              =CoreServer_url+"/api/mcu/chatroom/create"
CoreServer_CreatChatroomTest_01.chatroomInfo     =App_a["chatrooms"]
#CoreServer_CreatChatroomTest_01.desc             =App_a["chatrooms"]["chatroom_desc"]
CoreServer_CreatChatroomTest_01.app_id            =App_a["app_id"]

CoreServer_CreatChatroomTest_01.error_code       =App_a["correct_err_code"]

#########获取聊天室列表############
CoreServer_GetChatroomList_01                      =GetChatroomListTest()
#input
CoreServer_GetChatroomList_01.url                  =CoreServer_url+"/api/mcu/chatroom/list?"
CoreServer_GetChatroomList_01.chatroomInfo         =App_a["chatrooms"]
#CoreServer_GetChatroomList_01.live                 =""
#CoreServer_GetChatroomList_01.count                =""
CoreServer_GetChatroomList_01.app_id            =App_a["app_id"]

#expect
CoreServer_GetChatroomList_01.error_code            =App_a["correct_err_code"]

##############获取聊天室信息#############
CoreServer_GetChatroomInfor_01                       =GetChatroomInforTest()
#input
CoreServer_GetChatroomInfor_01.url                       =CoreServer_url+"/api/mcu/chatroom/get?"
CoreServer_GetChatroomInfor_01.chatroomInfo               =App_a["chatrooms"]
CoreServer_GetChatroomInfor_01.app_id                    =App_a["app_id"]
#expect
CoreServer_GetChatroomInfor_01.error_code                 =App_a["correct_err_code"]









