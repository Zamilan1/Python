tax_factor = 0.0065
print('Enter the property lot number')
print('or Enter 0 to End:')
lot = int(input('Enter lot Number'))
while lot != 0:
    value = float(input('Enter the property value'))
    tax = value*tax_factor
    print('Property tax:$',format(tax,'.2f'),sep='')
    print('Enter the next lot number or')
    print('Enter 0 to end')
    lot = int(input('Lot number:'))