import random

n_trials = 4000000
n_hits = 0 #initial
side=4.0
radius=side/2

for iter in range(n_trials):
    x, y = random.uniform(-radius, radius), random.uniform(-radius,radius)
    if x**2 + y**2 < radius**2: # if in the circle
        n_hits += 1
print(side**2 * (n_hits / float(n_trials))/radius**2)
