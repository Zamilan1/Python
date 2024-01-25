cal_from_fat = 9
cal_from_carbs = 4
def main():
    gramsfat = 0.0
    gramscarbs = 0.0
    calfat = 0.0
    calcarbs = 0.0
    gramsfat = float(input('Enter the fat gram'))
    gramscarbs = float(input('Enter the carbs gram'))
    calfat = gramsfat * cal_from_carbs
    calcarbs = gramscarbs * cal_from_fat
    print('The calories from fat are', calfat)
    print('The calories from carbs are', calcarbs)
main()