import numpy
#this is an alternative usage of levenshtein-distance algorithm. Main difference is using numpy.zeros to create the right matrix. Much simpler
def levenshteinDistanceDP(token1, token2):
    distances = numpy.zeros((len(token1) + 1, len(token2) + 1))

    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1

    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2
        
    printDistances(distances, len(token1), len(token2))
    return 0

def printDistances(distances, token1Length, token2Length):
    for t1 in range(token1Length + 1):
        for t2 in range(token2Length + 1):
            print(int(distances[t1][t2]), end=" ")
        print()
        
levenshteinDistanceDP("hello", "helo")
