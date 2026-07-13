def input_name_user() -> str:
    """fonction servant à demander à l'utilisateur de mettre un nom"""
    return input("entrez votre nom")


def input_number_user() -> int:
    """demander à l'utilisateur de dire combien d'allumette il enlève"""
    number = None
    while number is None:
        number = input("Veuillez indiquer le nombre d'allumette que vous prenez entre 1 et 4\n")
        if number == "1" or number == "2" or number == "3" or number == "4":
            number =int(number)
        else:
            number = None
    return number


def game():
    """fonction permettant de créé le jeu"""
    number_user = 2
    liste_user = []
    for _ in range(number_user):
        liste_user.append(input_name_user())
    allumette = " "*21
    user = liste_user[0]
    while len(allumette) > 1:
        print(f"{user} , c'est à vous de jouer")
        print(f"il reste {len(allumette)} allumettes")
        number_allumette = input_number_user()
        if len(allumette) > number_user:
            allumette = allumette[number_allumette:]
        else:
            print(f"{user} vous avez perdu")
            allumette = ""


def main() -> None :
   "fonction principale si on éxécute le code"
   game()
   print("Merci d'avoir jouer")


if __name__ == '__main__':
    main()
    