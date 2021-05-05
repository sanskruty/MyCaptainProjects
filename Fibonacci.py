number_of_iterations = int(input("How many iteration of fibonacci do you want?\t"))

a = 0
b = 1
print(a, b, end=" ")
for iter in range(1, number_of_iterations):
    c = a + b
    a = b
    b = c
    print(c, end=" ")