# 파이썬에서 테스트를 위한 라이브러리
# 사용예) python -m unittest 테스트할 함수들이 담긴 py 파일
# 아래처럼 결과가 나온다. 이걸로 코드 테스트 가능 
'''
$python -m unittest tests.py
F
======================================================================
FAIL: test (tests.MyTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\dev\codeship-test\tests.py", line 8, in test
    self.assertEqual(fun(3),5)
AssertionError: 4 != 5

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)

뭐 이런식으로 메세지가 뜰 것이다.
'''
import unittest
import TestServer
 
def fun(x):
    return x+1

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3),4)

    def testPort(self):
        self.assertEqual(TestServer.PORT_NUMBER,9000) #port는 9000이어야 한다.
