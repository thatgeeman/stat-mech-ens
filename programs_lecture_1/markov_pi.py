import random

x, y = 1.0, 1.0
delta = 0.1 # max delta range so that it 
			# doesnt go out always
n_trials = 4000
n_hits = 0
for i in range(n_trials):
    del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
    if abs(x + del_x) < 1.0 and abs(y + del_y) < 1.0:
        x, y = x + del_x, y + del_y # update x,y
    if x**2 + y**2 < 1.0: n_hits += 1 # check if in circle, if yes count
print (4.0 * n_hits / float(n_trials))
