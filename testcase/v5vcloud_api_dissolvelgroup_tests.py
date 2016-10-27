# -*- coding: utf-8 -*-
import unittest
import datetime
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import apiconfig.dissolvegroup.ProductionEnv_config as apimgr1
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

    def test0001_dissolve_group_test(self):
        print "B----------------------------------test0001_dissolve_group_test账号未登录---------------------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr1.CoreServer_DissolveGroupTest_01
        self.test.test_dissolve_group_test1(auth, session, info)
        print "E----------------------------------test0001_dissolve_group_test账号未登录-----------------------------------E"

    def test0002_dissolve_group_test(self):
        print "B----------------------------------test0002_dissolve_group_test群组不存在---------------------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr1.CoreServer_DissolveGroupTest_02
        self.test.test_dissolve_group_test(auth, session, info)
        print "E----------------------------------test0002_dissolve_group_test群组不存在-----------------------------------E"

    def test0003_dissolve_group_test(self):
        print "B----------------------------------test0003_dissolve_group_test缺少参数---------------------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr1.CoreServer_DissolveGroupTest_03
        self.test.test_dissolve_group_test2(auth, session, info)
        print "E----------------------------------test0003_dissolve_group_test缺少参数-----------------------------------E"
