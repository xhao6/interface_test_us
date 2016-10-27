# -*- coding: utf-8 -*-
import unittest
import datetime
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import apiconfig.joingroup.ProductionEnv_config as apimgr1
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

    def test0001_join_group_test(self):
        print "B----------------------------------test0001_join_group_test账号未登录---------------------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr1.CoreServer_JoinGroupTest_01
        self.test.test_join_group_test1(auth, session, info)
        print "E----------------------------------test0001_join_group_test账号未登录-----------------------------------E"

    def test0002_join_group_test(self):
        print "B----------------------------------test0002_join_group_test群组不存在---------------------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr1.CoreServer_JoinGroupTest_02
        self.test.test_join_group_test(auth, session, info)
        print "E----------------------------------test0002_join_group_test群组不存在-----------------------------------E"

    def test0003_join_group_test(self):
        print "B----------------------------------test0003_join_group_test非法参数---------------------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr1.CoreServer_JoinGroupTest_03
        self.test.test_join_group_test(auth, session, info)
        print "E----------------------------------test0003_join_group_test非法参数-----------------------------------E"

    def test0004_join_group_test(self):
        print "B----------------------------------test0004_join_group_test群组人数超限---------------------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr1.CoreServer_JoinGroupTest_04
        self.test.test_join_group_test2(auth, session, info)
        print "E----------------------------------test0004_join_group_test群组人数超限-----------------------------------E"
