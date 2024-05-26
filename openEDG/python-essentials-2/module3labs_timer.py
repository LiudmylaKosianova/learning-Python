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
    def __init__(self,h=0,m=0,s=0):
        self.__h = h
        self.__m = m
        self.__s = s        

    def __str__(self):
        timeList = [str(self.__h), str(self.__m), str(self.__s)]
        
        for i in range(3):
            if len(timeList[i]) == 1:
                timeList[i] = "0" + timeList[i]            
                
        currentTime = timeList[0]+":"+timeList[1]+":"+timeList[2]
        return currentTime
         
    def next_second(self):
        if self.__s == 59:
            setattr(self, "_Timer__s", 0)      
            setattr(self, "_Timer__m", self.__m + 1)
            if self.__m == 60:
                setattr(self, "_Timer__m", 0)
                setattr(self, "_Timer__h", self.__h + 1)
                if self.__h == 24:
                    setattr(self, "_Timer__h", 0)
        else:
            setattr(self, "_Timer__s", self.__s + 1) 

    def prev_second(self):
        if self.__s == 0:
            setattr(self, "_Timer__s", 59)      
            setattr(self, "_Timer__m", self.__m - 1)
            if self.__m == -1:
                setattr(self, "_Timer__m", 59)
                setattr(self, "_Timer__h", self.__h - 1)
                if self.__h == -1:
                    setattr(self, "_Timer__h", 23)
        else:
            setattr(self, "_Timer__s", self.__s - 1) 
        #
        # Write code here
        #


timer = Timer(23,59,59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
