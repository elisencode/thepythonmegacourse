# Bug:
# with open("file.txt", 'r') as file:
#     print(file.read())
#     print(len(file.read))

# Solution:
with open("file.txt", 'r') as file:
    content = file.read()

print(content)
print(len(content))
