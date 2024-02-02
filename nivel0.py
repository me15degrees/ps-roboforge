def num(num):
    if num%3==0:
        return "Fizz"
    elif num%5==0:
        return "Buzz"
    elif num%3==0 and num%5==0:
        return "FizzBuzz"
    return "#"

result = num(7)
print(result)