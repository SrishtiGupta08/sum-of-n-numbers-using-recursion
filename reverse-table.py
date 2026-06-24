#reverse table using while loop

n=int(input("enter the number:"))  # user input
i=10   # initializ the counter variable
while(i>=1):  # condition continue the loop while i is greater than or equal to 1

    print("n","x",i,"=",n*i)   # print the table
    i-=1   # decre value of i -1 time




# reverse table using for loop

n=int(input("enter the number:"))  # user input
for i in range(10,0,-1):   # loop 10 to 1 descending order
    print(n,"x",i,"=",n*i)  # print the table
