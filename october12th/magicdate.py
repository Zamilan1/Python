def check_special_date():
    month = int(input("Enter the month (1-12): "))
    day = int(input("Enter the day (1-31): "))
    year = int(input("Enter the two-digit year (00-99): "))

    if month * day == year:
        print("The date is special!")
    else:
        print("The date is not special.")

check_special_date()