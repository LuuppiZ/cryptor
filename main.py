#!/bin/python
import argparse
from itertools import cycle

parser = argparse.ArgumentParser(
    description="Caecar cipher decryptor, can also be used to encrypt."
)
parser.add_argument(
    "-t", 
    "-text", 
    help="Text you want to encrypt or decrypt.", 
    required=True, 
    type=str
)
parser.add_argument(
    "-s",
    "-shift",
    help="The ammount of times you want to shift letters.",
    type=int,
    default=0,
)
parser.add_argument(
    "-r",
    "-range",
    help="Range of letters you want to test. (min,max)",
    type=str,
    default="1",
)

args = parser.parse_args()
user_text = args.t
user_shift = args.s
user_range = args.r


def decrypt_caesar_cipher(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord("a") if char.islower() else ord("A")
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char
    return decrypted_text


if user_shift:
    possible_decryptions = decrypt_caesar_cipher(user_text, user_shift)
    print(possible_decryptions)
else:
    user_range = user_range.split(",")
    user_range[0] = int(user_range[0])
    user_range[1] = int(user_range[1])

    possible_decryptions = {
        shift: decrypt_caesar_cipher(user_text, shift)
        for shift in range(user_range[0], user_range[1] + 1)
    }
    [print(f"{key}: {value}") for key, value in possible_decryptions.items()]
