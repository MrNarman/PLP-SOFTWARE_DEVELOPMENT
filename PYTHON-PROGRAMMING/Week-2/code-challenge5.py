# Store a list of words
words = ["apple", "banana", "pear", "kiwi", "grape", "melon", "fig"]

# Use list comprehension to filter words with odd number of characters
odd_length_words = [word for word in words if len(word) % 2 != 0]

# Display the result
print("Original words:", words)
print("Odd length words:", odd_length_words)
