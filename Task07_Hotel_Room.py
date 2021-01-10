mount = input()
nights = int(input())
price_studio = 0
price_apartment = 0
discount_apartment = 0
discount_studio = 0

if nights <= 7:
    if mount == "May" or mount == "October":
        price_studio = 50
        price_apartment = 65
    elif mount == "June" or mount == "September":
        price_studio = 75.2
        price_apartment = 68.7
    else:
        price_studio = 76
        price_apartment = 77

if 7 < nights <= 14:
    if mount == "May" or mount == "October":
        price_studio = 50
        price_apartment = 65
        discount_studio = 5
    elif mount == "June" or mount == "September":
        price_studio = 75.20
        price_apartment = 68.70
    else:
        price_studio = 76
        price_apartment = 77

else:
    if mount == "May" or mount == "October":
        price_studio = 50
        price_apartment = 65
        discount_studio = 30
        discount_apartment = 10
    elif mount == "June" or mount == "September":
        price_studio = 75.2
        price_apartment = 68.7
        discount_studio = 20
        discount_apartment = 10
    else:
        price_studio = 76
        price_apartment = 77
        discount_apartment = 10

sum_apartment = (nights * price_apartment) - (nights * price_apartment * discount_apartment / 100)
sum_studio = (nights * price_studio) - (nights * price_studio * discount_studio / 100)

print(f"Apartment: {sum_apartment:.2f} lv.")
print(f"Studio: {sum_studio:.2f} lv.")


