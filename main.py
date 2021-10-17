def sorted_asc (l):
    '''
    verifica daca elementele unei liste sunt ordonate crescator
    :param l: o lista de nr intregi
    :return: True, daca nr din lista sunt ordonate crescator sau False, in caz contrar
    '''

    for i in range(1, len(l)):
        if l[i]<l[i-1]:
            return False
    return True

def test_sorted_asc ():
    assert sorted_asc ([1, 2, 3, 4, 5]) is True
    assert sorted_asc ([3, 2, 4, 5]) is False
    assert sorted_asc ([1, 10, 9, 11, 12]) is False
    assert sorted_asc ([11, 15, 20, 9]) is False
    assert sorted_asc ([15, 21, 30, 37]) is True

def get_longest_sorted_asc(l):
    '''
    determina cea mai lunga secventa de numere ordonate crescator dintr-o lista
    :param l: o lista de nr intregi
    :return: cea mai lunga secventa de numere ordonate crescator dintr-o lista
    '''
    subsecventaMax = []
    for i in range (len(l)):
        for j in range (i, len(l)):
            if sorted_asc(l[i:j+1]) and len(l[i:j+1]) > len(subsecventaMax):
                subsecventaMax = l[i:j+1]
    return subsecventaMax

def test_get_longest_sorted_asc():
    assert get_longest_sorted_asc([1, 19, 15, 14, 2, 3, 9, 7]) == [2, 3, 9]
    assert get_longest_sorted_asc ([9, 8, 7, 6]) == [9]
    assert get_longest_sorted_asc ([1, 13, 12, 15, 16, 20, 21]) == [12, 15, 16, 20, 21]
    assert get_longest_sorted_asc ([11, 22, 22, 20, 9]) == [11, 22, 22]

def div_count (n):
    '''
    determina nr de divizori ai un nr
    :param n: nr intreg
    :return: nr de divizori ai unui
    '''
    div = 1
    c = 0
    while div*div<=n:
        if n%div==0 and div*div<n:
            c = c + 2 #si div, si n/div sunt divizori, iar n!=n/div
        elif n%div==0:
            c = c + 1
        div = div + 1
    return c

def test_div_count():
    assert div_count (2) == 2
    assert div_count (27) == 4
    assert div_count (25) == 3
    assert div_count (36) == 9
    assert div_count (1001) == 8
    assert div_count (35) == 4
    assert div_count (196) == 9

def same_div_count (l):
    '''
    verifica daca elem unei liste au ac nr de divizori
    :param l: o lista de nr intregi
    :return: True, daca toate elementele au ac nr de divizori si False, in caz contrar
    '''
    c = div_count(l[0])
    for x in l:
        if div_count(x) != c:
            return False
    return True

def test_same_div_count ():
    assert same_div_count ([6, 27, 35, 125]) is True
    assert same_div_count ([36, 100, 196]) is True
    assert same_div_count ([2, 25, 10]) is False

def get_longest_same_div_count (l):
    '''
    gaseste cea mai lunga subsecventa de elem care au ac nr de divizori a unei liste
    :param l: o lista de nr intregi
    :return: cea mai lunga subsecventa de elem care au ac nr de divizori a unei liste
    '''
    subsecventaMax = []
    for i in range (len(l)):
        for j in range (i, len(l)):
            if same_div_count (l[i:j+1]) and len(l[i:j+1]) > len(subsecventaMax):
                subsecventaMax = l[i:j+1]
    return subsecventaMax

def test_get_longest_same_div_count ():
    assert get_longest_same_div_count([1, 3, 6, 27, 35, 125, 36, 100, 196, 2]) == [6, 27, 35, 125]
    assert get_longest_same_div_count ([3, 5, 7, 4, 9, 25, 121]) == [4, 9, 25, 121]

def prime_digit_number (n):
    '''
    determina daca un numar are sau nu toate cifrele prime
    :param n: nr natural
    :return: True, daca toate cifrele numarului sunt prime si False, in caz contrar
    '''
    while n>0:
        cif = n%10
        if not (cif==2 or cif==3 or cif==5 or cif==7):
            return False
        n=n//10
    return True

def test_prime_digit_number ():
    assert prime_digit_number (237) is True
    assert prime_digit_number (1115) is False
    assert prime_digit_number (2) is True
    assert prime_digit_number (7893) is False
    assert prime_digit_number (573) is True

def prime_digits (l):
    '''
    determina daca toate elementele unei liste au sau nu cifrele prime
    :param l: lista de nr intregi
    :return: True, daca toate elementele au cifrele prime si False, in caz contrar
    '''
    for x in l:
        if not (prime_digit_number(x)):
            return False
    return True

def test_prime_digits ():
    assert prime_digits ([237, 1115]) is False
    assert prime_digits ([2, 237, 7753]) is True
    assert prime_digits ([23, 37, 55]) is True
    assert prime_digits ([36, 974, 225]) is False

def get_longest_prime_digits (l):
    '''
    determina cea mai lunga secventa de elemente cu cifre prime a unei liste
    :param l: lista de nr intregi
    :return: cea mai lunga secventa de elemente cu cifre prime a unei liste
    '''
    subsecventaMax = []
    for i in range (len(l)):
        for j in range (i, len(l)):
            if prime_digits (l[i:j+1]) and len(l[i:j+1]) > len(subsecventaMax):
                subsecventaMax = l[i:j+1]
    return subsecventaMax

def test_get_longest_prime_digits ():
    assert get_longest_prime_digits([1, 33, 56, 77, 23, 253, 8, 73, 25]) == [77, 23, 253]
    assert get_longest_prime_digits([12, 44, 67, 21]) == []
    assert get_longest_prime_digits ([257, 22273, 22]) == [257, 22273, 22]
    assert get_longest_prime_digits ([1, 2, 3, 4, 5, 6, 7, 77, 53]) == [7, 77, 53]

def printMenu ():
    print ("1. Citire lista")
    print ("2. Afisare cea mai lunga subsecventa de nr. ordonate crescator ")
    print ("3. Afisare cea mai lunga subsecventa ale carei elemente au acelasi nr de divizori")
    print ("4. Afisarea cea mai lunga subsecventa ale carei elemente au toate cifrele prime")
    print ("x. Iesire")

def main():
    test_sorted_asc()
    test_get_longest_sorted_asc()
    test_div_count()
    test_same_div_count()
    test_get_longest_same_div_count()
    test_prime_digit_number()
    test_prime_digits()
    test_get_longest_prime_digits()
    l = []
    while True:
        printMenu()
        optiune = input ("Dati optiunea: ")
        if optiune=="1":
            givenString = input("Dati lista, cu elemente separate prin virgula: ")
            numbersAsString = givenString.split(",")
            for x in numbersAsString:
                l.append(int(x))
        elif optiune == "2":
            print(get_longest_sorted_asc(l))
        elif optiune == "3":
            print(get_longest_same_div_count(l))
        elif optiune == "4":
            print(get_longest_prime_digits(l))
        elif optiune == "x":
            break
        else:
            print ("Optiune gresita. Reincercati!")

main()