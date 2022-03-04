import copy

import Vars

def display():
    pieceColour = {
        0: "\033[48;5;235m  \033[0m",
        1: "\033[48;5;220m  \033[0m",
        2: "\033[48;5;45m  \033[0m",
        3: "\033[48;5;208m  \033[0m",
        4: "\033[48;5;20m  \033[0m",
        5: "\033[48;5;160m  \033[0m",
        6: "\033[48;5;40m  \033[0m",
        7: "\033[48;5;63m  \033[0m",
    }
    tl = [[pieceColour[i] for i in n] for n in Vars.screen]
    ts = '\n'.join(list(map(''.join, tl)))
    print('\033[0;0H' + ts)
    #print('\033[2J' + '\033[0;0H' + ts)
    #print(ts)

def game_space():
    Vars.setScreen = [[0 for i in range(Vars.width)] for i in range(Vars.height-5)]
    Vars.screen = copy.deepcopy(Vars.setScreen)