import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Orignal runtime complexity O(n^2)
# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# print(len(duplicates))

# runtime complexity O(n)
# Queue implementation
for _ in range(10000):
    if names_1[0] not in names_2:
        names_1.pop(0)
    else:
        duplicates.append(names_1[0])
        names_1.pop(0)
# runtime: 1.1590063571929932 seconds

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# ---
# for x in range(10000):
#     if names_1[x] in names_2:
#         duplicates.append(names_1[x])
# # runtime: 1.1426150798797607 seconds
#----
# # Create a dicitonary with keys as names and values 0-9999
# name_dict = dict(zip(names_1, range(10000)))

# # comprehension that looks for keys in names_2 list
# duplicates_dict = {k:v for (k,v) in name_dict.items() if k in names_2}

# # Extend duplicates list
# duplicates.extend(duplicates_dict.keys())
# # runtime: 1.1385281085968018 seconds