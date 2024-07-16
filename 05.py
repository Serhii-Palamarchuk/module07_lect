from collections import defaultdict

phone_numbers = [
    "0599993636",
    "0679993636",
    "0959993636",
    "0969993636",
    "0599993637",
    "0639993636",
    "0599993632",
    "0339993632"
]

res = defaultdict(list)
for ph in phone_numbers:
    if ph.startswith("050") or ph.startswith("095"):
        res["Vodafone"].append(ph)
    elif ph.startswith("067") or ph.startswith("096"):
        res["Kyivstar"].append(ph)

print(res)
