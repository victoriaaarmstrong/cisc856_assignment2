import numpy as np
import random
import matplotlib.pyplot as plt

ITERATIONS = 50000
ALPHA = 0.001

# helper functions
def normalize(arr):
    sum_arr = sum(arr)
    return [i/sum_arr for i in arr]

def soft_max(arr):
    ex = np.exp(arr - np.max(arr))
    return list(ex / ex.sum(axis=0))

def normalize_min(arr):
    sum_arr = sum([i if i > 0 else 0 for i in arr])
    return [i/sum_arr if i > 0 else 0 for i in arr]

def algorithmOne(game):
    if game == "prisoners_dilemma":
        rewardMatrixOne = [[5, 0], [10, 1]]
        rewardMatrixTwo = [[5, 10], [0, 1]]
        policyOne = [0.5, 0.5]
        policyTwo = [0.5, 0.5]

    elif game == "penny_game":
        rewardMatrixOne = [[1, -1], [-1, 1]]
        rewardMatrixTwo = [[-1, 1], [1, -1]]
        policyOne = [0.2, 0.8]
        policyTwo = [0.2, 0.8]

    elif game == "rock_paper_scissors":
        rewardMatrixOne = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]
        rewardMatrixTwo = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
        policyOne = [0.6, 0.2, 0.2]
        policyTwo = [0.6, 0.2, 0.2]

    else:
        print("Error: unsupported game, check name or type another")

    historyOne = [policyOne.copy()]
    historyTwo = [policyTwo.copy()]
    lenPol = len(policyOne) ## policies should be the same length for each player

    for i in range(ITERATIONS):
        ## You weren't sampling uniformly, this does sample uniformly - maybe try another way?
        a1 = np.random.choice(a=range(lenPol), p = policyOne)
        a2 = np.random.choice(a=range(lenPol), p = policyTwo)

        rewardOne = rewardMatrixOne[a1][a2]
        rewardTwo = rewardMatrixTwo[a1][a2]

        ## Player One
        for p in range(len(policyOne)):
            ## If the action is selected
            if p == a1:
                policyOne[p] = policyOne[p] + (ALPHA * rewardOne * (1 - policyOne[p]))
            ## If the action isn't selected
            else:
                policyOne[p] = policyOne[p] - (ALPHA * rewardOne* policyOne[p])

        for p in range(len(policyTwo)):
            ## If the action is selected
            if p == a2:
                policyTwo[p] = policyTwo[p] + (ALPHA * rewardTwo * (1 - policyTwo[p]))
            ## If the action isnt' selected
            else:
                policyTwo[p] = policyTwo[p] - (ALPHA * rewardTwo * policyTwo[p])

        historyOne = historyOne + [policyOne.copy()]
        historyTwo = historyTwo + [policyTwo.copy()]

    print(policyOne)
    print(policyTwo)

    return historyOne, historyTwo

def algorithmTwo(game):
    if game == "prisoners_dilemma":
        rewardMatrixOne = [[5, 0], [10, 1]]
        rewardMatrixTwo = [[5, 10], [0, 1]]
        policyOne = [0.5, 0.5]
        policyTwo = [0.5, 0.5]

    elif game == "penny_game":
        rewardMatrixOne = [[1, -1], [-1, 1]]
        rewardMatrixTwo = [[-1, 1], [1, -1]]
        policyOne = [0.2, 0.8]
        policyTwo = [0.2, 0.8]

    elif game == "rock_paper_scissors":
        rewardMatrixOne = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]
        rewardMatrixTwo = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
        policyOne = [0.6, 0.2, 0.2]
        policyTwo = [0.6, 0.2, 0.2]

    else:
        print("Error: unsupported game, check name or type another")

    historyOne = [policyOne.copy()]
    historyTwo = [policyTwo.copy()]
    expectationOne = policyOne.copy()
    expectationTwo = policyTwo.copy()

    lenPol = len(policyOne)  ## policies should be the same length for each player

    for i in range(ITERATIONS):
        ## You weren't sampling uniformly, this does sample uniformly - maybe try another way?
        a1 = np.random.choice(a=range(lenPol), p=policyOne)
        a2 = np.random.choice(a=range(lenPol), p=policyTwo)

        rewardOne = rewardMatrixOne[a1][a2]
        rewardTwo = rewardMatrixTwo[a1][a2]

        expectationOne = np.array(expectationOne) + (ALPHA * (np.array(policyOne) - np.array(expectationOne)))
        expectationTwo = np.array(expectationTwo) + (ALPHA * (np.array(policyTwo) - np.array(expectationTwo)))

        ## Player One
        for p in range(len(policyOne)):
            ## If the action is selected
            if p == a1:
                policyOne[p] = policyOne[p] + (ALPHA * rewardOne * (1 - policyOne[p])) + (ALPHA * (expectationOne[p] - policyOne[p]))
            ## If the action isn't selected
            else:
                policyOne[p] = policyOne[p] - (ALPHA * rewardOne * policyOne[p]) + (ALPHA * (expectationOne[p] - policyOne[p]))

        for p in range(len(policyTwo)):
            ## If the action is selected
            if p == a2:
                policyTwo[p] = policyTwo[p] + (ALPHA * rewardTwo * (1 - policyTwo[p])) + (ALPHA * (expectationTwo[p] - policyTwo[p]))
            ## If the action isnt' selected
            else:
                policyTwo[p] = policyTwo[p] - (ALPHA * rewardTwo * policyTwo[p]) + (ALPHA * (expectationTwo[p] - policyTwo[p]))

        historyOne = historyOne + [policyOne.copy()]
        historyTwo = historyTwo + [policyTwo.copy()]

    print(policyOne)
    print(policyTwo)

    return historyOne, historyTwo

historyOne, historyTwo = algorithmTwo('rock_paper_scissors')

#plt.plot(np.array(historyOne)[:,0], np.array(historyTwo)[:0])
plt.plot(np.array(historyOne)[:,0])
plt.plot(np.array(historyOne)[:,1])
plt.plot(np.array(historyOne)[:,2])
plt.show()