"""
Your class will be called Timer. 
Its constructor accepts three arguments representing 
hours (a value from range [0..23] - we will be using the military time), 
minutes (from range [0..59]) 
and seconds (from range [0..59]).

Zero is the default value for all of the above parameters. 
There is no need to perform any validation checks.

The class itself should provide the following facilities:

objects of the class should be "printable", 
i.e. they should be able to implicitly convert themselves into strings of the following form: 
"hh:mm:ss", with leading zeros added when any of the values is less than 10;

the class should be equipped with parameterless methods called
next_second() and previous_second(), 
incrementing the time stored inside objects by +1/-1 second respectively.
"""
class Timer:
    def __init__(self,h,m,s):
        self.__h = h
        self.__m = m
        self.__s = s
        

    def __str__(self):
        currentTime =f"{self.__h}:{self.__m}:{self.__s}"
        return currentTime
         
    # def next_second(self):
    #     #
    #     # Write code here
    #     #

    # def prev_second(self):
    #     #
    #     # Write code here
    #     #


timer = Timer(23, 59, 59)
print(timer)
# timer.next_second()
# print(timer)
# timer.prev_second()
# print(timer)
