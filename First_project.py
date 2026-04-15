# Day-1 for Python Project....
# Name = Rent Calculate for room..
# Inputs we need fro the user
# total rent
# Total food ordered for snacking and other bills.
# Electricity units Spend by room also
# charge Per UNit
# Persons living in room
# this python project for lern a bacis undersanding of  python 


rent = int(input("Enter your hostel/flat rent = "))
food =int(input("Enter the amount of food ordered = "))
electricity_spend = int(input("Enter the total of electricity spend = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the numbers of persons living in room/flat = "))

total_bill = electricity_spend * charge_per_unit

# this will be calculated a  rent for this room and addition thigs that take for each one also ...
output = (food + rent + total_bill) // persons

print("Each person will pay this amount = ", output)
