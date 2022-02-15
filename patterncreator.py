# Python code for beginners.
# This code creats pattern using star symbol.
# This code asks for number of rows and gives you option to print pattern(using *) in two ways. 


while(True):
    n = int(input("Enter the number of rows you want = "))
    a = "*"
    o = int(input("Enter either 0 or 1 = "))
    if o == 1:
        for i in range(1, n+1):
            print(a*i)
    else:
        for i in range(n,0,-1):
            print(a*i)
            
print("This was your selected pattern...")
