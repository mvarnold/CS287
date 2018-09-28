# Homework 02
# Michael Arnold

# allowed imports only (you may not need all of these):
import sys, os
import glob
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
# no other imports please!


############## Functions ##############

def load_report(filename):
    """Loads reports from reports directory"""
    f = open(filename, 'r')

    errors = {}
    for line in f:
        split_line = line.split(":")
        if len(split_line) > 1:
            try:
                value = int(split_line[1])
                errors[split_line[0]] = value
            except ValueError:
                pass

    return errors

# [Define any of your other functions here, replacing this code comment]

############ End Functions ############



# [Organize code related to problems in the corresponding sections delineated
# below (if code is required). Place code specific to a (sub)problem BELOW that
# problem's header. Please do not delete header comments]

############## Problem 1 ##############

#### P1.1 ####

#### P1.2 ####

#### P1.3 ####

global_errors = {}
files = glob.glob("reports/*")
for i, file in enumerate(files):
    errors = load_report(file)
    global_errors[file[8:14]] = errors

#### P1.4 ####
missing_ids = []
for i in range(1431):
    if global_errors[str(i).zfill(6)]:
        continue
    else:
        missing_ids.append(i)
print(missing_ids)
#### P1.5 ####

error_set = set()
for key, value in global_errors.items():
    for error in value:
        error_set.add(error)
print(error_set)
print(len(error_set))

#### P1.6 ####



############## Problem 2 ##############

#### P2.1 ####

#### P2.2 ####

#### P2.3 ####

#### P2.4 ####



############## Problem 3 ##############

#### P3.1 ####

#### P3.2 ####

#### P3.2 Bonus ####

#### P3.3 Bonus ####






