houses_per_year['sum_per_year'] = houses_per_year['Mean Price']*houses_per_year['Houses Sold']
all_sums_together = houses_per_year['sum_per_year'].sum()
total_n_houses = houses_per_year['Houses Sold'].sum()
weighted_mean = all_sums_together/total_n_houses
                                                                                
mean_original = houses['SalePrice'].mean()
                                                                                
difference = round(mean_original,10) - round(weighted_mean,10)                                                                                