body_mass_multipler = 703
weight = 0.0
height = 0.0
BMI = 0.0 
weight= float(input("Enter the weight in pounds "))
height= float(input("Enter the height in inches "))
BMI= weight * 703 / height*height
print("The person's BMi:",format(BMI,'.2f'))
BMI = 18.5
BMI = 25 
if BMI < 18.5:
    print('Person is underweight')
elif BMI > 25:
    print('Person is overweight')
else:
    print('You are optimal weight')
    
