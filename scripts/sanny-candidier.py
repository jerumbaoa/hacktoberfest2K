from random import *

def hello_gwapo(n):
    """print gwapo "Name"
    """
    if n >= 0 and n <= 84:
        print("dudz")
    elif n >= 85 and n <=89:
        print("tobi")
    elif n >= 90 and n <=92:
        print("sanny")
    elif n >= 93 and n <=96:
        print("thorjack")
    else:
        print("gaara")

randon_int = randint(0, 100)
hello_gwapo(randon_int)
