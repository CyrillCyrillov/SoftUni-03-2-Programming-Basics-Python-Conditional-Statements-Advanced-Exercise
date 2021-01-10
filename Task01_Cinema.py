type = input()
rows = int(input())
colums = int(input())

if type == "Premiere":
    print(f"{12 * rows * colums:.2f} leva")
elif type == "Normal":
    print(f"{7.5 * rows * colums:.2f} leva")
elif type == "Discount":
    print(f"{5 * rows * colums:.2f} leva")


