import time
from random import randint

year = "2024"

phrase = "\"Accrochez-vous ! Ne lâchez pas !\""


def thankyou():
    thankyou_string = """\tVotre phrase résonne dans ma tête et me motive à 
    persévérer pour accomplir mon objectif.

    Ma trajectoire de vie n'est plus la même grâce à votre guidage telle une lumière 
    blanche brillant au travers d'un sombre brouillard.

    Je progresse à chaque fois grâce à vos retours constructifs et pertinents.

    Vous êtes un professeur et un mentor exceptionnel, doté d'un sourire bienveillant, 
    d'une accessibilité et d'une écoute attentive.

    J'ai beaucoup de chance d'être votre étudiante.

    J'espère qu'un jour vous serez fier de moi en tant que votre ancienne élève qui 
    apportera sa contribution dans ce monde : « J'apporte à beaucoup d'autres personnes 
    sur la planète quelque chose qui ait une valeur solide et durable. »\n

    Je vous remercie encore une fois du fond du cœur.\n

    很有幸能够成为您的带教学生, 感谢您!\n
    """

    thankyou = thankyou_string.center(8, '*')

    print(thankyou + '\n')


happy_new_year_string_fr = "\tBonne année ! 🎉\n"
happy_new_year_string_en = "\tHappy New Year! 🎉\n"
happy_new_year_string_ch = "\t新年快乐! 🎉\n"


def happy_new_year():
    space = ""

    for i in range(1, 888):
        count = randint(1, 100)
        while count > 0:
            space += " "
            count -= 1

        if i % 10 == 0:
            thankyou()
            print(space + "🍀" + "😊" + " " + year + "\n")
            print(space + happy_new_year_string_fr)
            print(space + happy_new_year_string_en)
            print(space + happy_new_year_string_ch)
            print(space)

        elif i % 9 == 0:
            print(space + "🪅")
        elif i % 5 == 0:
            print(space + "🎈")
        elif i % 8 == 0:
            print(space + "🎈")
        elif i % 7 == 0:
            print(space + "🍁")
        elif i % 6 == 0:
            print(space + "❤️")
        elif i % 2 == 0:
            print(space + "📢" + " " + phrase)
        else:
            print(space + "🔸")

        space = ""
        time.sleep(0.6)


print("Bonjour ! Veuillez Taper « 1 », puis Entrée")

while True:
    user_input = input("> ")
    if user_input == "1":
        happy_new_year()
        break
    else:
        print("Vous n'avez pas tapé « 1 ». Veuillez réessayer.")
        continue

# Code modified by me:
# Source Code: <https://replit.com/@elisencode/Happy-New-Year-Python-Code>
# [Youtube Happy New Year Python Code]<https://www.youtube.com/watch?v=EUAYQ82uRWU>
# Thank you for phil's contribution.

# Inspired from:
# PySeek: <https://www.youtube.com/watch?v=5qUKjBxAZKA>
# Source Code: <https://pyseek.com/2021/01/happy-new-year-2024-in-python/>

# [How to Calculate Reading Time](https://infusion.media/content-marketing/how-to-calculate-reading-time/)
# [Handle line breaks (newlines) in strings in Python](https://note.nkmk.me/en/python-string-line-break/)
# [Four Leaf Clover](https://emojipedia.org/four-leaf-clover)
# [Smiling Face with Smiling Eyes](https://emojipedia.org/smiling-face-with-smiling-eyes)
# [Haut-Parleur](https://emojipedia.org/fr/haut-parleur)
