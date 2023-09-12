#Question 1: Write a function to print “hello_USERNAME!” USERNAME is the input of the function.
def hello_name(user_name):
    """Prints 'hello_USERNAME!'"""
    print("hello_" + user_name + "!")

#Question 2: Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    """Prints the odd numbers from 1-100"""
    print(list(range(1,100,2)))

#Question 3: Please write a Python function, max_num_in_list to return the max number of a given list.
def max_num_in_list(a_list):
    """Returns the max number of a given list"""
    maxnum = str(max(a_list))
    print(maxnum)
    return maxnum



#Question 4: Write a function to return if the given year is a leap year. A leap year is
#divisible by 4, but not divisible by 100, unless it is also divisible by 400.
#The return should be boolean Type (true/false)
def is_leap_year(a_year):
    """Returns if the given year is a leap year"""
    leap = False
    if a_year % 4 == 0:
        if a_year % 100 != 0:
            if a_year % 400 == 0:
                leap = True
                return leap
    print(leap)

#Question 5: Write a function to check to see if all numbers in list are consecutive numbers.
def is_consecutive(a_list):
    consecutive = False
    if a_list[0] == a_list[1] - 1:
            consecutive = True          
    if a_list[1] == a_list[2] - 1:
            consecutive = True
    if a_list[2] == a_list[3] - 1:
            consecutive = True
    if a_list[3] == a_list[4] - 1:
            consecutive = True
       
    print(consecutive)

    
  



hello_name(input("Enter your username: "))
first_odds()
a_list= [19, 20, 21, 22, 23]
max_num_in_list(a_list)
is_leap_year(1965)
is_consecutive(a_list)
