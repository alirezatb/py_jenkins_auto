from datetime import datetime
class multiply:
    def times(self, input_2):
        set_value_1 = datetime.now().day
        return str(input_2) + ' ' + str(set_value_1)

if __name__=='__main__':
    ml = multiply()
    ml.times(12)
