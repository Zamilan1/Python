import circle
import rectangle
area_circile_choice =1
circumference_choice =2
area_rectangle_choice =3
perimeter_rectangle_choice=4
quit_choice =5
def main():
    while choice != quit_choice:
    display_menu()
    choice =int(input('Enter your choice'))
    if choice == area_circile_choice:
    radius = float(input('Enter the circle radius'))
    choice = int(input('Enter the circle radius'))
    print('The area of circle is:',circle.area(radius))
    print('The area of circle is:',circle.area(radius))
elif choice == circumference_choice:
    radius =float(input('Enter the radius'))
    print('The circumference of circle is:',circle.get_circumference())
elif choice == area_rectangle_choice
    width = float(input('Enter the rectangle width'))
    lenght = float(input('Enter the rectange lenght'))
    print('The area of rectangle is:',rectangle.get_area())
elif choice == quit_choice:
    print('Exit')
else:
    print('Error invalid section')
def display_menu():
     print('    Menu')
     print('1-Area of Circle')
     print('2-Circumference of Circle')
     print('3-Area of Rectangle')
     print('4-Perimeter of Rectangle')
     print('5-Quit')
     main()