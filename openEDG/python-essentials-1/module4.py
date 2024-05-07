"""
Functions
"""
def fruits(nApples, nPlums, nCherries):
    print("We have", nApples, "apples")
    print("We have", nPlums, "plums")
    print("We have", nCherries, "cherries")

fruits(2, 5, 7) #positional arguments
fruits(nCherries=2, nApples=5, nPlums=7) #keyword arguments
fruits(2, nCherries=0, nPlums=7) #mix positional and keyword.Positional should go first
