num = input("Enter a number: ")
num = int(num)
if num < 0:
    if num % 2 == 0:
        print(f"{num} is Negative Even Number")
    elif num % 2 != 0:
        print(f"{num} is Negative Odd Number")
elif num > 0:
    if num % 2 == 0:
        print(f"{num} is Positive Even Number")
    elif num % 2 != 0:
        print(f"{num} is Positive Odd Number")
else:
    print(f"{num} is Zero")