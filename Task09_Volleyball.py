import math
type_year = input()
feast_days = int(input())
home_city_holidays = int(input())

games = (48 - home_city_holidays) * (3 / 4) + (home_city_holidays) + (feast_days * 2 / 3)

if type_year == "leap":
    games = games * 1.15

print(math.floor(games))

