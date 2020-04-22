import random

histo = [0, 0, 0, 0, 0, 0, 0, 0, 0]
neighbor =  [[1, 3, 0, 0], [2, 4, 0, 1], [2, 5, 1, 2],
             [4, 6, 3, 0], [5, 7, 3, 1], [5, 8, 4, 2],
             [7, 6, 6, 3], [8, 7, 6, 4], [8, 8, 7, 5]]
weight = [3.0, 0.5, 1.0, 0.5, 1.0, 0.5, 2.0, 0.5, 1.0] 
# it doent depend on the transition probability
# only the probability at the position matters
# I remember Baschnagel saying this

pos = 8
n_iter = 1000000
for iter in range(n_iter):
    new_pos = neighbor[pos][random.randint(0, 3)]
    if random.random() < weight[new_pos] / weight[pos]: 
    	# metropolis criterion satisfied
        pos = new_pos # update to new position
    histo[pos] += 1 # reached pos count

norm = sum(weight)
print ('comparison:  weight, histogram')
for k in range(9): 
    print ('site: ', k,' weight: ', weight[k], ' histo: ', norm * histo[k] / float(n_iter))
