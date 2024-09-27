# This is a sample Python script.

# install packages
import matplotlib.pyplot as plt
import pandas as pd
import random

# initiate variables
roll_options = ['nun', 'gimel', 'hey', 'shin']
data_cum = pd.DataFrame(columns=('game', 'winner', 'rounds'))

class player:
    def __init__(self, name, bank):
        self.name = name
        self.bank = bank

def play_dreidel(g, data_cum):
    rounds = 0

    p1 = player('p1', 10) # remove roller
    p2 = player('p2', 10)
    p3 = player('p3', 10)
    p4 = player('p4', 10)
    players = [p1, p2, p3, p4]

    # play game
    pot = 0
    while len(players) > 1:
        rounds += 1

        ## ante one into pot
        for p in players:
            pot += 1
            p.bank -= 1

        ## play a round
        for p in players:

            ## spin dreidel
            roll = random.choice(roll_options)

            ## score results & update roller bank
            if roll == 'nun':
                p.bank = p.bank
            elif roll == 'gimel':
                p.bank = p.bank + pot
                pot = 0
            elif roll == 'hey':
                if pot % 2 > 0:
                    award = pot/2 + 0.5
                else:
                    award = pot / 2
                pot = pot - award
                p.bank = p.bank + award
            else:
                p.bank = p.bank - 1
                pot = pot + 1

            #print(p.name, roll, p.bank)

            ## check player to see if bust
            if p.bank <= 0:
                players.remove(p)
                #print(p.name, ' removed')
        #print('Pot: ', pot)
        #print('Num players: ', len(players))
        #print()
    #print('Rounds: ', rounds)
    data_game= [g, players[0].name, rounds]
    data_cum.loc[len(data_cum.index)] = data_game

def plot_results(data_cum):
    plt.hist(data_cum[['rounds']])
    plt.xlabel('Rounds')
    plt.ylabel('Frequency')
    plt.title('Dreidel Histogram - Bank: 10')
    plt.savefig('results/dreidel_hist.png')
    plt.show()

# Press the button in the header to run the script.
if __name__ == '__main__':
    print('========== New Sim ==========')
    for g in range(1,401):
        #print('Game: ', g, ' complete.')
        play_dreidel(g, data_cum)

print('... simulation complete')
#print()
#print(data_cum)

print()
print(data_cum[['rounds']].describe())
plot_results(data_cum)
