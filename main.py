def input_name_user() -> str:
    return input("entrez votre nom")


def input_number_user() -> int:
    number = None
    while number is None:
        number = input("Veuillez indiquer le nombre d'allumette que vous prenez entre 1 et 4\n")
        if number == "1" or number == "2" or number == "3" or number == "4":
            number =int(number)
        else:
            number = None
    return number