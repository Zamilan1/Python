def main ():
    value = 99
    print('The value is',value)
    change_me(value)
    print('Back in the main value',value)
def change_me(arg):
    print('Im changing the value')
    arg = 0
    print('NOw the the value is',arg)
main()