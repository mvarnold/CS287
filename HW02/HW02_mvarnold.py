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

def error_set(global_errors):
    error_set = set()
    for key, value in global_errors.items():
        for error in value:
            error_set.add(error)
    print(error_set)

def wilson_lower_confidence(num, pos, z=1.96):
    """`num` samples, `pos` of which are positive = true = 1. The rest
    are negative = false = 0. `z` is the normal proportion for confidence
    interval, default z = 1.96 (95%)
    """
    n = num
    if n == 0:
        return 0

    p = pos / n  # observed rate p
    return (p + z*z/(2*n) - z*np.sqrt((p*(1-p) + z**2/(4*n))/n)) / (1 + z**2/n)
# [Organize code related to problems in the corresponding sections delineated
# below (if code is required). Place code specific to a (sub)problem BELOW that
# problem's header. Please do not delete header comments]

############## Problem 1 ##############

#### P1.1 ####

#### P1.2 ####

#### P1.3 ####

global_errors = {}
files = glob.glob("reports/*")
for file in files:
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
print(error_set(global_errors))


for center_id, error_dict in global_errors.items():
    if 'A/C' in error_dict:
        global_errors[center_id]["HVAC"] = error_dict['A/C']
        global_errors[center_id].pop("A/C")
    if "Air Con." in error_dict:
        global_errors[center_id]["HVAC"] = error_dict["Air Con."]
        global_errors[center_id].pop("Air Con.")
print(error_set(global_errors))
#### P1.6 ####



############## Problem 2 ##############

#### P2.1 ####

total_errors = {}
for center_id, error_dict in global_errors.items():
    total_errors[center_id] = 0
    for error in error_dict.values():
        total_errors[center_id] += error

sorted_errors = sorted(total_errors.items(), key=lambda kv: kv[1], reverse=True)
sorted_error_list = list(zip(*sorted_errors))  

plt.semilogy(sorted_error_list[1],'o',ms=3)
plt.xlabel("Total Error Rank")
plt.ylabel("# Errors")
plt.title("Data Centers ranked by Total Errors")
plt.show()
#### P2.2 ####
print("the mean number of errors per data center was {0:0.2f}".format(np.average(list(total_errors.values()))))
print("the median number of errors per data center was {}".format(np.median(list(total_errors.values()))))

#### P2.3 ####

error_types_count = {} 
for center_id, error_dict in global_errors.items():
    for error,count in error_dict.items():
        if error in error_types_count:
            error_types_count[error] += count
        else:
            error_types_count[error] = count

plt.bar(error_types_count.keys(), error_types_count.values())
plt.xticks(rotation='90')
plt.tight_layout()
plt.show()

#### P2.4 ####



############## Problem 3 ##############

#### P3.1 ####

flooding_dict = {}
for center_id, erryyor_dict in global_errors.items():
    for 

#### P3.2 ####

#### P3.2 Bonus ####

#### P3.3 Bonus ####






