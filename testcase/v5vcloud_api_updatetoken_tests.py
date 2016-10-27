# -*- coding: utf-8 -*-
import unittest
import datetime
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import apiconfig.updatetoken.ProductionEnv_config as apimgr1
import lib.modules as modules
import apiconfig.mainprocess.ProductionEnv_config as apimgr

#from apiconfig.mainprocess.ApiClass import getToken
#from apiconfig.mainprocess.ApiClass import getUserIdSessionId


class core_server_tests(unittest.TestCase):
    test = modules.test_core_server()
    def setUp(self):
        currentTime = str(datetime.datetime.now())[0:19]
        print "@@@@@@@@@@-- RUN TESTCASE --%s@@@@@@@@@@" % currentTime
        pass

    def tearDown(self):
        pass


    def test0001_update_token__test(self):
        print "B----------------------------------test0001_update_token__test账号未登录---------------------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr1.CoreServer_UpdateTokenTest_01
        self.test.test_update_token_test1(auth, session, info)
        print "E----------------------------------test0001_update_token__test账号未登录-----------------------------------E"

    def test0002_update_token__test(self):
        print "B----------------------------------test0001_update_token__test缺少参数---------------------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr1.CoreServer_UpdateTokenTest_02
        self.test.test_update_token_test(auth, session, info)
        print "E----------------------------------test0001_update_token__test缺少参数-----------------------------------E"

