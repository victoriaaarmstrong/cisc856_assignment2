import numpy as np

ITERATIONS = 50000
ALPHA = 0.001

########################
## Prisoner's Dilemma ##
########################
REWARD_P1_P = [[5, 0], [10, 1]]
REWARD_P2_P = [[5,10], [0, 1]]
POLICY_P1_P = [0.5, 0.5]
POLICY_P2_P = [0.5, 0.5]

########################
###### Penny Game ######
########################
REWARD_P1_PE = [[1, -1], [-1, 1]]
REWARD_P2_PE = [[-1, 1], [1, -1]]
POLICY_P1_PE = [0.2, 0.8]
POLICY_P2_PE = [0.2, 0.8]

#########################
## Rock Paper Scissors ##
#########################
REWARD_P1_R = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]
REWARD_P2_R = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
POLICY_P1_R = [0.6, 0.2, 0.2]
POLICY_P2_R = [0.6, 0.2, 0.2]


def algorithmOne():
    return

def algorithmTwo():
    return

def main(game, iterations=ITERATIONS):
    if game == "prisoners_dilemma":
        rewardOne = REWARD_P1_P
        rewardTwo = REWARD_P2_P
        policyOne = POLICY_P1_P
        poicyTwo = POLICY_P2_P

    elif game == "penny_game":
        rewardOne = REWARD_P1_PE
        rewardTwo = REWARD_P2_PE
        policyOne = POLICY_P1_PE
        policyTwo = POLICY_P2_PE

    elif game == "rock_paper_scissors":
        rewardOne = REWARD_P1_R
        rewardTwo = REWARD_P2_R
        policyOne = POLICY_P1_R
        policyTwo = POLICY_P2_R

    else:
        print("Error: unsupported game, check name or type another")


    return

main("prisoners_dilemma")
main("penny_game")
main("rock_paper_scissors")