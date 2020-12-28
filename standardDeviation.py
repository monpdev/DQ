from math import sqrt
C = [1,1,1,1,1,1,1,1,1,21]

def standard_deviation(array):
    reference_point = sum(array)/len(array)
    
    distances = []
    for value in array:
        squared_distance = (value -reference_point)**2
        distances.append(squared_distance)
        
    variance = sum(distances)/len(distances)
    
    return sqrt(variance)

standard_deviation_C = standard_deviation(C)