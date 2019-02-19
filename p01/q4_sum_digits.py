number = int(input("Enter any integer between 0 and 1000: "))
result = 0
while number > 0:
    result += number % 10
    number = number // 10

print("The sum of the digits of that integer is " + str(result))