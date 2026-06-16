#this program is for printing the hollow square pattern

n=int(input("enter the number:"))  #this line for taking user input

for i in range(1,n+1):   #for loop for printing the pattern n+1 times

    if(i==1 or i==n):   #this condition for printing the first and last line of the pattern

        print("* "*n)   #this line for printing the first and last line of the pattern

    else:

        print("*",end="")    #print the first star of the line

        print(" "*(2*n-3),end="")   #this line for printing the spaces between the stars
       
        print("*")   #this line for printing the last star of the line



#Same program using while loop

i=1

while(i<=n):   #while loop for printing the pattern

    if(i==1 or i==n):   #this condition for printing the first and last line of the pattern

        print("* "*n)   #this line for printing the first and last line of the pattern

    else:

        print("*",end="")     #print the first star of the line 

        print(" "*(2*n-3),end="")   #this line for printing the spaces between the stars

        print("*")   #this line for printing the last star of the line 

    i=i+1   #incrementing the value of i to avoid infinite loop
