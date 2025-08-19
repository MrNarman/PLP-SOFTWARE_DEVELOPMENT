# file  = open('newfile.pdf', 'w')
# file.write('This is a test file for writing binary data.\n')
# file.close()

# file = open('newfile.pdf', 'r')
# data = file.read()
# print(data)
# file.close()

#AAppending to a file
# file = open('newfile.pdf', 'a')
# file.write('Appending some more data to the file.\n')
# file.write('Today is very cold.\n')
# file.close()

# file = open('newfile.pdf', 'r')
# data = file.readline()
# print(data)
# file.close()

try:
    file = open('newfile.pdf', 'r')
    data = file.read()
    print(data)
    file.close()
except FileNotFoundError:
    print("The file does not exist.")
    # Handle the error, e.g., create the file or notify the user
finally:
    file.close()  # Ensure the file is closed if it was opened