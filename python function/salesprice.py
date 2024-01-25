discount_percent = .20
def main():
    reg_price = get_regular_price()
    sales_price = reg_price-discount_percent(reg_price)
    print("The regular price of the item is: $",reg_price)
def get_regular_price():
    price = float(input('Enter the items regular price'))
    return price
def discount_percent(price):
    return price*discount_percent
main()