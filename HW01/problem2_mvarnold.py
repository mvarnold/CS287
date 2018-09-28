# STAT/CS 287
# HW 01
#
# Name: Michael Arnold
# Date: 09-11-18

import random

def coin_flip(p):
    """takes a probability p and returns heads with probability p or tails
    with probability 1-p"""
    coin = random.random()
    if coin < p:
        return "H"
    else:
        return "T"

def coin_test(p):
    """runs statistics on a coin of probablity p"""
    coin_history = []
    for i in range(1000):
        coin_history.append(coin_flip(p))
   
    # build run history
    run = 0
    run_history = []
    for flip in coin_history:
        if flip == "H":
            run += 1
        else:
            if run > 0:
                run_history.append(run)
                run = 0
    if run > 0:
        run_history.append(run)

    # tally runs of length n
    run_statistics = {i+1:0 for i in range(100)}
    for run in run_history:
        run_statistics[run]+=1 
    
    return run_statistics

def main():
    # runs coin test for each probability of heads
    runs = ["run0.2","run0.4","run0.6","run0.8"]
    for i,p in enumerate([0.2,0.4,0.6,0.8]):
        runs[i]= coin_test(p)

    # print statements
    print("# runs".ljust(5),'0.2'.rjust(4),'0.4'.rjust(4),'0.6'.rjust(4),'0.8'.rjust(4))
    print("length")
    print("-"*30)
    for i in range(1,11):
        print(str(i).ljust(5),end='')
        for j in range(4):
            print(str(runs[j][i]).rjust(5),end="")

        print()

    # make average row
    print("ave".ljust(5),end='')
    for j in range(4):
        index = 0
        run_sum = 0
        for length,number in runs[j].items():
            run_sum += number*length
            index += 1
        print(str(run_sum/index).rjust(5),end="")
    print()
if __name__ == "__main__":
    main()
