"""
Leap year
"""
def is_year_leap(year): 
	if year%100!=0 and year%4==0:
		return True
	elif year%100==0 and year%400==0:
		return True
	else:
		return False	


test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
		
"""
Leap year and months
"""
#def is_year_leap(year):
#
# Your code from LAB 4.3.1.6.
#

def days_in_month(year, month):
	days31 = [1,3,5,7,8,10,12]
	if month==2:
		if is_year_leap(year):
			return 29
		else:
			return 28
	if month in days31:
		return 31
	else:
		return 30 

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")

