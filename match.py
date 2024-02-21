# salary = float(input("enter the salary : "))
# match salary:
#     case salary if salary <= 50000:
#         print("low income tax is to be paid")
#     case salary if salary > 50000 and salary <=100000:
#         tax=salary*0.28
#         print("medium income tax is to be paid",round(tax,2))
#     case _:
#         tax=(salary-50001)*0.3+579
#         print("high income tax is to be paid ",round(tax,2))

# list1 = [0,1]
# for i in range(10):
#     list1.append(list1[-1]+list1[-2])
# print(list1)


# Amstrong number

num = int(input("enter_a_number: "))
len_num = len(str(num))
check = num
amstrong_num = 0

while num  != 0:
    digit = num % 10
    amstrong_num = amstrong_num + digit ** len_num
    num = num//10


if amstrong_num == check:
    print("It is a amstrong number : ", amstrong_num)
else:
    print("It is not a amstrong number : ", amstrong_num)


# prime number
    
num_1 = int(input("enter a number: "))

for i in range(2,int((num_1/2))+1):
    if num_1%i==0:
        print(f"{num_1} is not a prime number ")
        break
    else:
        print("{} is a prime number".format(num_1))
        break

# write a code for factorial using python without using functions
factorial=1
n=int(input("Enter the number of you want to find the factorial:"))
for i in range(1,n+1):
    factorial = factorial*i
print("The Factorial of {0} is: {1} ".format(n,factorial))    
    