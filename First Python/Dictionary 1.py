# create dictionary using { } and :
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
print()


# create dictionary using dict() constructor and =
d2 = dict(a = "Geeks", b = "for", c = "Geeks")
print(d2)
print()


dictio = { "name": "Alice", 1: "Python", (1, 2): [1, 2, 4],  "Nested": {'x': 'Welcome', 'y': 'To', 'z': 'Milano'} }

# Accessing Dictionary Items
# key within square brackets [key] or get() method.

# Access using key
print(dictio[ "name" ])


# Access using get()
print(dictio.get( "Nested" ))


# REMOVING DICTIONARY ITEMS
# Using del to remove an item
del dictio["Nested"]
print(dictio)

# Using pop() to remove an item and return the value
val = dictio.pop((1, 2))
print(val)
print(dictio)

# Using popitem to removes and returns
# the last key-value pair.
key, val = dictio.popitem()  # deletes last item
print(f"Key: {key}, Value: {val}")

# Clear all items from the dictionary
dictio.clear()
print(dictio)