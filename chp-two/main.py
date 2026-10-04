def double(x):
    return x * 2

print(double(7))

#example of using the first-class fucntions in python
def apply_to_one(f):
    return f(1)

my_double = double
x = apply_to_one(my_double)

print(x)

#lambda functions

y = apply_to_one(lambda x: x+4)

#functions with defined behavior

def name(first="What's his name", last="Something"):
    return first + " " + last

print(name("Pedro", "Oliveira"))
print(name("Pedro"))
print(name(last="Oliveira"))

#string manipulation
#ways of uniting strings in python:
first_name = "Pedro"
surname = "Oliveira"

full_name1 = first_name + " " + surname
full_name2 = "{0} {1}".format(first_name, surname)
full_name3 = f"{first_name} {surname}" ##will be used throughout the book

print(full_name1)
print(full_name2)
print(full_name3)

#exceptions

try:
    print(0/0)
except ZeroDivisionError:
    print("cannot divide by zero")

#lists

integer_list = [1, 2, 3]
list_with_different_types = ["test", 1, 0.87]
list_of_lists = [integer_list, list_with_different_types, []]

print(sum(integer_list))
print(len(list_of_lists))

##slicing and strigding lists
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[0:3]) #prints first 3 elements
print(numbers[-1]) #prints last number
print(numbers[-1:0:-1]) #prints the list in reverse
print(numbers[::3]) #prints the list 3 by 3

##adding elements to my list

ten_to_fifteen = [10, 11, 12, 13, 14, 15]
numbers.extend(ten_to_fifteen)
numbers.append(16) 
print(numbers)

#tuples

my_list = [1, 2]
my_tuple = (1, 2)
my_other_tuple = 3, 4

try:
    my_tuple[0] = 3
except TypeError:
    print("cannot modify tuples")

#using tuples to receive output

def add_and_mult(x, y):
    return (x + y), (x * y)

sp = add_and_mult(5, 5)
s, p = add_and_mult(6, 6)

print(sp)
print(s)
print(p)
