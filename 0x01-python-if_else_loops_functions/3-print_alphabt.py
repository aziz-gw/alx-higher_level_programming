#!/usr/bin/python3

for ascii_alpha_lower in range(97, 123):
    if chr(ascii_alpha_lower) not in "qe":
        print("{}".format(chr(ascii_alpha_lower)), end="")
