'''

*
***
*****
*******

'''
# code for this pattern using for loop by taking input from user

n=int(input("enter the no.: "))   #this line for taking input from user

for i in range(1,n+1):  #for loop for printing the pattern n+1 times

    print("*"*(2*i-1))  #this line prints the stars for each row



    
# same pattern using while loop

n=int(input("enter the no.: "))   # this line for taking input from user

i=1   
while(i<=n):     # while loop for printing the pattern n+1 times

    print("*"*(2*i-1))   # this line prints the stars for each row

    i+=1    # incrementing the value of i to avoid infinite loop 