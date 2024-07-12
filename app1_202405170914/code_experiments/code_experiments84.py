# variable named 'file'

with open("../files/doc.txt", "r") as file:
    print("Hello")
    content = file.read()

print(content)
