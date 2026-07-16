from secrets import choice


def input_name_user() -> str:
    """fonction servant à demander à l'utilisateur de mettre un nom"""
    return input("entrez votre nom")


def input_numberheapmatches_user() -> int:
    """demander à l'utilisateur de dire quel tas d'allumette il va utiliser"""
    number = None
    while number is None:
        number = input("Veuillez indiquer le tas que vous allez prendre entre 1 et 4\n")
        if number == "1" or number == "2" or number == "3" or number == "4":
            number =int(number) - 1
        else:
            number = None
    return number


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


def choice_computer_matches(number_matches: int) -> int:
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


def game_setup() -> None:
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
    if game_choice == "nime":
       game_nime(liste_user, i ,  user)
    else:
        game_variation(liste_user, i , user)


def choice_computer_heap_matches(list_heap_matches:list[str]) -> int :
    heap_matches = [heap for heap in list_heap_matches if len(heap)> 1]
    if len(heap_matches) > 1:
        heap = list_heap_matches.index(choice(heap_matches))
    elif len(heap_matches) == 1:
        heap = list_heap_matches.index(heap_matches[0])
    else:
        heap = 0
    return heap


def game_nime(liste_user : list[str], i: int,user: str) -> None:
    """fonction permettant de créé le jeu de nime"""
    matches = " "*21
    while len(matches) > 0:
        print(f"il reste {len(matches)} allumettes")
        if user != "\n":
            print(f"{user} , c'est à vous de jouer")
            number_matches = input_number_matches_user()
        else:
            print("Ordinateur, c'est à vous de jouer")
            number_matches = choice_computer_matches(len(matches))
        if len(matches) >= number_matches:
            matches = matches[number_matches:]
            i +=1
        user = liste_user[i % 2]
    winner(liste_user[i  % 2])


def game_variation(liste_user : list[str], i: int ,user: str) -> None:
    """fonction permettant de créé le jeu de Marienbad"""
    list_matches = [" ", " " * 3, " " * 5, " " * 7]
    while any([len(i) >0 for i in list_matches]):
        for i in range(1,5):
            print(f" le tas numéro  {i} a {len(list_matches[i - 1])}")
        if user != "\n":
            print(f"{user} , c'est à vous de jouer")
            heap_matches = input_numberheapmatches_user()
            number_matches = input_number_matches_user()
        else:
            print("Ordinateur, c'est à vous de jouer")
            heap_matches = choice_computer_heap_matches(list_matches)
            number_matches = choice_computer_matches(len(list_matches[heap_matches]))
        if len(list_matches[heap_matches]) >= number_matches:
            list_matches[heap_matches] = list_matches[heap_matches][number_matches:]
            i +=1
        user = liste_user[i % 2]
    winner(liste_user[i  % 2])


def winner(winner:str) -> None:
    if winner == "\n":
        winner = "Ordinateur"
    print(f"{winner} est le grand vainqueur.")
    

def main() -> None :
   "fonction principale si on éxécute le code"
   game_setup()
   print("Merci d'avoir jouer")


if __name__ == '__main__':
    main()
