# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:29:31 2024

@author: shang
"""

print("Change Calculator")

choice = 'y'

while choice.lower() == 'y':
    # Test input
    cents = int(input("\nEnter number of cents (0-99): "))
    if (cents < 0) or (cents > 99):
        print("Please enter a number between 0-99.")
        continue
    else:
        # Calculation
        q = cents // 25
        d = (cents % 25) // 10
        n = (cents % 25 % 10) // 5
        p = (cents % 25 % 10 % 5) // 1
        print(f"\nQuarters:\t{q}")
        print(f"Dimes:\t\t{d}")
        print(f"Nickels:\t{n}")
        print(f"Pennies:\t{p}\n")

        choice = input("Continue? (y/n): ")
print("\nBye!")
