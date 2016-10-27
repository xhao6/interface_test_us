
# -*- coding: utf-8 -*-
import unittest
import datetime
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import apiconfig.getgroupinfor.production_env_config as apimgr1
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
    ####获取群组信息------缺少参数#####
    def test0101_get_group_infor_test(self):
        print "B----------------------------------test0101_test_get_group_infor_test-----------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr1.CoreServer_GetGroupInforTest_01
        self.test.test_get_group_infor_test(auth, session, info)
        print "E----------------------------------test0101test_get_group_infor_test------------------------E"

    ####获取群组信息------账户未登录#####
    def test0201_get_group_infor_test(self):
        print "B----------------------------------test0201_test_get_group_infor_test-----------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr1.CoreServer_GetGroupInforTest_01
        self.test.test_get_group_infor_testB(auth, session, info)
        print "E----------------------------------test0201test_get_group_infor_test------------------------E"

    ####获取群组信息------群组不存在#####
    def test0301_get_group_infor_test(self):
        print "B----------------------------------test0201_test_get_group_infor_test-----------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr1.CoreServer_GetGroupInforTest_03
        self.test.test_get_group_infor_test(auth, session, info)
        print "E----------------------------------test0201test_get_group_infor_test------------------------E"