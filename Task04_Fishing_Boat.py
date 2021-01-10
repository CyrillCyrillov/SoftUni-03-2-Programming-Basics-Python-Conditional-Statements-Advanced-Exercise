budged = int(input())
season = input()
number_of_fishermen = int(input())
price = 0
discount = 0
additional_discount = 0

if season == "Spring":
    price = 3000
elif season == "Summer" or season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600

if number_of_fishermen <= 6:
    discount = 10
elif 7 <= number_of_fishermen <= 11:
    discount = 15
elif number_of_fishermen > 12:
    discount = 25

if (number_of_fishermen % 2) == 0 and season != "Autumn":
    additional_discount = 5

price = price - (price * discount / 100.0)
price = price - (price * additional_discount / 100.0)

if price <= budged:
    print(f"Yes! You have {budged - price:.2f} leva left.")
else:
    print(f"Not enough money! You need {price - budged:.2f} leva.")






