type_of_flowers = input()
number_of_flowers = int(input())
budged = int(input())
price = 0
discount = 0

if type_of_flowers == "Roses":
    price = 5
    if number_of_flowers > 80:
        discount = 10
elif type_of_flowers == "Dahlias":
    price = 3.8
    if number_of_flowers > 90:
        discount = 15
elif type_of_flowers == "Tulips":
    price = 2.8
    if number_of_flowers > 80:
        discount = 15
elif type_of_flowers == "Narcissus":
    price = 3
    if number_of_flowers < 120:
        discount = -15
elif type_of_flowers == "Gladiolus":
    price = 2.5
    if number_of_flowers < 80:
        discount = -20

sum = (number_of_flowers * price) - ((number_of_flowers * price) * (discount / 100.0))

if sum > budged:
    print(f"Not enough money, you need {sum - budged:.2f} leva more.")
else:
    print(f"Hey, you have a great garden with {number_of_flowers} {type_of_flowers} and {budged - sum:.2f} leva left.")




