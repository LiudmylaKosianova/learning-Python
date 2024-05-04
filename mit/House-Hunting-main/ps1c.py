"""
The programm calculates optimal percentage of the salary to be saved every months for the user, 
if they want to save up for the downpayment in 36 months.
User's salary and the price of a house is taken as an input. 
The programm assumes, that
- the user gets the pay raise of 7% every six month
- the user's investments get annual return of 4%
- the downpayment amount is 25% of the house price
"""

print("Welcome to savings calculator!\n")

user_input = input("Enter your annual salary: ")
annual_salary = float(user_input) #user's annual salary
monthly_salary = annual_salary / 12 #calculate user's monthly salary
print("\tYour monthly salary is: ", monthly_salary)
print("\tI assume you have a pay raise of 7% every half a year.")
print("\tI also assume you make wise investments that return 4% annually.")


user_input = input("Enter the cost of your dream home: ")
total_cost = float(user_input) #the total cost of the house
down_payment = total_cost * 0.25 #the downpayment that the user needs to save up for 
print("\tYou need to save ", down_payment, " in three years time.")
 

def calc_months (down_payment,monthly_salary,portion_to_save):

    """
    Calculates how many months is needed to save up for the downpayment
    Parameters:
    -down_payment is an amount of money that should be paid
    -monthly_salary is actual salary per month
    -portion_to_save is a percentage of monthly salary that is to be saved
    Returns:
    number of months needed to save up for the downpayment
    """


    down_payment = down_payment
    monthly_salary = monthly_salary
    portion_to_save = portion_to_save

    count = 0
    current_savings = 0.0
    base = portion_to_save * monthly_salary  

    while down_payment > current_savings:
        current_savings += (current_savings * (0.04/12)) + base
        count += 1
        if count%6 == 0:
            monthly_salary += monthly_salary*0.07
            base = portion_to_save * monthly_salary

    return count


def calc_portion (down_payment,monthly_salary):

    """
    Implements binary search to find the right amount to save 
    Parameters:
    -down_payment is an amount of money that should be paid
    -monthly_salary is actual salary per month    
    Returns:
    percent of the monthly salary to save in order to save up for the downpayment in 36 months
    """
    down_payment = down_payment
    monthly_salary = monthly_salary

    portion_list = sorted(range(0,10000))#create a sorted list in range 0-10000 representing percents
    low = 0 #index for searching in the list
    high = len(portion_list) - 1 #index for searching in the list

    while low <= high:
        mid = (low + high) // 2 

        portion_to_save = portion_list[mid] / 10000
        N_months = calc_months(down_payment,monthly_salary,portion_to_save)
        

        if N_months == 36:
            return portion_to_save
        elif N_months > 36:
            low = mid + 1
        else:
            high = mid - 1
    return -1

portion = calc_portion (down_payment,monthly_salary)
portion_print = "{:.2f}".format(portion*100)
print("\tThe recomended portion to save: ", portion_print, "%")


