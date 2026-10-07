items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

print("Shopping List:")

number = 1

for item in items:
    print(number, ".", item)
    number += 1

count = 0

for item in items:
    if len(item) > 4:
        count += 1

print("Items with more than 4 letters:", count)

longest = ""

for item in items:
    if len(item) > len(longest):
        longest = item

print("Longest item:", longest)
