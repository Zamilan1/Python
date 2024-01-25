import math 
def main():
    a = float(input('enter the lenght of side a:'))
    b = float(input('enter the lenght of side b'))
    c =math.hypot(a,b)
    print("the lenght of the hypotenuse is",c)
main()