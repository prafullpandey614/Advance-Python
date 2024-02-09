'''
Generators in Python are a special kind of iterator that allow you to iterate over a sequence of values lazily. 
They produce values one at a time and only when needed, which can save memory and improve performance, especially when dealing with large datasets. Generators are defined using functions and the yield keyword. Here's how they work:
'''

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b  # each time when next function is called code re runs from this line

# Using the Fibonacci generator
fib = fibonacci()
for _ in range(10):
    print(next(fib))  # Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
