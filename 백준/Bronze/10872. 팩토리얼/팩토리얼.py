n = int(input())
	
def factorial(i):
    result = 1
    if i > 0:
        result = i * factorial(i - 1)
    return result

print(factorial(n))