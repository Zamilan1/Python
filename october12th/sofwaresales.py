retail_price = 99
quantity = 0
full_price = 0.0
discountrate = 0.0
discountamount = 0.0
totalamount = 0.0
quantity = int(input("Enter the NUmber of packages purchased:"))
if quantity >99:
    discountrate = .40
elif quantity > 49:
    discountrate = .30
elif quantity >19:
    discountrate = .20
elif quantity > 9:
    discountrate = .10
else:
    discountrate = 0
    full_price = quantity*retail_price
    discountamount = full_price*discountrate
    totalamount = full_price-discountamount
    print('Discount amount:$',format(discountamount,'.2f'))
    print('Total amount : $', format(totalamount,'.2f'))