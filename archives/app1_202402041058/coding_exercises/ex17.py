ips = ['100.122.133.105', '100.122.133.111']

user_input = int(input("Enter the index of the IP you want: "))

message = f"You chose {ips[user_input]}"

if user_input == 0:
    print(message)
elif user_input == 1:
    print(message)
else:
    print("Error 404")

# while user_input < len(ips):
#     if user_input == ips[0] :
#         print(f"You chose {ips[0]}")