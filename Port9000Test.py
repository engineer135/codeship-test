import unittest
import TestServer

class MyTest(unittest.TestCase):
    def testPort(self):
        self.assertEqual(TestServer.PORT_NUMBER,9000) #port는 9000이어야 한다.
