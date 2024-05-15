# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:45:46 2024

@author: Austin
"""
print("SALES DATA IMPORTER")

print("\nEnter sales data\n")


total_sales = 0

amount =float(input("Amount:\t\t\t"))
year = int(input("Yeah:\t\t\t"))
month = int(input("Month (1-12):\t"))
day = int(input("Day (1-31):\t\t"))
total_sales = total_sales + amount
print(f"\n1.\t\t\t\t{year}-{month}-{day}\t\t\t\t ${amount:.2f}\n")

amount =float(input("Amount:\t\t\t"))
year = int(input("Yeah:\t\t\t"))
month = int(input("Month (1-12):\t"))
day = int(input("Day (1-31):\t\t"))
total_sales = total_sales + amount
print(f"\n2.\t\t\t\t{year}-{month}-{day}\t\t\t\t ${amount:.2f}\n")

amount =float(input("Amount:\t\t\t"))
year = int(input("Yeah:\t\t\t"))
month = int(input("Month (1-12):\t"))
day = int(input("Day (1-31):\t\t"))
total_sales = total_sales + amount
print(f"\n3.\t\t\t\t{year}-{month}-{day}\t\t\t\t ${amount:.2f}n")


print("\nTotal Sales\n----------")
print(f"${total_sales}")

print("\nBye!")







