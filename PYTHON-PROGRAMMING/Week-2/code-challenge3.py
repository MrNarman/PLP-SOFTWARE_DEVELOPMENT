person_details = {}

required_fields = ["name", "age", "city"]

for field in required_fields:
    value = input(f"Please enter your {field}: ")
    person_details[field] = value

print("Here are the details you entered:")
print(person_details)