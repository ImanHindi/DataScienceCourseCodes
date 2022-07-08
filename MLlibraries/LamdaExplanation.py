#references:
#https://stackabuse.com/lambda-functions-in-python/
#In Python, a lambda function is a single-line function declared with no name,
#  which can have any number of arguments, but it can only have one expression. 
# Such a function is capable of behaving similarly to a regular function declared using the Python's def keyword. 
# Often times a lambda function is passed as an argument to another function.

#Example 1:
def remainder(num):
    return num % 2
#same as :
lambda num: num % 2


#Example 2:
#Lambda functions are used when you need a function for a short period of time. 
# This is commonly used when you want to pass a function as an argument to higher-order functions, that is,
#  functions that take other functions as their arguments.
def testfunc(num):
    return lambda x : x * num
#we have a function that takes one argument, 
# and the argument is to be multiplied with a number that is unknown.
result1 = testfunc(10)
print(type(result1))
print(result1(9))

#It is possible for us to use the testfunc() 
# function to define the above two lambda functions within a single program:
def testfunc(num):
    return lambda x : x * num

result1 = testfunc(10)
result2 = testfunc(1000)

print(result1(9))
print(result2(9))




#Example3

#The filter() Function
#The Python's filter() function takes 
#a lambda function together with a list as the arguments. 
#It has the following syntax:

numbers_list = [2, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]
filtered_list = list(filter(lambda num: (num > 7), numbers_list))
print(filtered_list)
#A lambda function, along with the list to be evaluated, is passed to the filter() function.
#  The filter() function returns a list of those elements that return True when evaluated by the lambda funtion.
#  Consider the example given below:


#Example 4:

#The map() Function:

numbers_list = [2, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]

mapped_list = list(map(lambda num: num % 2, numbers_list))

print(mapped_list)

#In the script above, we have a list numbers_list, 
# which consists of random numbers. We then call the map() function and pass it a lambda function as the argument.
#  The lambda function calculates the remainder after dividing each number by 2. 
# The result of the mapping is stored in a list named mapped_list. 
# Finally, we print out the contents of the list.