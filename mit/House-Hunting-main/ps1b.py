"""
The program calculates how many months it will take for a user to save up enough money 
for a down payment. The programm assumes that user's investments earn a return of
r = 0.04 (or 4%) and the required down payment percentage is 0.25 (or 25%). 
The programm takes into account the user's pay raise that they have every six months. 
"""
 

annual_salary = 0.0 # user's annual salary will be entered by the user
monthly_salary = annual_salary / 12 
portion_saved = 0.0 #percent of salary to be saved every month will be entered by the user
total_cost = 0.0 #cost of a house will be entered by the user
portion_down_payment = 0.25 #the portion of a cost needed for the down payment is 25%
r = 0.04 #annual return from the current_savings investments

user_input = input("Enter your annual salary: ")
annual_salary = float(user_input)

user_input = input("Enter the percent of your salary to save: ")
portion_saved = float(user_input) / 100

user_input = input("Enter the cost of your dream home: ")
total_cost = float(user_input)

user_input = input("Enter your semi-annual pay raise percent: ")
semi_anual_raise = float(user_input) / 100

down_payment = total_cost * portion_down_payment #down payment amount that the user wants to save for
monthly_salary = annual_salary / 12 #calculate the monthly salary of the user
base = portion_saved * monthly_salary #calculate the base amount to be saved every month
current_savings = 0.0

count = 0

while down_payment > current_savings:
    current_savings += (current_savings * (r/12)) + base
    count += 1
    if count%6 == 0:
        monthly_salary += monthly_salary*semi_anual_raise
        base = portion_saved * monthly_salary

    
print("Number of months: ", count)
  
    

