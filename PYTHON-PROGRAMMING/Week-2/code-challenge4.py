first_set = set()
second_set = set()

for i in range(3):
    first_number = int(input("Enter a number for the first set: "))
    first_set.add(first_number)

print("\n")

for i in range(3):
    second_number = int(input("Enter a number for the second set: "))
    second_set.add(second_number)

print("\nThe intersection of the two sets is:", first_set.intersection(second_set))