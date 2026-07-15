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


def choice_computer(number_matches: int) -> int:
    """choix de l'ordinateur"""
    if number_matches % 5 != 1:
        number = 5 - number_matches % 5
    else:
        number = choice(list(range(1, min(5, number_matches + 1))))
    return number


def choice_game_user() -> str:
    """permet de savoir quel jeu ce sera"""
    game = None
    while game is None:
        game = input("Veuillez indiquer le jeu (nime ou Marienbad\n")
        if game != "nime" or game !="Marienbad" :
            game = None
            
    return game


def preparation() -> None:
    """prépare les variables ainsi que les configurations si c'est pour jouer contre l'ordi ou pas"""
    game_choice = choice_game_user()
    number_user = input_number_user()
    liste_user = []
    for _ in range(number_user):
        liste_user.append(input_name_user())
    if number_user == 1:
        liste_user.append("\n")
    user = choice(liste_user)
    i = liste_user.index(user)
    winner = None
    if game_choice == "nime":
       game_nime(liste_user, i , winner, user)
    else:



def game_nime(liste_user : list[str], i: int,  winner : None|str ,user: str) -> None:
    """fonction permettant de créé le jeu"""
    matches = " "*21
    while len(matches) > 0:
        if user != "\n":
            print(f"{user} , c'est à vous de jouer")
        else:
            print("Ordinateur, c'est à vous de jouer")
        print(f"il reste {len(matches)} allumettes")
        if user != "\n":
            number_matches = input_number_matches_user()
        else:
            number_matches = choice_computer(len(matches))
        if len(matches) >= number_matches:
            matches = matches[number_matches:]
            i +=1
        user = liste_user[i % 2]
    winner = liste_user[i  % 2]
    if winner == "\n":
        winner = "Ordinateur"
    print(f"{winner} est le grand vainqueur.")
    

def main() -> None :
   "fonction principale si on éxécute le code"
   preparation()
   print("Merci d'avoir jouer")


if __name__ == '__main__':
    main()
