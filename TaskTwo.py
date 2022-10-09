print("\033c")

X = int(input("Введите число X: "))
Y = int(input("Введите число Y: "))
Z = int(input("Введите число Z: "))

for X in range(2):
        for Y in range(2):
            for Z in range(2):
                print(not (X or Y or Z) == (not X and not Y and not Z))
                print(X, Y, Z)