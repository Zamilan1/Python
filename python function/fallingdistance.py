#distance = (9.8*t*t)/2
def main():
    distance = 0.0
    print('Time\tfalling distance')
    print('----------------------')
    for time in range(1,11):
        distance = falling_distance(time)
        print(time, '\t', format(distance,'.2f'))
def falling_distance(time):
    distance = (9.8*time*time)/2
    return distance
main()