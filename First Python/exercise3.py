seasonConversions = {
    "Spr": "Spring",
    "Sum": "Summer",
    "Aut": "Autumn",
    "Win": "Winter"
}
print(seasonConversions)
print(seasonConversions["Win"])
print(seasonConversions.get("Sum"))
print(seasonConversions.get("Aut", "there's sth"))
print(seasonConversions.get("Sfgg", " No, there's not"))


