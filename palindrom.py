num = int(input("Enter a number: "))
# print(num//10)
digit = 0
# while num > 0:
#     digit += 1
#     num = num // 10
# print("Number of digits:", digit)

while num > 0:
    ld = num % 10
    fd = num // (10 ** (digit - 1))
    if ld != fd:
        print("Not a palindrome")
        break
    num = num % (10 ** (digit - 1)) // 10
    digit -= 2
else:
    print("Palindrome") 