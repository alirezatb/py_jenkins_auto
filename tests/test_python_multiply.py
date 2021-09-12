import unittest
from python_multiply import multiply


class Test2(unittest.TestCase):
    ainfo = multiply()

    def test_times(self):
        out = self.ainfo.times(12)
        self.assertEqual(out, '12 12')
if __name__ == '__main__':
    t =Test2()
    t.test_times()