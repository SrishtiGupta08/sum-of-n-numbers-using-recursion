'''
*******
 *****
  ***
   *

'''

def pattern(): # function for pattern
     
      count=1  
      for i in range(7,0,-2):  # loop

        print("*"*i)  # print the pattern
        print(" "*count,end="") # end="" is used to stay on the same line
        count+=1   
        
pattern() # function calling
