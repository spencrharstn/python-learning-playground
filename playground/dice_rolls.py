import statistics
import numpy
from time import time
from collections import OrderedDict
from die import Die

def mean_alt(nums):
    """Given a list of numbers, returns the mean (average)"""
    return float(sum(nums)) / max(len(nums), 1)

def get_mean_time(mean_func, rolls):
    """Given a list of numbers, returns a tuple of the function used, average and time elapsed"""
    t1 = time()
    average = mean_func(rolls)
    t2 = time()
    return t2 - t1

def main():
    """The main function"""

    num_sides = int(input("How many sides on the die? "))
    die1 = Die(num_sides)
    rolls = []
    num_rolls = int(input("How many rolls of the die? "))
    for i in range(1, num_rolls + 1):
        result = die1.roll_die()
        rolls.append(result)
    average = 0

    variations = {}

    variations['mean_alt'] = get_mean_time(mean_alt, rolls)
    variations['statistics.mean'] = get_mean_time(statistics.mean, rolls)
    variations['numpy.mean'] = get_mean_time(numpy.mean, rolls)
    
    sorted_variations = OrderedDict([(k, variations[k]) for k in sorted(variations, key=variations.get)])
    
    print("Variation\t\tTime (in seconds)")
    for variation, time in sorted_variations.items():
        print(variation + "\t\t" + str(time))

if __name__ == '__main__':
    main()