import circle
import rectangle
area_circile_choice =1
circumference_choice =2
area_rectangle_choice =3
perimeter_rectangle_choice=4
quit_choice =5
def main():
while choice != quit_choice
display_menu()
    print("""
1. Calculate the area of a circle using radius and pi as inputs.
          2. Calculate the circumference of a circle using radius and pi as inputs.
          3. Calculate the area of a rectangle using length, width and height as inputs.
          4. Calculate the perimeter of a rectangle using length, width and height as inputs.
          5. Exit Program.""")
    choice = int(input("Enter your choice : "))
    if (choice == 1):
        r = float(input("Enter the value for radius in cm :"))
        result = circle.calculate_circle_area(r)
        print("The area of the circle is ",result,"cm^2.")
        elif (choice == 2):
r = float(input("Enter the value for radius in cm :"))
result = circle.calculate_circle_circumference(r)
print("The circumference of the circle is ",result,"cm.")
elif (choice == 3):
l = float(input("Enter the value for length in cm :"))
w = float(input("Enter the value for width in cm :"))
h = float(input("Enter the value for height in cm :"))
result = rectangle.calculate_rectangle_area(l, w, h)
print("The area of the rectangle is ",result,"cm^2.")
elif (choice == 4):
l = float(input("Enter the value for length in cm :"))
w = float(input("Enter the value for width in cm :"))
h = float(input("Enter the value for height in cm :"))
result = rectangle.calculate_rectangle_perimeter(l, w, h)
print("The perimeter of the rectangle is ",result,"cm.")
elif (choice == 5):
break
else:
print ("Invalid Choice! Please enter again.")
