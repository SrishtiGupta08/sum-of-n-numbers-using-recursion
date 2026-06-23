'''
* * * * *
 * * * *
  * * *
   * *
    *
by taking user input
'''

def pattern(): # function for pattern
     
     n=int(input("Enter the number: "))  # n is variable that store the user input
     count=1  
     for i in range(n,0,-1):  # loop

        print("* "*i)  # print the pattern
        print(" "*count,end="")  # end="" is used to stay on the same line
        count+=1
        
pattern() # function calling