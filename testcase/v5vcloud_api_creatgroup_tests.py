# -*- coding: utf-8 -*-
import unittest
import datetime
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import apiconfig.creatgroup.ProductionEnv_config as apimgr1
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


    def test0101_create_group_test(self):
        print "B-------------------------test0101_create_group_test缺少参数---------------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr1.CoreServer_CreatGroupTest1_02
        self.test.test_create_group_testQ(auth, session, info)
        print "E------------------------test0101_create_group_test缺少参数---------------------------E"

    def test0201_create_group_test(self):
        print "B------------------------test0201_create_group_test账户未登录---------------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr1.CoreServer_CreatGroupTest2_02
        self.test.test_create_group_test1(auth, session, info)
        print "E------------------------test0201_create_group_test账户未登录---------------------------E"

    def test0301_create_group_test(self):
        print "B------------------------test0301_create_group_test群成员超过限制---------------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr1.CoreServer_CreatGroupTest3_02
        self.test.test_create_group_test2(auth, session, info)
        print "E------------------------test0301_create_group_test群成员超过限制---------------------------E"