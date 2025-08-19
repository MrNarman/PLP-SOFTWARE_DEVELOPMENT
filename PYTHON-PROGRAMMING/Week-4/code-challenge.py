read_file = open('input.txt', 'r')
data = read_file.read()
no_of_words = len(data.split())
upper_case_data = data.upper()

write_file = open('output.txt', 'w')
write_file.write(upper_case_data)
write_file.write(f'\nTotal number of words: {no_of_words}')
write_file.close()
    # This line will raise an error if file was never opened