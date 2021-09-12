import unittest
import python_pass_check as AccountClass


class Test(unittest.TestCase):
    accInfo = AccountClass.account()

    def test_check_password_length(self):
        print("Checking possible passwords\n")
        passwordList = [ 'abeautifulday', 'astrictboss', 'alovelyhouse' ]

        for passwd in passwordList:
            print("Checking password " + passwd + "\n")
            passInfo = self.accInfo.check_password_length(passwd)
            self.assertTrue(passInfo)

    def test_calculate_numbers(self):
        first_number = 2
        second_number = 3
        out = self.accInfo.calcuate_numbers(first=first_number, second=second_number)
        self.assertEqual(out, "5")

if __name__ == '__main__':
    unittest.main()