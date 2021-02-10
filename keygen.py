# This program generates keys for a crackme I recently solved.
# How does it work? The algorithm it used added all of the ASCII values of letters
# in a key, and if the sum was correct then the key was verified, giving the user access.
import random

ascii_value = 1091 # Set the ascii sum here.
keyCount = 0
keyCountMax = 20 # Set the amount of keys you want displayed here.

while keyCount < keyCountMax:
    ascii_sum = 0
    key_string = ""
    while ascii_sum <= ascii_value:
        choice = random.choice("-0123456789=ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz")
        ascii_sum += ord(choice)
        key_string += choice
        if ascii_sum == 1091:
            keyCount += 1
            print("Valid Key found : ", key_string)