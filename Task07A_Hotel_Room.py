mount = input()
nights = int(input())
sum_studio = 0
sum_apartment = 0

if mount == "May" or mount == "October":
    sum_studio = 50 * nights
    sum_apartment = 65 * nights
    if 7 < nights <= 14:
        sum_studio = sum_studio * 0.95
    elif nights > 14:
        sum_studio = sum_studio * 0.7
        sum_apartment = sum_apartment * 0.9
elif mount == "June" or mount == "September":
    sum_studio = 75.2 * nights
    sum_apartment = 68.7 * nights
    if nights > 14:
        sum_studio = sum_studio * 0.8
        sum_apartment = sum_apartment * 0.9
elif mount == "July" or mount == "August":
    sum_studio = 76 * nights
    sum_apartment = 77 * nights
    if nights > 14:
        sum_apartment = sum_apartment * 0.9

print(f"Apartment: {sum_apartment:.2f} lv.")
print(f"Studio: {sum_studio:.2f} lv.")
