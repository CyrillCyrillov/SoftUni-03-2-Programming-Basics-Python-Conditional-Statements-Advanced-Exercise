degrees = int(input())
part_of_the_day = input()
outfit = str
shoes = str

if part_of_the_day == "Evening":
    outfit = "Shirt"
    shoes = "Moccasins"
elif part_of_the_day == "Morning" and 10 <= degrees <= 18:
    outfit = "Sweatshirt"
    shoes = "Sneakers"
elif part_of_the_day == "Morning" and 18 < degrees <= 24:
    outfit = "Shirt"
    shoes = "Moccasins"
elif part_of_the_day == "Morning" and degrees >= 25:
    outfit = "T-Shirt"
    shoes = "Sandals"
elif part_of_the_day == "Afternoon" and 10 <= degrees <= 18:
    outfit = "Shirt"
    shoes = "Moccasins"
elif part_of_the_day == "Afternoon" and 18 < degrees <= 24:
    outfit = "T-Shirt"
    shoes = "Sandals"
elif part_of_the_day == "Afternoon" and degrees >= 25:
    outfit = "Swim Suit"
    shoes = "Barefoot"

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
