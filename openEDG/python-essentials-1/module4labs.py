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
		
"""
Leap year, months and days
Returns corresponding day of the year
"""
 
def day_of_year(year, month, day):
	if (year<=0) or (month not in range(1,13)) or (day not in range(1,32)):
		return None
	dayN=0
	
	for i in range(1,month):		 
		dayN += days_in_month(year,i)
	dayN += day
	return dayN
	
print(day_of_year(2000, 12, 31))
print(day_of_year(2024,12,31))
print(day_of_year(2023, 12,31))

"""
Prime or not
"""
def is_prime(num):
	if num==1 or num==2:
		return True
	for i in range(2,num):
		if num%i==0:
			return False
	return True
 
print("Prime numbers: ", end=" ")
for i in range(1, 20):
	
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()

"""
Europe: fuel consumed per 100 kilometers
USA: miles travelled using 1 gallon of fuel
convert 
"""
#1 mile = 1609.344 metres
#1 gallon = 3.785411784 litres

def liters_100km_to_miles_gallon(litres):
	miles = None
	gallons = litres / 3.785411784
	miles = 100000 / 1609.344
	
	return miles / gallons

def miles_gallon_to_liters_100km(miles):
	litres = None
	metres = miles * 1609.344
	km = metres / 1000
	litres = 3.785411784

	return (litres * 100)/km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

 



