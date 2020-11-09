#Sort the values
rooms = houses['TotRms AbvGrd'].copy()
rooms = rooms.replace({'10 or more': 10})
rooms = rooms.astype(int)
rooms_sorted = rooms.sort_values()

#Find the median
middle_indices = [int((len(rooms_sorted)/2)-1),
                  int((len(rooms_sorted)/2))
                 ] #len-1 and len because Series use 0-indexing
middle_values = rooms_sorted.iloc[middle_indices] 
median = middle_values.mean()