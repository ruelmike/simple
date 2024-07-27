# Example of the fibnaccie sequence

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
'''
print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
'''

for n in range(10):
    my_var = "n=", n,  "fib(n)= ", fib(n)
    print(fib(n))
    your_var = n**2
    # print(my_var)
    # print(your_var)
