num_count = int(input("How many numbers you want to enter: "))
num_list = []
for num in range(num_count):
    number = int(input("Enter a number: "))
    num_list.append(number)
print("The numbers you entered are: ", num_list)
#sum of numbers
print("The sum of numbers is: ", sum(num_list))
#average of numbers
print("The average of numbers is: ", sum(num_list)/len(num_list))
#number of positive numbers
positive_count = 0
for num in num_list:
    if num > 0:
        positive_count += 1
print("The count of positive numbers is: ", positive_count)
#number of negative numbers
negative_count = 0
for num in num_list:
    if num < 0:
        negative_count += 1
print("The count of negative numbers is: ", negative_count)
#number of zeros
zero_count = 0
for num in num_list:
    if num == 0:
        zero_count += 1
print("The count of zeros is: ", zero_count)
#number of even numbers
even_number_count = 0
for num in num_list:
    if num %2 == 0:
        even_number_count += 1
print("The count of even numbers is: ", even_number_count)
#number of odd numbers
odd_number_count = 0
for num in num_list:
    if num %2 != 0:
        odd_number_count += 1
print("The count of odd numbers is: ", odd_number_count)
#largest number
largest_number = max(num_list)
print("The largest number is: ", largest_number)
#smallest number
smallest_number = min(num_list)
print(f"{smallest_number} is the smallest number in given list")