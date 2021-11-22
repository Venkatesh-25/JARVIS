# import string
# k = string.ascii_uppercase
# print(k)
import random
import sys
from jarvis import speak

salpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
balpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
basic_symbols = ['+', '-', '*', '/']
medium_symbols = ['@', '!', '#', '%']
advance_symbols = ['?', ':', ';', '&', '$', '_']


def password():
    
    
    sa1 = random.choice(salpha)
    ba1 = random.choice(balpha)

    sa2 = random.choice(nums)
    ba2 = random.choice(salpha)

    sa3 = random.choice(balpha)
    ba3 = random.choice(nums)

    sa4 = random.choice(salpha)
    ba4 = random.choice(balpha)

    bsymbol1 = random.choice(basic_symbols)
    bsymbol2 = random.choice(basic_symbols)
    bsymbol3 = random.choice(basic_symbols)

    poipoi = sa1+ba3+bsymbol1+sa4+ba2+ba1+bsymbol3+sa1+bsymbol2+ba4+sa2+ba3

    print(poipoi)
    speak(poipoi)
