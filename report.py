import unittest
import time
from HTMLTestRunner import HTMLTestRunner

# 指定测试用户为当前文件夹下都interface目录
# test_dir = './report'
discover = unittest.defaultTestLoader.discover('.', pattern='*_test.py')
# discover = unittest.defaultTestLoader.discover(test_dir, pattern='add_guest_test.py')


if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = './report/' + now +'_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='JD Interface Test Report', description='Implementation Example with:')
    runner.run(discover)
    fp.close()
