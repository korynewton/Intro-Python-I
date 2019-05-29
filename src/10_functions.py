# Write a function is_even that will return true if the passed-in number is even.

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

def even_or_odd(number):
    result = is_even(number)
    if result:
        print('Even!')
    else:
        print('Odd!')
    
even_or_odd(num)