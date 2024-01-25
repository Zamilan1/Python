class Square:
    def __init__(self, side):
        """ creates a square having the given side
        """
        self.side = side
 
    def area(self):
        """ returns area of the square
        """
        return self.side**2
 
    def perimeter(self):
        """ returns perimeter of the square
        """
        return 4 * self.side
 
    def __repr__(self):
        """ declares how a Square object should be printed
        """
        s = 'Square with side = ' + str(self.side) + '\n' + \
        'Area = ' + str(self.area()) + '\n' + \
        'Perimeter = ' + str(self.perimeter())
        return s
 
 
if __name__ == '__main__':
    # read input from the user
    side = int(input('enter the side length to create a Square: '))
     
    # create a square with the provided side
    square = Square(side)
 
    # print the created square
    print(square)
Note: For more information about the function __repr__(), refer this article. Now that we have our software ready, let’s have a look at the directory structure of our project folder and after that, we’ll start testing our software.

---Software_Testing
   |--- __init__.py (to initialize the directory as python package)
   |--- app.py (our software)
   |--- tests (folder to keep all test files)
           |--- __init__.py