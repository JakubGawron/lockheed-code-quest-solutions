import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

rankNames = ['ACE', 'KING', 'QUEEN', 'JACK']
for _ in range(int(input())):
    scores = {
        'player': 0,
        'dealer': 0
    }
    for k in scores.keys():
        aces = 0
        for card in [card.split('_', maxsplit=1)[0] for card in input().split()]:
            if card in rankNames:
                if card == 'ACE':
                    aces += 1
                    continue
                scores[k] += 10
                continue
            scores[k] += int(card)
        
        if aces:
            temp = scores[k] + 10 + aces
            if temp <= 21:
                scores[k] = temp
            else:
                scores[k] += aces

    print(f"Player Score: {scores['player']} Dealer Score: {scores['dealer']}", end=' ')
    if scores['player'] > 21:
        print('Dealer Wins!')
    elif scores['dealer'] > 21:
        print('Player Wins!')
    elif scores['player'] > scores['dealer']:
        print('Player Wins!')
    elif scores['dealer'] > scores['player']:
        print('Dealer Wins!')
    else:
        print('Tie!')