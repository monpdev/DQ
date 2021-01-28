population = [0, 3, 6]

samples = [[0,3], [0,6],
           [3,0], [3,6],
           [6,0], [6,3]
          ]

from numpy import var, std

pop_var = var(population, ddof = 0)
pop_std = std(population, ddof = 0)

st_devs = []
variances = []

for sample in samples:
    st_devs.append(std(sample, ddof = 1))
    variances.append(var(sample, ddof = 1))

mean_std = sum(st_devs)/len(st_devs)
mean_var = sum(variances)/len(variances)

equal_stdev = pop_std == mean_std
equal_var = pop_var == mean_var