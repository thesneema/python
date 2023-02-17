n1 = 0
n2 = 1
limit = int(input("Enter the limit: "))
print("The fibonacci series upto ",limit," termsare:")
print(n1)
print(n2)
for i in range(limit - 2):
    n = n1 + n2
    print(n)
    n1 = n2
    n2 = n