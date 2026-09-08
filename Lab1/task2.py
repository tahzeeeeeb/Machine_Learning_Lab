checkInput = int(input("Enter a number: "))
iterations = int(checkInput/2)
count = 0

for i in range (2, iterations):
    if(checkInput % i) == 0: count+=1

if count == 0: print("Prime")
else: print("non-prime")

