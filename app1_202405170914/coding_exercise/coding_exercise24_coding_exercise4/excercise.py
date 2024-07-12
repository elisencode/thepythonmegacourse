# Create a file called "file.txt"
file = open("file.txt", "x")

# Write the text "snail" there
file.write("snail")

file.close()

file = open("file.txt", "r")

content = file.read()

print(content)

file.close()
