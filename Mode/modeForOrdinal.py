def mode(array):
    counts = {}
    
    for value in array:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    return max(counts, key = counts.get)

mode_function = mode(houses['Land Slope'])
mode_method = houses['Land Slope'].mode()
same = (mode_function == mode_method)