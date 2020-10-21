population = [3, 7, 2]
samples = [[3,7],[3,2],
           [7,2],[7,3],
           [2,3],[2,7]
          ]

sample_means = []
for sample in samples:
    sample_means.append(sum(sample)/len(sample))

population_mean = sum(population)/len(population)
mean_of_sample_means = sum(sample_means)/len(sample_means)

unbiased = (population_mean == mean_of_sample_means)