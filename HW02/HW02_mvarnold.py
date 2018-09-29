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

def check_id(filename):
    """checks that the filename matches the DATACENTER id number"""
    f = open(filename, "r")

    for line in f:
        split_line = line.split()
        if split_line[1] == filename[8:14]:
            return 0
        else:
            print("error")

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
    return ((p + z*z/(2*n) - z*np.sqrt((p*(1-p) + z**2/(4*n))/n)) / (1 + z**2/n),
            (z*z/(2*n) - z*np.sqrt((p*(1-p) + z**2/(4*n))/n)) / (1 + z**2/n))

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
print("the number of data centers loaded is {}".format(len(global_errors)))

#### P1.4 ####

missing_ids = []
for i in range(1431):
    if global_errors[str(i).zfill(6)]:
        continue
    else:
        missing_ids.append(i)
print("the number of missing data centers ids is {}".format(len(missing_ids)))

for file in files:
    check_id(file)

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
plt.savefig("rank_errors.png")
plt.close()
#### P2.2 ####
print("the mean number of errors per data center was {0:0.2f}".format(np.average(list(total_errors.values()))))
print("the median number of errors per data center was {}".format(np.median(list(total_errors.values()))))
print("the mode number of errors per data center was {}".format(scipy.stats.mode(list(total_errors.values()))[0][0]))

#### P2.3 ####

error_types_count = {} 
for center_id, error_dict in global_errors.items():
    for error,count in error_dict.items():
        if error in error_types_count:
            error_types_count[error] += count
        else:
            error_types_count[error] = count

sorted_errors = sorted(error_types_count.items(), key=lambda kv: kv[1], reverse=True)
sorted_error_list = list(zip(*sorted_errors))  

plt.bar(sorted_error_list[0],sorted_error_list[1])
plt.xticks(rotation='90')
plt.tight_layout()
plt.savefig("error_types.png")
plt.close()
print(error_types_count)
#### P2.4 ####



############## Problem 3 ##############

#### P3.1 ####
flood_count = {}
flooding_dict = {}
for center_id, error_dict in global_errors.items():
    flooding_dict[center_id] = error_dict['Physical intrusion (water)']/sum(error_dict.values())
    flood_count[center_id] = error_dict['Physical intrusion (water)']

sorted_errors = sorted(flooding_dict.items(), key=lambda kv: kv[1], reverse=True)
sorted_error_list = list(zip(*sorted_errors))
print("The highest proportion of flooding happens at Data Center {}".format(sorted_error_list[0][0]))

#### P3.2 ####

plt.plot(sorted_error_list[1], '.')
plt.annotate("Data Center {}".format(sorted_error_list[0][0]), (0, sorted_error_list[1][0]), (200, 0.75), arrowprops=dict(facecolor='black', arrowstyle = "->"))
plt.title("rank of flood risk")
plt.xticks(rotation='90')
plt.ylabel("ratio of water errors to total")
plt.tight_layout()
plt.savefig("figures/flood_risk_rank.png")
plt.show()


#### P3.2 Bonus ####

uncertainty = {}
for center_id, error_dict in global_errors.items():
    uncertainty[center_id] = wilson_lower_confidence(total_errors[center_id],
            flood_count[center_id])

data_array = np.zeros((1431,3))
index = 0
for center_id in global_errors.keys():
    data_array[index,0] = center_id
    data_array[index,1] = flooding_dict[center_id]
    data_array[index,2] = uncertainty[center_id][1]
    index += 1

data_array.view("i8,i8,i8").sort(order=['f1'], axis=0)


plt.errorbar([i for i in range(1431)],data_array[:,1][::-1],yerr=data_array[:,2][::-1],marker='.')
plt.annotate("Data Center {}".format(sorted_error_list[0][0]), (0, sorted_error_list[1][0]), (200, 0.75), arrowprops=dict(facecolor='black', arrowstyle = "->"))
plt.title("rank of flood risk")
plt.xticks(rotation='90')
plt.tight_layout()
plt.savefig("figures/flood_risk_rank_uncertainty.png")
plt.show()


data_array = np.zeros((1431,3))
index = 0
for center_id in global_errors.keys():
    data_array[index,0] = center_id
    data_array[index,1] = flooding_dict[center_id]
    data_array[index,2] = uncertainty[center_id][0]
    index += 1

data_array.view("i8,i8,i8").sort(order=['f2'], axis=0)


plt.plot([i for i in range(1431)],data_array[:,2][::-1],'.')
plt.annotate("Data Center {0:0.0f}".format(data_array[:,0][::-1][0]), (0, data_array[:,2][::-1][0]), (200, 0.75), arrowprops=dict(facecolor='black', arrowstyle = "->"))
plt.title("rank of flood risk")
plt.xticks(rotation='90')
plt.tight_layout()
plt.savefig("figures/flood_risk_rank_lowerwilson.png")
plt.show()



#### P3.3 Bonus ####

