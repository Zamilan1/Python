total = 0
bugs = 0
for day in range(5): # 0,1,2,3,4
   bugs =int(input('Enter the number of bugs collects on day'))
   total = total+bugs 
print('The total bugs collected:',total)