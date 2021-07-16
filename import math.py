import math

def minimumTime(numOfParts, parts):
    # WRITE YOUR CODE HERE
    print("teste")
    if (numOfParts == 0):
        return 0
    
    init  = int(math.floor(numOfParts / 2))

    times = []
    
    while (len(parts) > 1):
        timeNow = parts[init-1] + parts[init]
        times.append(timeNow)
        del parts[init]
        parts[init-1] = timeNow
        init  = int(math.floor(len(parts) / 2))
    
    finalTime = 0
    for item in times:
        finalTime = finalTime + item
    return finalTime
    
def main():
    print("teste")
    teste = [8, 4, 6, 12]
    timeFinal = minimumTime(4, teste)
    print(timeFinal)