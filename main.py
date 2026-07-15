from secrets import choice


def input_name_user() -> str:
    """fonction servant à demander à l'utilisateur de mettre un nom"""
    return input("entrez votre nom")


def input_number_matches_user() -> int:
    """demander à l'utilisateur de dire combien d'allumette il enlève"""
    number = None
    while number is None:
        number = input("Veuillez indiquer le nombre d'allumette que vous prenez entre 1 et 4\n")
        if number == "1" or number == "2" or number == "3" or number == "4":
            number =int(number)
        else:
            number = None
    return number


def input_number_user() -> int:
    """permet de savoir combien de joueurs il aura"""
    number = None
    while number is None:
        number = input("Veuillez indiquer le nombre de joueurs (1 ou 2)\n")
        if number == "1" or number == "2":
            number =int(number)
        else:
            number = None
    return number

def game():
    """fonction permettant de créé le jeu"""
    number_user = input_number_user()
    liste_user = []
    for _ in range(number_user):
        liste_user.append(input_name_user())
    matches = " "*21
    if number_user == 1:
        liste_user.append("\n")
    user = choice(liste_user)
    i = 0
    winner = None
    while len(matches) > 0:
        if user != "\n":
            print(f"{user} , c'est à vous de jouer")
        else:
            print("Ordinateur, c'est à vous de jouer")
        print(f"il reste {len(matches)} allumettes")
        if user != "\n":
            number_matches = input_number_matches_user()
        else:
            
        if len(matches) >= number_matches:
            allumette = allumette[number_matches:]
            i +=1
        user = liste_user[i % 2]
    winner = liste_user[i  % 2]
    if winner == "\n":
        winner = "Ordinateur"
    print(f"{winner} est le grand vainqueur.")
    

def main() -> None :
   "fonction principale si on éxécute le code"
   game()
   print("Merci d'avoir jouer")


if __name__ == '__main__':
    main()
