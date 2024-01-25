# Coffee Record Manager

This Python script allows you to search for a coffee description in a coffee record file and update its quality. Here's a step-by-step explanation of the code:

## Step 1: Import the necessary module

```python
import os
```

This line imports the `os` module, which provides functions for interacting with the operating system.

## Step 2: Define the `main()` function

```python
def main():
```

This line defines the `main()` function, which is the entry point of the script.

## Step 3: Prompt the user for input

```python
    found = True
    search = input('Enter description to search for')
    new_qty = input('Enter the new quality')
```

These lines prompt the user to enter the description of the coffee they want to search for and the new quality they want to assign to it. The `input()` function is used to read user input from the console.

## Step 4: Open the coffee record file

```python
    coffee_file=open(r"C:\Users\me\Desktop\coffee_record\showcoffeeRecord.py",'r')
```

This line opens the coffee record file in read mode. The `open()` function takes two arguments: the path to the file and the mode in which the file should be opened. In this case, the file is opened in read mode, which is indicated by the 'r' mode.

## Step 5: Open a temporary file

```python
    tempt_file =open(r"C:\Users\me\Desktop\coffee_record\coffee.py",'w')
```

This line opens a temporary file in write mode. The `open()` function takes two arguments: the path to the file and the mode in which the file should be opened. In this case, the file is opened in write mode, which is indicated by the 'w' mode.

## Step 6: Read the coffee record file line by line

```python
    descr = coffee_file.readline()
    while descr !='':
```

These lines read the coffee record file line by line. The `readline()` method of the file object is used to read each line of the file. The loop continues until the end of the file is reached, which is indicated by an empty string ('') being returned by the `readline()` method.
