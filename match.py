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

# factorial 
factorial=1
n=int(input("Enter the number of you want to find the factorial:"))
for i in range(1,n+1):
    factorial = factorial*i
print("The Factorial of {0} is: {1} ".format(n,factorial))    

# palindrome 
s=input("Enter a string:")
rev=""
temp=s[::-1]

print("The string is: ",s)
print("The reverse string is:", temp)

if s.lower()==temp.lower():
    print("The given string is a Palindrome.")
else:
    print("The given string is not a Palindrome.")

# reverse number

num = int(input("Enter a number : "))
reverse_num = 0
check_num = num

while num>0:
    digit = num%10
    reverse_num = reverse_num * 10 + digit
    num = num//10

if check_num == reverse_num:
    print("Given number is a palindrome number")
else:
    print("Given number is not a palindrome number")


# biggest of three numbers

def largest_num(first_num,second_num,third_num):

    if first_num > second_num and first_num > third_num:
        print(f"{first_num} is the largest number")
    elif  second_num > first_num and second_num > third_num:
         print(f"{second_num} is the largest number")
    else:
        print(f"{third_num} is the largest number")

largest_num(567,342,987)

# printing prime numbers for given range

num = int(input("Enter the starting number of the range :"))
end = int(input("Enter the ending number of the range :"))

for i in range(num, end+1):
    if i > 1:
        for j in range(2,i):
            if (i % j) == 0:
                break
        else:
            print(i)

#increment the value by 1

num = int(input("Enter the number : "))
print("Incremented Number : ",num+1)

#Determine weather a person is eligible to vote by using  input 

age_of_the_person = int(input("Enter the age: "))

if  age_of_the_person >= 18:
    print("Eligible")
else:
    print( "Not Eligible")

# A company decides to give bonus to all its employees on New year. A 10% bonus on salary for all the male workers and
# 25% to females. build a programme to enter Salary and Gender(m or F) of employee. 
    
salary_of_employee = int(input("Enter thr salary : "))
gender = input("Enter the gender(M/F): ")

gender = gender.lower()

if gender == "f":
    salary = salary_of_employee + salary_of_employee*0.25
    print(f"The new salary after adding 25% to female employees is {salary}")
else:
    salary = salary_of_employee + salary_of_employee*0.1
    print(f"The new salary after adding 10% to male employees is {salary}")

# check weather the number is positive or negitive or equal to zero using input
    
User_choice = int(input( "Enter any number :  "))
if User_choice < 0:
   print ("Your number is Negative.")
elif User_choice > 0:
    print("Your number is positive")
else:
    print("Your number is zero")


# Test Weather the charcter is vowel or not vowel using input
enter_a_char = input( "Enter signle character : ")
enter_a_char = enter_a_char.lower()
vowels = ['a','e','i','o','u']
if enter_a_char  in vowels:
    print("Entered char is Vowel")
else:
    print("Entered char is  not Vowel")

#Given an integer input perform the following conditional actions:

#If n is odd, print odd
#If n is even and in the inclusive range of 2 to 5, print small
#If n is even and in the inclusive range of 6 to 20, print medium
#If n is even and greater than 20, print big
    
check_num = int(input("Enter the Number : "))

if check_num %2 != 0:
    print("The entered {0} is odd".format(check_num))
elif check_num % 2 ==0:
    if check_num > 2 and check_num <= 5:
        print("{0} is a small number ".format(check_num))
    elif 6 <= check_num <= 20:
        print("{0} is a medium number".format(check_num))
    else:
        print("{0} is a big number".format(check_num))

# print first 10 numbers using while loop
        
num = 1
while num<=10:
    print(num)
    num = num+1
# find average and sum for first 10 numbers using while loop
num = 10
sum_of_num = num
total_of_num = 0
while num<=0:
    total_of_num = total_of_num + num
    num -= 1
average = total_of_num / num
print("Sum of First 10 natural numbers is :",sum_of_num)
print("Average of First 10 natural numbers is : ",average)

#Draw a line using while loop 

num = int(input("enter the number greater than 600 : "))

while num>=0:
    print("_",end="")
    num = num-1
#calculate the sum of m to n  numbers using input
    
start_num = int(input("Enter the start_num : "))
last_num = int(input("Enter the  last_num : "))
sum_of_start_and_last = 0
for i in range(start_num,last_num+1):

    sum_of_start_and_last = sum_of_start_and_last + i
    print(sum_of_start_and_last)
print(sum_of_start_and_last)


# countdown 10 to 0 using input

num =  int(input('Enter any number : '))

for i in range(num,0,-1):

    num =  num - i


    print(i)
print(num)