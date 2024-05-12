

while True:
    country = input("Please write down a country name: ")
    country = country.strip()
    print(country)

    match country:
        case "USA":
            print("Hello")
        case "India":
            print("Namaste")
        case "Germany":
            print("Hallo")
        case "exit":
            break
        case _:
            print("Om tare tuttare ture soha")

print("Goodbye")
