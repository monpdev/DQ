distribution_1 = [42, 24, 32, 11]
distribution_2 = [102, 32, 74, 15, 38, 45, 22]
distribution_3 = [3, 12, 7, 2, 15, 1, 21]

def findmean(arrayn):
    sum_distribution = 0
    for value in arrayn:
        sum_distribution += value
    return sum_distribution/len(arrayn)

mean_1 = findmean(distribution_1)
mean_2 = findmean(distribution_2)
mean_3 = findmean(distribution_3)