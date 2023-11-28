import math


def je_li_kodna_rijec(checked_string: str) -> bool:
    """Provjerava je li zadani string kodna rjijec u bazi 2

    Argumenti:
        checked_string {str} -- string koji se provjerava

    Vraca:
        boolean -- je li string valjana kodna rijec
    """
    for checked_character in checked_string:
        if checked_character != "0" and checked_character != "1":
            return False

    return True

def broj_kodnih_rijeci(code_word_list: list) -> int:
    """Vraca broj kodnih rijeci blok koda K -> M

    Argumenti:
        code_word_list {list} -- lista kodnih rijeci koju se analizira

    Vraca:
        int -- broj kodnih rijeci
    """
    return len(code_word_list)


def duljina_kodnih_rijeci(code_word: str) -> int:
    """Vraca duljinu kodnih rijeci u blok kodu K -> n

    Argumenti:
        code_word {str} -- analizirana kodna rijec

    Vraca:
        int -- duljina kodnih rijeci
    """
    return len(code_word)




def informacijski_bitovi(number_of_code_words: int) -> int:
    """Vraca broj informacijskih bitova kodnih rijeci u kodu K -> k

    Argumenti:
        number_of_code_words {int} -- M (broj kodnih rijeci koda K)

    Vraca:
        int -- broj informacijskih bitova kodnih rijeci
    """
    return int(math.log2(number_of_code_words))


def udaljenost(code_word1: str, code_word2: str) -> int:
    """Vraca broj razlicitih bitova izmedu 2 kodne rijeci

        Argumenti:
            code_word1 {str} -- kodna rijec 1
            code_word2 {str} -- kodna rijec 2

        Vraca:
            int -- broj razlicitih bitova
    """
    code_distance = 0
    for i in range(len(code_word1)):
        if code_word1[i] != code_word2[i]:
            code_distance += 1

    return code_distance


def min_udaljenost(code_word_fixed_length: int, code_word_list: list) -> int:
    """Vraca minimalnu udaljenost -> d(K)

    Argumenti:
        code_word_fixed_length {int} -- n (duljina kodnih rijeci)
        code_word_list {list} -- lista kodnih rijeci koda K

    Vraca:
        int -- minimalna udaljenost
    """
    
    # inicijalno je d postavljen na vrijednost duljine kodne rijeci koda K, smanjuje se ako se nade manja udaljenost
    minimal_code_distance = code_word_fixed_length

    for i in range(len(code_word_list)):
        for j in range(i + 1, len(code_word_list)):
            code_words_distance = udaljenost(code_word_list[i], code_word_list[j])
            if code_words_distance < minimal_code_distance:
                minimal_code_distance = code_words_distance

    return minimal_code_distance




def koef_savrsenosti(code_word_fixed_length: int, maximum_number_of_errors_corrected: int) -> float:
    """Vraca koeficijent savrsenosti za kod K

       Argumenti:
           code_word_fixed_length {int} -- n (duljina kodnih rijeci u kodu K)
           maximum_number_of_errors_corrected {int}  -- t (najveci broj pogresaka koje se mogu ispraviti)

       Vraca:
           float -- koeficijent savrsenosti za kod K
       """
    sum_of_binoms = suma_binoma(code_word_fixed_length, maximum_number_of_errors_corrected)

    return math.pow(2, code_word_fixed_length) / sum_of_binoms



def je_li_savrsen(number_of_code_words: int, code_perfection_coefficent: float) -> bool:
    """Metoda vraca je li kod savrsen s obzirom na koeficijent za savrsenost takvog koda

       Argumenti:
           number_of_code_words {int} -- M (broj kodnih rijeci koda K)
           code_perfection_coefficent {float} -- koeficijent za savresnost koda K

       Vraca:
           bool -- True ako je kod K savrsen
       """
    return number_of_code_words == code_perfection_coefficent



def max_otkriveni(code_word_list_minimal_distance: int) -> int:
    """Vraca najveci broj gresaka koje kod moze otkriti

    Argumenti:
        code_word_list_minimal_distance {int} -- d(K)
        
    Vraca:
        int -- najveci broj pogresaka koje kod moze otkriti
    """
    return code_word_list_minimal_distance - 1



def max_ispravljeni(code_word_list_minimal_distance: int) -> int:
    """Vraca najveci broj gresaka koje kod moze ispraviti

    Argumenti:
        code_word_list_minimal_distance {int} -- d(K)
        
    Vraca:
        int -- najveci broj pogresaka koje kod moze ispraviti
        """
    return int((code_word_list_minimal_distance - 1) / 2.0)



def binom_koef(n: int, r: int) -> int:
    """Racuna binomni koeficijent, nCr
        n! / (r! * (n - r)!)

    Argumenti:
        n {int}
        r {int}

    Vraca:
        int -- binomni koeficijent
    """
    try:
        binom = math.factorial(n) // math.factorial(r) // math.factorial(n - r)
    except ValueError:
        binom = 0
    return binom


def suma_binoma(n: int, t: int) -> int:
    """Vraca sumu binomnih koeficijenata
    suma = C(n, 0) + C(n, 1) + ... + C(n, t)

    C(x, y) je binomni koeficijent
    
    Argumenti:
        n {int}
        t {int}

    Vraca:
        int -- suma binomnih koeficijenata
    """
    sum_of_binoms = 0
    for i in range(t + 1):
        sum_of_binoms += binom_koef(n, i)

    return sum_of_binoms


def sadrzi_nulu(code_word_list: list) -> bool:
    """Provjerava postoji li kodna rijec od iskljucivo znakova 0

    Argumenti:
        code_word_list {list} -- lista kodnih rijeci

    Vraca:
        bool -- je li 0 kodna rijec
    """
    for code_word in code_word_list:
        if "1" not in code_word:
            return True

    return False


def suma(code_word1: str, code_word2: str) -> str:
    """Racuna sumu dvaju kodnih rijeci

    Argumenti:
        code_word1 {str} -- String jedne kodne rijeci
        code_word2 {str} -- String druge kodne rijeci

    Vraca:
        str -- String sumiranih kodnih rijeci
    """
    code_word1_num = int(code_word1, base=2)
    code_word2_num = int(code_word2, base=2)

    
    # bin vraca binarni broj s 0b na pocetku
    # maknu se prvi znakovi i puni se nulama s lijeve strane do zeljene duljine (duljine kodne rijeci)
    
    code_word_sum = bin(code_word1_num ^ code_word2_num)[2:].zfill(len(code_word1))

    return code_word_sum


def provjeri_sumu(code_word_list: list) -> bool:
    """Provjerava sve moguce sume kodnih rijeci i daju li one neku drugu kodnu rijec koda K

    Argumenti:
        code_word_list {list} -- lista kodnih rijeci

    Vraca:
        bool -- vracaju li sve sume kodnu rijec koda K
    """
    for i in range(len(code_word_list)):
        for j in range(i + 1, len(code_word_list)):
            sum_of_code_words = suma(code_word_list[i], code_word_list[j])
            if sum_of_code_words not in code_word_list:
                return False

    return True


def je_li_linearan(code_word_list: list) -> bool:
    """Provjerava je li kod linearan

    Dva uvjeta koja moraju biti zadovoljena:
    1. Suma bilo koje dvije kodne rijeci daju kodnu rijec iz koda K
    2. Postoji kodna rijec koja se sastoji samo od nula
    
    Argumenti:
        code_word_list {list} -- lista kodnih rijeci

    Vraca:
        bool -- je li kod linearan
    """
    return sadrzi_nulu(code_word_list) and provjeri_sumu(code_word_list)


def print_error_nema_rijeci():
    """Ispisuje gresku ako nije upisana nijedna kodna rijec
    """
    print("Nijedna kodna riječ nije upisana. Kraj rada.")


def print_error_krivi_broj():
    """Ispisuje gresku ako broj kodnih rijeci u kodu K nije potencija broja 2
    """
    print("Broj kodnih riječi nije potencija broja 2. Kraj rada.")


def print_kodne_rijeci(code_word_list: list):
    """Ispisuje listu kodnih rijeci
    """
    for code_word in code_word_list:
        print(code_word)


def main():
    print("TINF 20/21, grupa 25, Zadatak 9")
    print("Kodne rijeci upisujte svaku u svom retku.")
    print("Duljina prve kodne rijeci koristit ce se kao zadana duljina za sve ostale.")
    print("Za kraj unosa kodnih rijeci pritisnite tipku enter na prazan redak.")
    print("")
    
    code_word = input()
    code_word_fixed_length = None
    # prazan string - gotov s radom
    if len(code_word) == 0:
        print_error_nema_rijeci()
        return

    code_word_list = []

    while code_word:
        if not je_li_kodna_rijec(code_word):
            print("Kodna rijec sadrzi znakove razlicite od 0 i 1.")
            print("Upisite kodnu rijec ponovo:")
            code_word = input()
            continue

        if code_word_fixed_length is None:
            code_word_fixed_length = duljina_kodnih_rijeci(code_word)

        if len(code_word) != code_word_fixed_length:
            print("Ova kodna rijec ima duljinu razlicitu od prethodnih.")
            print("Upisite kodnu rijec ponovo:")
            code_word = input()
            continue

        if code_word in code_word_list:
            print("Vrijednost koju ste upisali vec postoji kao kodna rijec.")
            print("Upisite kodnu rijec ponovo:")
            code_word = input()
            continue

        code_word_list.append(code_word)
        code_word = input()

    number_of_code_words = broj_kodnih_rijeci(code_word_list)
    if number_of_code_words == 0:
        print_error_nema_rijeci()
        return

    number_of_informational_bits = informacijski_bitovi(number_of_code_words)
    if (number_of_code_words != 2**number_of_informational_bits):
        print_error_krivi_broj()
        return

    print("*************************")
    print("Kod K:")
    print_kodne_rijeci(code_word_list)
    print("*************************")

    print("Analiza koda K:")
    print("Broj kodnih rijeci:")
    print(f"M = {number_of_code_words}")

    print("Duljina kodne rijeci:")
    print(f"n = {code_word_fixed_length}")

    print("Broj informacijskih bitova:")
    print(f"k = {number_of_informational_bits}")

    code_word_list_minimal_distance = min_udaljenost(code_word_fixed_length, code_word_list)
    print("Minimalna udaljenost koda:")
    print(f"d(K) = {code_word_list_minimal_distance}")

    maximum_number_of_errors_discovered = max_otkriveni(code_word_list_minimal_distance)
    print("Broj gresaka koje kod moze otkriti:")
    print(f"s = {maximum_number_of_errors_discovered}")

    maximum_number_of_errors_corrected = max_ispravljeni(code_word_list_minimal_distance)
    print(f"Broj gresaka koje kod moze ispraviti:")
    print(f"t = {maximum_number_of_errors_corrected}")

    print("Vrijedi:")
    print("M <= 2^n / (C(n, 0) + C(n, 1) + ... +C(n, t))")

    print("Kod je perfektan ako vrijedi:")
    print("M = 2^n / (C(n, 0) + C(n, 1) + ... +C(n, t))")

    code_perfection_coefficent = koef_savrsenosti(code_word_fixed_length,
                                                                 maximum_number_of_errors_corrected)

    if je_li_savrsen(number_of_code_words, code_perfection_coefficent):
        print(f"Kod je perfektan: {number_of_code_words} = {code_perfection_coefficent}")
    else:
        print(f"Kod nije perfektan: {number_of_code_words} < {code_perfection_coefficent}")

    if je_li_linearan(code_word_list):
        print("Kod je linearan")
    else:
        print("Kod nije linearan")


if __name__ == '__main__':
    main()
