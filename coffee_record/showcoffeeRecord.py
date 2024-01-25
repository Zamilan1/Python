def main():
    coffee_file = open()
    descr = coffee_file.readline()
    while discr !="":
        qty = float(coffee_file.readline())
        descr = descr.rstrip('\n')
        print('Description:',descr)
        print('Quantity:',qty, )
        descr=coffee_file.readline()
    coffee_file.close()
    print('Data Read')
main()