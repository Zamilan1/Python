import math
def main():
    number = float(input('Enter a number:'))
    square_root = math.sqrt(number)
    print('The square root of', number, 'is approximately', round(square_root, 2))
main()