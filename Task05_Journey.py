budged = float(input())
season = input()

if budged <= 100:
    print("Somewhere in Bulgaria")
    if season == "summer":
        print(f"Camp - {budged * 0.3:.2f}")
    else:
        print(f"Hotel - {budged * 0.7:.2f}")
elif 100 < budged <= 1000:
    print("Somewhere in Balkans")
    if season == "summer":
        print(f"Camp - {budged * 0.4:.2f}")
    else:
        print(f"Hotel - {budged * 0.8:.2f}")
else:
    print("Somewhere in Europe")
    print(f"Hotel - {budged * 0.9:.2f}")


