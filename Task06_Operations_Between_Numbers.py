n1 = int(input())
n2 = int(input())
operation = input()

if operation == "+":
    if (n1 + n2) % 2 == 0:
        print(f"{n1} {operation} {n2} = {n1 + n2} - even")
    else:
        print(f"{n1} {operation} {n2} = {n1 + n2} - odd")
elif operation == "-":
    if (n1 - n2) % 2 == 0:
        print(f"{n1} {operation} {n2} = {n1 - n2} - even")
    else:
        print(f"{n1} {operation} {n2} = {n1 - n2} - odd")
elif operation == "*":
    if (n1 * n2) % 2 == 0:
        print(f"{n1} {operation} {n2} = {n1 * n2} - even")
    else:
        print(f"{n1} {operation} {n2} = {n1 * n2} - odd")
else:
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    elif operation == "/":
        print(f"{n1} / {n2} = {n1 / n2:.2f}")
    else:
        print(f"{n1} % {n2} = {n1 % n2}")

