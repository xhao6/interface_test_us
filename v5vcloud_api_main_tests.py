# -*- coding: utf-8 -*-
import unittest

from lib import modules
#import apiconfig.TestEnv_config as apimgr
import apiconfig.mainprocess.ProductionEnv_config as apimgr
import datetime

class core_server_tests(unittest.TestCase):
    test = modules.test_core_server()
    def setUp(self):
        currentTime = str(datetime.datetime.now())[0:19]
        print "@@@@@@@@@@-- RUN TESTCASE --%s@@@@@@@@@@" % currentTime
        pass

    def tearDown(self):
        pass

    def test0001_get_token_test(self):
        print "B----------------------------------test0001_get_token----------------------------------B"
        auth = apimgr.CoreServer_getToken_01
        self.test.test_get_token_test(auth)
        print "E----------------------------------test0001_get_token----------------------------------E"

    def test0101_get_userId_sessionId_test(self):
        print "B----------------------------------test0101_get_userId_sessionId-----------------------B"
        auth = apimgr.CoreServer_getToken_01
        info = apimgr.CoreServer_getUserIdSessionId_01
        self.test.test_get_userId_sessionId_test(auth, info)
        print "E----------------------------------test0101_get_userId_sessionId------------------------E"

    def test0201_get_sessionID_test(self):
        print "B----------------------------------test0201_get_sessionID-------------------------------B"
        auth = apimgr.CoreServer_getToken_01
        info = apimgr.CoreServer_getSessionID_01
        self.test.test_get_sessionID_test(auth, info)
        print "E----------------------------------test0201_get_sessionID-------------------------------E"

    def test0002_get_sessionID_test(self):
        print "B----------------------------------test002_get_sessionID-------------------------------B"
        auth = apimgr.CoreServer_getToken_01
        info = apimgr.CoreServer_getSessionID_03
        self.test.test_get_sessionID_test(auth, info)
        print "E----------------------------------test0002_get_sessionID-------------------------------E"

    def test0301_get_server_test(self):
        print "B----------------------------------test0301_get_server_test-----------------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr.CoreServer_GetServerTest_01
        self.test.test_get_server_test(auth, session, info)
        print "E----------------------------------test0301_get_server_test-----------------------------E"

    def test0401_update_token_test(self):
        print "B----------------------------------test0401_update_token_test---------------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr.CoreServer_UpdateTokenTest_01
        self.test.test_update_token_test(auth, session, info)
        print "E----------------------------------test0401_update_token_test---------------------------E"

    def test0501_get_location_test(self):
        print "B----------------------------------test0501_get_location_test---------------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr.CoreServer_GetLocationTest_01
        self.test.test_get_location_test(auth, session, info)
        print "E----------------------------------test0501_get_location_test---------------------------E"

    #########更新用户昵称##########
    def test0601_update_nickname_test(self):
        print "B----------------------------------test0601_update_nickname-----------------------------B"
        auth    = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info    = apimgr.CoreServer_UpdateNicknameTest_01
        self.test.test_update_nickname_test(auth, session, info)
        print "E----------------------------------test0601_update_nickname-----------------------------E"

    def test0701_create_group_test(self):
        print "B----------------------------------test0701_create_group_test---------------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr.CoreServer_CreatGroupTest_02
        res = self.test.test_create_group_test(auth, session, info)
        ############## 反向赋值给group_id ##############
        # print "@@@@@@@@@@",res["id"]
        info.groupInfo["group_id"] = res["id"]

        print "E----------------------------------test0701_create_group_test---------------------------E"

    def test0801_join_group_test(self):
        print "B----------------------------------test0801_join_group_test-----------------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr.CoreServer_JoinGroupTest_01
        self.test.test_join_group_test(auth, session, info)
        print "E----------------------------------test0801_join_group_test-----------------------------E"

    def test0901_update_group_test(self):
        print "B----------------------------------test0901_update_group--------------------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr.CoreServer_UpdateGroupTest_01
        self.test.test_update_group_test(auth, session, info)
        print "E----------------------------------test0901_update_group--------------------------------E"

    def test1001_get_group_infor_test(self):
        print "B----------------------------------test1001_get_group_infor-----------------------------B"
        auth    = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr.CoreServer_GetGroupInforTest_01
        self.test.test_get_group_infor_test(auth, session, info)
        print "E----------------------------------test1001_get_group_infor-----------------------------E"

    def test1101_get_offline_messages_test(self):
        print "B----------------------------------test1101_get_offline_messages_test-------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr.CoreServer_GetOfflineMessagesTest_01
        self.test.test_get_offline_messages_test(auth, session, info)
        print "E----------------------------------test1101_get_offline_messages_test-------------------E"

    def test1201_upload_unread_mes_test(self):
        print "B----------------------------------test1201_upload_unread_mes_test----------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr.CoreServer_UploadUnreadMesTest_01
        self.test.test_upload_unread_mes_test(auth, session, info)
        print "E----------------------------------test1201_upload_unread_mes_test---------------------E"
    ##########判断文件是否上传#######
    def test1301_is_file_exist_test(self):
        print "B----------------------------------test1301_is_file_exist_test----------------------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr.CoreServer_IsFileExistTest_01
        self.test.test_is_file_exist(auth, session, info)
        print "E----------------------------------test1301_is_file_exist_test----------------------------------E"
    ##########上传文件##############
    def test1401_upload_file_test(self):
        print "B----------------------------------test1401_upload_file_test---------------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr.CoreServer_UploadFileTest_01
        self.test.test_upload_file_test(auth, session, info)
        print "E----------------------------------test1401_upload_file_test---------------------------E"

    def test1501_set_close_disturb_test(self):
        print "B----------------------------------test1501_set_disturb_test---------------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr.CoreServer_SetDisturbTest_01
        self.test.test_set_disturb_test(auth, session, info)
        print "E----------------------------------test1501_set_disturb_test---------------------------E"

    def test1601_set_open_disturb_test(self):
        print "B----------------------------------test1601_set_disturb_test---------------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr.CoreServer_SetDisturbTest_02
        self.test.test_set_disturb_test(auth, session, info)
        print "E----------------------------------test1601_set_disturb_test---------------------------E"
    ########群组中踢人########
    def test1701_remove_group_member_test(self):
        print "B----------------------------------test1701_remove_group_member------------------------B"
        session    = apimgr.CoreServer_getSessionID_01
        token      = apimgr.CoreServer_getToken_01
        Info       = apimgr.CoreServer_removeGroupMemberTest_01
        self.test.test_remove_group_member_test(token,session,Info)
        print "E----------------------------------test1701_remove_group_member------------------------E"
    ###########退出群组#######
    def test1801_exit_group_test(self):
        print "B----------------------------------test1801_exit_group_test------------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_03
        info = apimgr.CoreServer_ExitGroupTest_01
        self.test.test_exit_group(auth, session, info)

        print "E----------------------------------test1801_exit_group_test------------------------E"
    ###########解散群组#######
    def test1901_dissolve_group_test(self):
        print "B----------------------------------test1901_dissolve_group_test------------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01

        info = apimgr.CoreServer_DissolveGroupTest_01
        self.test.test_dissolve_group_test(auth, session, info)
        print "E----------------------------------test1901_dissolve_group_test------------------------E"

    def test2001_creat_chatroom_test(self):
        print "B----------------------------------test2001_creat_chatroom_test------------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr.CoreServer_CreatChatroomTest_01
        res=self.test.test_creat_chatroom_test(auth, session, info)
        info.chatroomInfo["id"] = res["id"]
        print "E----------------------------------test2001_creat_chatroom_test------------------------E"


    def test2101_get_chatroom_list_test(self):
       print "B----------------------------------test2101_creat_chatroom_list_test------------------------B"
       auth = apimgr.CoreServer_getToken_01
       session = apimgr.CoreServer_getSessionID_01
       info = apimgr.CoreServer_GetChatroomList_01
       self.test.test_get_chatroom_list_test(auth, session, info)
       print "E----------------------------------test2101_creat_chatroom_list_test------------------------E"


    def test2201_get_chatroom_infor_test(self):
        print "B----------------------------------test2201_creat_chatroom_infor_test------------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr.CoreServer_GetChatroomInfor_01
        self.test.test_get_chatroom_infor_test(auth, session, info)
        print "E----------------------------------test2201_creat_chatroom_infor_test------------------------E"



