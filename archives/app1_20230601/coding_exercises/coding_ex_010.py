ranking = ['John', 'Sen', 'Lisa']

for rank in ranking:
    user_input = int(input("Enter rank number: ")) - 1

    print(ranking[user_input])

    if ranking[user_input] == ranking[1]:
        break
