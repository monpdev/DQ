from numpy.random import randint, seed
equal_distances = 0

for i in range(5000):
    seed(i)
    distribution = randint(0,1000,10)
    mean = sum(distribution)/len(distribution)
    
    above = []
    below = []
    for value in distribution:
        if value == mean:
            continue
        if value < mean:
            below.append(mean - value)
        if value > mean:
            above.append(value - mean)
    
    sum_above = round(sum(above),1)
    sum_below = round(sum(below),1)
    if(sum_above == sum_below):
        equal_distances += 1
