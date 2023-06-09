##Functions to calculate the Elo rating of a player after a match
import math
##Calculates expected Probability of winning for player A
def expProb(RA,RB):
    return 1/(1+10**((RA-RB)/400))

def wElo(numGamesA, numGamesB, result):
    ##When player A wins
    if (result == 1):
        return ((numGamesA)/(numGamesA+numGamesB))
    ##When player B wins
    elif (result == 0):
        return ((numGamesB)/(numGamesA+numGamesB))

##Calculates new Elo rating if reult is 1, player A won, 0 if player B won
def newRating(RA, RB, numGamesA, numGamesB , K, result):
    ##When player A wins
    if (result == 1):
        RA = RA + K*(1-expProb(RA,RB))(wElo(numGamesA, numGamesB, result))
        RB = RB + K*(0-expProb(RB,RA))(wElo(numGamesA, numGamesB, result))
    ##When player B wings
    elif (result == 0):
        RA = RA + K*(0-expProb(RA,RB))(wElo(numGamesA, numGamesB, result))
        RB = RB + K*(1-expProb(RB,RA))(wElo(numGamesA, numGamesB, result))

    return RA, RB

