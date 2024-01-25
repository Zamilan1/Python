def main():
    found =False
    search = input('Enter description saerch for ')
    coffee_file = open()
    descr=coffee_file.readline()
    while descr !="":
        qty=float(coffee_file.readline())
        descr=descr.rstrip('\n')
        if descr == search:
            print("Description:",descr)
            print("Quantity: ",qty,)
            found =True
        descr = coffee_file.readline()
    coffee_file.readline()
    if not found:
        print('That item was not found in the file')
main()
