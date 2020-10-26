def weighted_mean(distribution, weights):
    weighted_sum = []
    for mean, weight in zip(distribution, weights):
        weighted_sum.append(mean*weight)
    return sum(weighted_sum)/sum(weights)

weighted_mean_function = weighted_mean(houses_per_year['Mean Price'],houses_per_year['Houses Sold'])

from numpy import average
weighted_mean_numpy = average(houses_per_year['Mean Price'],
        weights = houses_per_year['Houses Sold'])

equal = round(weighted_mean_function,10) == round(weighted_mean_numpy,10)
         