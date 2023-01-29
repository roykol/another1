
import os
from arttss import logo
print(logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def caesar(e_direction):

  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if shift > 26:
    shift %= 26
  if e_direction == "encode":
    cipher_text = ""
    for letter in text:
      position = alphabet.index(letter)
      new_position = position + shift
      cipher_text += alphabet[new_position]
    print(f"The {e_direction} text is {cipher_text}")

  elif e_direction == "decode":
    cipher_text = ""
    for letter in text:
      position = alphabet.index(letter)
      new_position = position - shift
      cipher_text += alphabet[new_position]
    print(f"The {e_direction} text is {cipher_text}")

again = False
while not again:
  direc = False
  while not direc:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction != "encode" and direction != "decode":
      print("PLEASE INPUT THE RIGHT ONE!")
    else:
      caesar(e_direction=direction)
      direc = True

  ask = input("Do you want to start again?'yes'or 'no': ").lower()
  if ask == "no":
    again = True
    print("GOODBYE!")


os.system('cls')
