# -*- coding: utf-8 -*- 
import unittest
import TestServer

class MyTest(unittest.TestCase):
    def testPort(self):
        self.assertEqual(TestServer.PORT_NUMBER,8000) #port는 8000이어야 한다.
