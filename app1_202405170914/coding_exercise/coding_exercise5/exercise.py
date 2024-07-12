prompts = input("Please enter a new member: ")

with open("members.txt","r") as reader:
    # Read and print the entire file
    print(reader.read())

with open("members.txt", "a") as myfile:
    myfile.write(prompts)

with open("members.txt", "r") as reader:
    print(reader.read())
