X = int(input())
Y = int(input())

if X > Y:
    X, Y = Y, X

for num in range(X + 1, Y):
    if num % 5 == 2 or num % 5 == 3:
        print(num)
