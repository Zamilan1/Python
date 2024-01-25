WEIGHT_OF_PACKAGES = 0.0
weight= 010

poundrate = 1.50
RATE_PER_ROUND = 0.0
weight = float(input('Enter the weight of package:'))
if weight > 10:
    RATE_PER_ROUND = 4.75
elif weight > 6:
    RATE_PER_ROUND = 4.00
elif weight > 2:
    RATE_PER_ROUND = 3.00
elif weight > 1:
    RATE_PER_ROUND = 1.50
else:
    RATE_PER_ROUND = 0
print('Rate_per_round:$',format(RATE_PER_ROUND,'.2f'))
print('weight:$',format(weight,'.2f'))
