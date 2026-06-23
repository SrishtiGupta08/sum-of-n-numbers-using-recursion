'''
*****
****
***
**
*
by taking user input
'''

def pattern(): # function for pattern
     
     n=int(input("Enter the number: "))  # n is variable in which user input will be store

     for i in range(n,0,-1):  # loop

        print("*"*i)  # print the pattern
        
pattern() # function calling
