# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:16:22 2024

@author: Austin
"""


print("=" * 63, end="\n")
print("\t\t\t\t Baseball Team Manager \n")
print("This program calculates the batting average for a player based \non the player's official number of at bats and hits.")
print("=" * 63, end="\n\n")


player_name = input("Player's name: ")
at_bats = int(input("Official number of at bats: "))
number_hits = int(input("Number of hits: "))

batting_average = round(number_hits / at_bats, 3)

print(f"\n{player_name}'s batting average is {batting_average}")
