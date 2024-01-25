time = int(input('Enter the number of hours traveled: '))
speed = float(input('Enter the speed of the vehicle in MPH: '))

print('Hour\tDistance Traveled')
print('------------------------')

distance_data = {hour: hour * speed for hour in range(1, time + 1)}

for hour, distance_traveled in distance_data.items():
    print(f'{hour}\t{distance_traveled}')
