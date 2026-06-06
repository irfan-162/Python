a,b,c = map(int, input("Enter three numbers: ").split())
largest = max(a,b,c)
smallest = min(a,b,c)

if a < largest and a > smallest:
    print("Middle:", a)
elif b < largest and b > smallest:
    print("Middle:", b)
else: 
    print("Middle:", c)    