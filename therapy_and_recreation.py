import random

def create_puzzle():

    games = [
        {'numbers' : [1,2,3,4], 'answer' : 5, 'options' : [2,5,10]},
        {'numbers' : [2,4,6,8], 'answer' : 10, 'options' : [10,20,15]},
        {'numbers' : [5,10,15,20], 'answer' : 25, 'options' : [20,15,25]},
        {'numbers' : [1,2,3,5,8], 'answer' : 13, 'options' : [13,12,14]},
        {'numbers' : [20,17,14,11], 'answer' : 8, 'options' : [9,10,8]},
    ]

    random_game = random.randint(0,len(games)-1)

    return games[random_game]