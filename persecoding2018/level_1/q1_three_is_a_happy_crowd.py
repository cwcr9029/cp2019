num1 = int(input())
num2 = int(input())
num3 = int(input())
if num1 + num2 == num3 or num1 + num3 == num2 or num2 + num3 == num1:
    print("HAPPY CROWD")
else:
    print("UNHAPPY CROWD")