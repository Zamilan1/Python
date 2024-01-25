test1mark=int(input('Enter mark out of 25 for the test1:'))
test2mark=int(input('Enter mark out of 25 for the test3:'))
examMark=int(input('Enter mark out of 50 for the exam :'))
if (test1mark < 0 or test1mark > 25) or \
   (test2mark < 0 or test2mark > 25) or \
   (examMark < 0 or examMark > 50):
print('Error': Invalid mark entered)
else:
totalmark = test1mark+test2mark+examMark
print('Total mark:',totalmark)
if totalmark < 50 or examMark < 25:
    print('Fail')
elif totalmark >= 50 and totalmark <= 59:
    print('Pass')
elif totalmark >= 60 and totalmark <= 79:
    print('Credit')
elif totalmark >=80 and totalmark <= 100:
    print('Distinction')