def double(x):
    return x * 2

print("--- Testing functions")
print(double(7))

#example of using the first-class fucntions in python
def apply_to_one(f):
    return f(1)

my_double = double
x = apply_to_one(my_double)

print("\n--- Testing first-class functions")
print(x)

#lambda functions

y = apply_to_one(lambda x: x+4)

#functions with defined behavior

def name(first="What's his name", last="Something"):
    return first + " " + last

print("\n--- Testing functions with defined behavior")
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

print("\n--- Testing string manipulation")
print(full_name1)
print(full_name2)
print(full_name3)

#exceptions

print("\n--- Testing exceptions")
try:
    print(0/0)
except ZeroDivisionError:
    print("cannot divide by zero")

#lists

integer_list = [1, 2, 3]
list_with_different_types = ["test", 1, 0.87]
list_of_lists = [integer_list, list_with_different_types, []]

print("\n--- Testing lists")
print(sum(integer_list))
print(len(list_of_lists))

##slicing and strigding lists
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("\n--- Testing slicing and strides in lists")
print(numbers[0:3]) #prints first 3 elements
print(numbers[-1]) #prints last number
print(numbers[-1:0:-1]) #prints the list in reverse
print(numbers[::3]) #prints the list 3 by 3

##adding elements to my list

ten_to_fifteen = [10, 11, 12, 13, 14, 15]
numbers.extend(ten_to_fifteen)
numbers.append(16) 
print("\n--- Testing element addition to lists")
print(numbers)

#tuples

my_list = [1, 2]
my_tuple = (1, 2)
my_other_tuple = 3, 4
 
print("\n--- Testing tuples")
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

#how to declare dicts

empty_dict = {}
empty_dict2 = dict()
grades = {"Joel":80, "Tim":95}

joel_grades = grades["Joel"]

print(joel_grades)

try:
    kate_grades = grades["Kate"]
except KeyError:
    print("no grade for Kate")

grades["Kate"] = 100

print(len(grades))
print(grades)

document = ["janeiro",
            "janeiro",
            "janeiro",
            "fevereiro",
            "fevereiro",
            "março",
            "abril",
            "maio",
            "junho",
            "julho",
            "agosto",
            "agosto",
            "agosto",
            "agosto",
            "setembro",
            "outubro",
            "outubro",
            "outubro",
            "outubro",
            "outubro",
            "novembro",
            "dezembro",
            "dezembro",
            "dezembro",
            "dezembro",
            "dezembro",
            "dezembro",
            "dezembro"
        ]

word_counts_dict = {} #creates an empty dict

print(document)

from collections import defaultdict

word_counts = defaultdict(int) #creates a dict with default value 0 by any given key-value, if not specified

print(word_counts)

for word in document:
    word_counts[word] += 1

print(word_counts)

from collections import Counter
c =  Counter([0, 1, 2, 0])

word_counts = Counter(document) #count the parameter i want to and puts in the order of biggest to smallest
print(word_counts)

for word, count in word_counts.most_common(12):
    print(word, count)

primes_below_10 = {2, 3, 5, 7}
document_set = set(document)

print(document_set)

number_x = 3
parity = "even" if number_x % 2 == 0 else "odd"

print(number_x)


