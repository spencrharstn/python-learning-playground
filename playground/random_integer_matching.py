# Finding random integers
# from: https://www.reddit.com/r/learnpython/comments/7jn9qn/i_wrote_this_code_and_i_keep_running_it_and_im/

import random as r
from datetime import datetime
import calendar
#from matplotlib import pyplot as plt

def get_time():
    d = datetime.utcnow()
    unixtime = calendar.timegm(d.utctimetuple())
    unixtimee = datetime.fromtimestamp(unixtime)
    print(unixtimee)

get_time()
maxnum = 10000

def run():
    counter = 0
    while True:
        var1 = r.randint(0,maxnum)
        var2 = r.randint(0,maxnum)

        counter += 1

        if var1 == var2:
            print("Match is: {}".format(var1))
            print("Iterations: {} times.".format(counter))
            get_time()
            return counter

run()
#counts = [run() for _ in range(1000)]
#plt.hist(counts, bins=20)
#plt.show()