keep_going = 'y'
while keep_going == 'y':
    sales = float(input('Enter the amount of sales:'))
    comm_rate = float(input('Enter the commission rate:'))
    commission = sales*comm_rate
    print('commission is $',format(commission,'.2f'),sep='')
    keep_going = input('Do you want to Calculate anothoer commission (y for n):')