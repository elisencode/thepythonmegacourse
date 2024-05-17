ranking = ['John', 'Sen', 'Lisa']

for rank in ranking:
    user_input = input("Enter a name: ")

    if user_input == ranking[1]:
        print(ranking.index(user_input) + 1)
        break