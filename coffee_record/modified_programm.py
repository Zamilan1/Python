import os


def main():
    found = True
    search = input('Enter description to search for')
    new_qty = input('Enter the new quality')
    coffee_file=open(r"C:\Users\me\Desktop\coffee_record\showcoffeeRecord.py",'r')
    tempt_file =open(r"C:\Users\me\Desktop\coffee_record\coffee.py",'w')    
    descr = coffee_file.readline()
    while descr !='':
        qty = float(coffee_file.readline())
        descr = descr.rstrip('\n')
        if descr == search:
            tempt_file.write(descr+'\n')
            tempt_file.write(str(new_qty)+'\n')
            found  = True
        else :
            tempt_file.write(descr+'\n')
            tempt_file.write(str(qty)+'\n')
        descr = coffee_file.readline()
    coffee_file.close()
    tempt_file.close()
    if not found:
        print("Not Found")
        else:
os.remove("coffee.py")
os.rename("tempt.py","coffee.py")
    if found:
    print('The file was UPDATED')
        else:
        print('That item was not found in the file')
main()