expenses_list = {
    "Loan Payment": 0,
    "Insurance": 0,
    "Gas": 0,
    "Oil": 0,
    "Tires": 0,
    "Maintenance": 0,
}


for expense in expenses_list:
    expenses_list[expense] = float(input(f"Enter monthly cost for {expense}: "))


total_monthly_cost = sum(expenses_list.values())
total_annual_cost = total_monthly_cost * 12


print(f"\nTotal Cost Monthly Expenses: ${total_monthly_cost:.2f}")
print(f"Total Annual Cost: ${total_annual_cost:.2f}")