# Homework 04
# Michael Arnold


"""
*** DESCRIBE YOUR CODE ORGANIZATION HERE ***
"""


#################### PLEASE  DO NOT MODIFY CODE HERE #####################
import sys, os, string
import math, random
import csv, json
from collections import Counter
# Please do not use other imports in this homework
##########################################################################



def correlation_coefficient(X,Y):
    """Compute and return (as a float) the Pearson correlation coefficient
    between two lists of numbers X and Y.
    """
    





def load_data(filename):
	"""

	"""
	data = []
	with open(filename) as line:
		data.append(json.load(line.strip()))
	print(data)

def main():
	load_data("data/diabetes_study_rz03__data.txt")





# *** PROBLEM 3 BELOW THIS IMPORT ONLY ***
import matplotlib.pyplot as plt


if __name__ == '__main__':
	main()
