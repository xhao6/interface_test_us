# -*- coding: utf-8 -*-
import unittest
import datetime
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import apiconfig.setdisturb.ProductionEnv_config as apimgr1
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

    def test0101_set_disturb_test(self):
        print "B----------------------test0101_set_disturb_test账户未登录---------------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr1.CoreServer_SetDisturbTest_01
        self.test.test_set_disturb_test1(auth, session, info)
        print "E----------------------test0101_set_disturb_test账户未登录---------------------------E"

    def test0201_set_disturb_test(self):
        print "B----------------------test0201_set_disturb_test账户未登录---------------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr1.CoreServer_SetDisturbTest_02
        self.test.test_set_disturb_test1(auth, session, info)
        print "E-----------------------test0201_set_disturb_test账户未登录---------------------------E"