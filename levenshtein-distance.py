import numpy as np
def levenshtein_distance(s, t, ratio_calc = False):

    # Initialize matrix of zeros
    rows = len(s)+1
    cols = len(t)+1
    distance = np.zeros((rows,cols),dtype = int)

    # Populate matrix alternatively we can use zero function. Check alternative.py
    for i in range(1, rows):
        for k in range(1,cols):
            distance[i][0] = i
            distance[0][k] = k

    # Iterate over the matrix to compute the cost of deletions,insertions and/or substitutions    
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0 # If the characters are the same in the two strings in a given position [i,j] then the cost is 0
            else:
                # the cost of a substitution is 2. If we calculate just distance, then the cost of a substitution is 1.
                if ratio_calc == True:
                    cost = 2
                else:
                    cost = 1
            distance[row][col] = min(distance[row-1][col] + 1,      # deletions
                                 distance[row][col-1] + 1,          # insertions
                                 distance[row-1][col-1] + cost)     # substitutions
    if ratio_calc == True:
        # Computation of the Levenshtein Distance
        Ratio = ((len(s)+len(t)) - distance[row][col]) / (len(s)+len(t))
        return Ratio
    else:
        # print(distance) #  watch computes the cost of deletions,
        # insertions and/or substitutions
        # This is the minimum number of chars required to convert string a to string b
        return "{} chars required ".format(distance[row][col])

difference = levenshtein_distance('hello', 'helo')

print(difference)
