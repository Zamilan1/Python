replacement = 0.8
def main():
    replace = 0.0
    mininsurance = 0.0
    replace = float(input('Enter the replacement cost:'))
    mininsurance = replace*replacement
    showinsurance(replace,mininsurance)
def showinsurance(replace,mininsur):
    print('The replacement cost is:',format(replace,'.2f'))
    print('The minimum insurance cost is:',format(mininsur,'.2f'))
main()