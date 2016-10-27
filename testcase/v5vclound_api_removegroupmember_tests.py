# -*- coding: utf-8 -*-
import unittest
import datetime
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import apiconfig.removegroupmember.production_env_config as apimgr1
import lib.modules as modules
import apiconfig.mainprocess.ProductionEnv_config as apimgr
class core_server_tests(unittest.TestCase):
    test = modules.test_core_server()
    def setUp(self):
        currentTime = str(datetime.datetime.now())[0:19]
        print "@@@@@@@@@@-- RUN TESTCASE --%s@@@@@@@@@@" % currentTime
        pass

    def tearDown(self):
        pass

    def test0000_create_group_test(self):
        print "B----------------------------------test0000_create_group_test---------------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr.CoreServer_CreatGroupTest_02
        res = self.test.test_create_group_test(auth, session, info)
        ############## 反向赋值给group_id ##############
        # print "@@@@@@@@@@",res["id"]
        info.groupInfo["group_id"] = res["id"]

        print "E----------------------------------test0000_create_group_test---------------------------E"

    ####群组中踢人--------群组不存在#####
    def test0101_remove_group_member_test(self):
        print "B----------------------------------test0101_remove_group_member_test-----------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr1.CoreServer_RemoveGroupMemberTest_01
        self.test.test_remove_group_member_test(auth, session, info)
        print "E----------------------------------test0101_remove_group_member_test------------------------E"
    ####群组中踢人--------缺少参数#####
    def test0201_remove_group_member_test(self):
        print "B----------------------------------test0201_remove_group_member_test-----------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr1.CoreServer_RemoveGroupMemberTest_02
        self.test.test_remove_group_member_testC(auth, session, info)
        print "E----------------------------------test0201_remove_group_member_test------------------------E"
    #####群组中踢人--------未登录######
    def test0301_remove_group_member_test(self):
        print "B----------------------------------test0301_remove_group_member_test-----------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr1.CoreServer_RemoveGroupMemberTest_03
        self.test.test_remove_group_member_testB(auth, session, info)
        print "E----------------------------------test0301_remove_group_member_test------------------------E"