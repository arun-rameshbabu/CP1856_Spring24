# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:28:49 2024

@author: Austin
"""

print("BLACKJACK!\nBlackjack Payout is 3:2\n")

starting_money = input("Starting money:\t")
bet_amount = input("Bet amount:\t\t")

blackjack_ratio = float(1.5)

print("\nENDING MONEY FOR A...")
print("Blackjack:\t\t", round(float(starting_money) + float(bet_amount) * blackjack_ratio, 2))
print("Win:\t\t\t\t", round(float(starting_money) + float(bet_amount), 2))
print("Blackjack:\t\t", round(float(starting_money), 2))
print("Blackjack:\t\t", round(float(starting_money) - float(bet_amount), 2))

print("\nBye!")

