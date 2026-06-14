f1 = 1
f2 = 1

n = int(input("Enter the number of terms: "))
print(f1, f2, end=" ")
for i in range(0,n - 2):
    print(f1 + f2, end=" ")
    temp = f1
    f1 = f2
    f2 = temp + f2

print("")
sum = 1
for i in range(n,0,-1):
    sum *= i
print("Factorial of", n, "is", sum)