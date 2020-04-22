import random

def direct_pi(N,side):
    n_hits = 0 #initial
    radius=side/2.0
    for iter in range(n_trials):
       x, y = random.uniform(-radius, radius), random.uniform(-radius,radius)
       if x**2 + y**2 < radius**2: # if in the circle
           n_hits += 1
    return n_hits/radius**2

n_runs = 1000
side=2
n_trials = 40000
for run in range(n_runs):
    print (side**2  * direct_pi(n_trials,side) / float(n_trials)) # already normed by radius
