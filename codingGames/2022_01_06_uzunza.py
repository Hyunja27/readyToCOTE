# =======================================================================================================================
# =======================================================================================================================
# [Q]

# A small portion of our genes are not found in the nucleus of our cells but in the mitochondria.
# This mitochondrial DNA is inherited almost exclusively on the maternal branch,
# so we inherit it from our mother, maternal grandmother, and so on.

# You are processing data for a genetic research institute and
# you are given a list of name, mother's name pairs extracted from birth certificates and
# your task is to list all the descendants of a given person who definitely have the same mitochondrial DNA.
# (The possibility of mutation is ignored.)
# Input
# 1st line: a string which is the name of the person whose appropriate descendants should be listed
# 2nd line: N number of birth certificate data
# next N lines: two, space separated unique strings, the first one is the name, the second is the mother's name
# Output
# Nobody if there is no appropriate descendant or
# K lines: string, the name of the appropriate descendant, in lexical order
# Constraints
# 1 <= K < N <= 1000

# All names are unique.

# Neither name, nor mother's name contains space.

# The length of each name < 100
# Example
# Input
# Emese
# 5
# Lelle Emese
# Bibor Lelle
# Csilla Emese
# Piros Bibor
# Arany Lelle
# Output
# Arany
# Bibor
# Csilla
# Lelle
# Piros

# =======================================================================================================================
# =======================================================================================================================
# [mine]



# import sys
# import math

# # Auto-generated code below aims at helping you parse
# # the standard input according to the problem statement.

# c = []
# c.append(input())
# n = int(input())
# for i in range(n):
#     n, m = input().split()
#     if m in c:
#         c.append(n)
# c.remove(c[0])
# c.sort()
# if len(c) != 0:
#     for i in c:
#         print(i)
# else:
#     print("Nobody")


# # Write an answer using print
# # To debug: print("Debug messages...", file=sys.stderr, flush=True)