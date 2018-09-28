# STAT/CS 287
# HW 01
#
# Name: Michael Arnold
# Date: 09-11-18


def similarity(A, B):
    """computes the similarity between two sets A and B"""
    return len(A.intersection(B)) / len(A.union(B))

set1 = {i for i in range(10)}
set2 = {i for i in range(20) if i % 2 == 0}
set3 = {i for i in range(30) if i % 3 == 1}

sets = [set1, set2, set3]
for i,set in enumerate(sets):
    print("set "+str(i)+" is "+ str(set))

print("The similarity of set1 and set2 is ", format(similarity(set1, set2), '.3f'))
print("The similarity of set2 and set3 is ", format(similarity(set3, set2), '.3f'))
print("The similarity of set1 and set3 is ", format(similarity(set1, set3), '.3f'))
