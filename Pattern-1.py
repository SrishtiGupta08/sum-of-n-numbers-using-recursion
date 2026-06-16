n=int(input("enter the number: "))
i=1
while(i<=n):
    print(" "*(n-i),end="")
    print("*"*(i*2-1))
    i+=1

# now we will try this from for loop

n=int(input("enter the number: "))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(i*2-1))




