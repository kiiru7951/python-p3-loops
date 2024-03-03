#!/usr/bin/env python3

def happy_new_year():
    count = 10
    print(count)
    while count > 0:
        count -= 1
        print(count)
        if count == 0:
            print ("Happy New Year!")
    return count

def square_integers(int_list):
    int_list = [integer * integer for integer in int_list]
    return int_list
    

def fizzbuzz():
    for number in range(1,101):
        if (number % 3 == 0 and number % 5 == 0):
            print ("FizzBuzz")
        elif (number % 3 == 0):
            print ("Fizz")
        elif (number % 5 == 0):
            print ("Buzz")
        else:
            print (number)
    return number