## virtual enviroments

it's always a good practice to run python scripts in virtual enviroments, since it does not use my default python installation and does not mess with the versions of libraries i'm using.

## first class fucntions in python

as done in the book, in python we can assign a function to a variable without ever needing to execute the function.
```python
def greet(name):
    return f"Hello {name}!"

say_hello = greet
print(say_hello("Pedro"))
```

## slicing and stride

how to use stride:
list[start:stop:step]
