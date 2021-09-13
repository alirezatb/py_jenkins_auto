
class account:
    def check_password_length(self, password):
        if len(password) > 8:
            return True
        else:
            return False


    def calcuate_numbers(self, first, second):
        return str(first + second)

if __name__ == '__main__':
    accVerify = account()
    print('The password length is ' + str(accVerify.check_password_length('offtoschool')))
    print("calculate_number_output" + accVerify.calcuate_numbers(1, 3))