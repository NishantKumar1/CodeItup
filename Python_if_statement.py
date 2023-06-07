# Write a program to check whether a number is odd /even
# n = int(input("Enter the number you want to check if it is even or odd? :"))
# if n %2 == 0:
#     print(f"{n} is even number")
# else:
#     print(f"{n} is odd number")   


# Write a program to check whether an person is able to vote or not?
# age = int(input("Please enter your age as per your Voter Id or Aadhar Card? :"))
# if age >= 18:
#     print(f"Your age is {age} and as per your records, you are eligible to Vote.")
# else:
#     print(f"Your age is {age} and as per the records, you are not eligible to Vote.")


# Write a program to find max between two numbers?
# a = int(input("Enter your 1st number? :"))
# b = int(input("Enter your 2nd number? :"))
# if a > b:
#     print(f"{a} is the max number")
# else:
#     print(f"{b}is the Max number")


# Write a program to find max between three numbers?JaiHanuman@296

# a = int(input("Enter the number? :"))
# b = int(input("Enter the number? :"))
# c = int(input("Enter the number? :"))
# if a > b and a > c:
#     print(f"{a} is the Max number")
# elif b>a and b>c:
#     print(f"{b} is the Max number")
# else:
#     print(f"{c} is the Max number")

# Write a program to check whether a given number is postive, negative or zero.
# n = int(input("Enter the number you want to check? :"))
# if n > 0:
#     print(f"Number {n} is a positive number")
# elif n < 0:
#     print(f"Number {n} is a negative number")
# else:
#     print(f"Number {n} is Zero")

# Write a program to find the middle number in a group of three numbers.
# a = int(input("Enter the 1st number? :"))
# b = int(input("Enter the second number? :"))
# c = int(input("Enter the third number? :"))
# if a > b and a < c or a < b and a >c:
#     print(f"Number {a} is middle number")     
# elif b > a and b < c or b<a and b>c:
#     print(f"Number {b} is middle number")
# else:
#     print(f"Number {c} is middle number")


# Write a program to calculate total marsks in 5 subjects(Full marks = 100) as well as percentage of marks and divison as the following condition.
# Percentage >= 80--- Grade A
# Percentage >= 60----Grade B
# Percentage > 40-----Grade C
# Percentage <40 -----Grade D

Maths = int(input("Enter the number of marks for Maths? :"))
English = int(input("Enter the number of marks for English> :"))
Science = int(input("Enter the number of marks for Science? :"))
SST= int(input("Enter the number of marks for SST? :"))
Hindi= int(input("Enter the number of marks for Hindi? :"))
Total_marks_per_subject = 100
Total_marks_all_subjects = 500
Total_marks_obtained = Maths + English + Science + SST + Hindi
Percentage = Total_marks_obtained/Total_marks_all_subjects * 100
print(Percentage)
if Percentage >=80:
    print(f"Your Grade is A")
elif Percentage>=60:
    print("Your Grade is B")
elif Percentage>40:
    print("Your Grade C")
else:
    print("Your Grade is D")
        