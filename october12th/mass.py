mass = float(input("Enter the mass of object in kilogram"))
weight = mass*9.8
if weight > 500:
    print("The object is too heavy:")
elif weight < 100:
    print("The object is too light:")
else:
    print("The object weight",weight,'newtons')
