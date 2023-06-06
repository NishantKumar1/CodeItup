# # Python Program structure
# # Write a proram to add two numbers
# a = 10
# b = 3
# c = a + b
# print(c)

# # Write a proram to subtract two numbers
# a = 20
# b = 10
# c = a-b
# print(c)

# # Write a proram to mutiply  two numbers

# a = 9
# b = 8
# c = a * b
# print(c)

# # Write a proram to divide two numbers
# n = 10
# b = 2
# c = n/b
# c = n//b
# print(c)

# # Write a proram to addition/subtraction/mutiplication/division in the same program
# a = 4
# b = 2
# add = a +b
# sub = a -b
# Mult = a * b
# Div = a //b

# print("Addition =",add)
# print("Subtraction =",sub)
# print("Mutiplication=" , Mult)
# print("Divide =",Div)

# #Write a program to accept electricity unit consumption and calculate total price at the rate of 5rs unit. Give a discount of 10% on all over bill?
# unit = int(input("Enter the Unit of electricity spend this month? :"))
# charge_per_unit = 5
# discount= 10
# bill = unit*charge_per_unit
# print(bill)
# discount_bill = bill * 10//100
# print(discount_bill)
# total_bill = bill-discount_bill
# print(total_bill)


# #Write a program to accept marks of 5 subjects and find total marks and percentage assuming full marks as 100 in each subject

# Maths = int(input("Please enter the marks obtained in Maths?: "))
# English= int(input("Please enter the marks obtained in English?:"))
# Science = int(input("Enter the marks obtained in Science?: "))
# SST = int(input("Enter the marks obtained in SST? :"))
# Hindi=int(input("Enter the marks obtained in Hindi? :"))
# Total_Subjects = 5
# Marks_per_subject = 100
# Total_Marks= Total_Subjects * Marks_per_subject
# print(Total_Marks)
# Marks_achieved_in_total= (Maths + English + Science+ SST+ Hindi)
# print(Marks_achieved_in_total)
# Percentage = Marks_achieved_in_total/Total_Marks * 100
# print(Percentage)


# # Write a program to swap values of two numbers.

a = 10
b = 11
c = a
a = b
b = c
print("Value of a", a)
print("Value of b", b)
print("Value of C", c)


# Write a program to accept total sales amount and find the profit amount 5 %?
Sales = int(input("Enter the total sales? :"))
profit = 5
total_sale_profit = Sales * profit // 100
print(f"total_sale_profit is = {total_sale_profit}")
total_profit= Sales+total_sale_profit
print(f"total_profit is equal to {total_profit}")