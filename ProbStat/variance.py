C = [1,1,1,1,1,1,1,1,1,21]

def variance(array):
    reference_point = sum(array)/len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
        
    return sum(distances)/len(distances)

variance_C = variance(C)