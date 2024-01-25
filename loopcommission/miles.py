print('Miles\tkilometers')
print('---------------')

for miles in range(10, 81, 10):
    kilometers = round(miles * 1.60934, 2)
    print(miles, '\t', kilometers)
