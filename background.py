import numpy as np
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

terminal_ht = 20
terminal_width= 60
#The basic drawing board
class Screen:

    def __init__(self):
        self.screen_height = terminal_ht
        self.screen_width = terminal_width
        self.screen = np.full((self.screen_height,self.screen_width), ' ', dtype=np.unicode)
    
    def move_right(self):
        for base in self.screen:
            for i in range(0,len(base)):
                if i == self.screen_width-1:
                    pass
                else:
                    base[i] = base[i+1]
    
    def move_left(self):
         for base in self.screen:
            for i in range(len(base)-1,0,-1):
                if i == len(base):
                    pass
                else:
                    base[i] = base[i-1]
    
    #Colors are added whenever they are printed
    def draw(self):
        for base in self.screen:
            for stone in base[20:45]:
                if stone == '#':
                    print(Fore.LIGHTGREEN_EX+stone+Style.RESET_ALL, end=" ")
                elif stone == '$':
                    print(Fore.YELLOW+stone+Style.RESET_ALL, end=" ")
                elif stone == '8':
                    print(Fore.LIGHTRED_EX+stone+Style.RESET_ALL, end=" ")
                elif stone == 'x':
                    print(Fore.LIGHTCYAN_EX+stone+Style.RESET_ALL, end=" ")
                elif stone == '?':
                    print(Fore.LIGHTMAGENTA_EX+stone+Style.RESET_ALL, end=" ")
                elif stone == '>' or stone == '<':
                    print(Fore.RED+stone+Style.RESET_ALL, end=" ")
                elif stone == '0':
                    print(Fore.BLUE+stone+Style.RESET_ALL, end=" ")
                
                else:
                    print(stone,end = " ")
            print(' ')
