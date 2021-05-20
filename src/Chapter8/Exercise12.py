"""
Exercise 12
The following functions are all intended to check whether
a string contains any lowercase letters, but at least some
of them are wrong. For each function, describe what the
function actually does(assuming that the parameter is a string).
"""


def cipher(msg, key):
    # zmienna przechowujaca zaszyfrowana msg
    message = ""

    # przechodzimy przez wszystkie znaki napisu msg
    for x in msg:
        # sprawdzamy czy x jest litera
        if x.isalpha():
            # zamieniamy znak na reprezentacje liczbowa
            number = ord(x)
            # przesuwamy reprezentacje liczbowa znaku o key pozycji
            number += key

            if x.isupper():
                if number > 90:
                    number -= 26
                elif number < 65:
                    number += 26
            else:
                if number > 122:
                    number -= 26
                elif number < 97:
                    number += 26

            # wracamy do reprezentacji znakowej i budujemy zaszyfrowana msg
            message += chr(number)
        else:
            message += x
    return message


print("Twoja zaszyfrowana msg to ")
print(cipher("KAjsi 220 adsfn?", 13))
