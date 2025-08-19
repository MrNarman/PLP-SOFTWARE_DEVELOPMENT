try:
    with open('version1.txt', 'r') as file:
        content = file.read()

    with open('v1_output.txt', 'w') as output_file:
        output_file.write(content.upper())
        word_count = len(content.split())
        output_file.write(f'\nTotal number of words: {word_count}')

except FileNotFoundError:
    print("File not found. Please check the file path and try again.")