from datetime import datetime
class multiply:
    def times(self, input_1):
        get_value = datetime.now().day
        return str(input_1) + ' ' + str(get_value)

if __name__=='__main__':
    ml = multiply()
    ml.times(12)
