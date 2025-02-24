# Guessing Game (title)
#
# guess a number between 1 and 100 (instrcutions)
#
# Your Guess                 text area input (integer field - self.addIntegerField(0, row=1, column=1))
#
#
# Next Guess (button)                New Game (button)
#
#
# notification
#
# if guess is too high, change instruction to 'Sorry too large!
# if too low, change instruction to 'Sorry too small!
# when I win, tell me how many guess it took to win
# next guess butoon allows for new guess input
# new game button is disabled until user wins

from breezypythongui import EasyFrame
import random
 
class GuessingGame(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title='Guessing Game')
        self.setSize(500, 250)
        self.score = 0
        self.tryCount = 1
        self.hintFlag = False
        self.val = random.randint(1, 100)
        self.instructions = self.addLabel(text='Guess a number between 1 and 100', row=0, column=2, columnspan=4)
        self.guessField = self.addLabel(text='Your Guess', row=5, column=0 )
        self.input = self.addIntegerField(0, row=5, column=4, width=25)
        self.nextGuessBtn = self.addButton(text='Next Guess', row=5, column=0, command=self.nextGuess)
        self.nextGameBtn = self.addButton(text='Next Game', row=5, column=3, command=self.nextGame, state='disabled')
        self.quitBtn = self.addButton(text='Quit', row=5, column=4, command=self.quitGame)
        self.hintBtn = self.addButton(text='Hint', row=5, column=2, command=self.hintVal)
    
    def nextGuess(self):
        # print(self.input.keys())
        self.guess = int(self.input.getNumber())
        # print(type(self.guess))
        if self.guess == self.val:
            if self.hintFlag == False:
                self.score += 1
            self.instructions['text'] = f'You win in {self.tryCount} turns !!! Score: {self.score}'
            self.nextGameBtn['state'] = 'normal'
            self.nextGuessBtn['state'] = 'disabled'
        elif self.guess > self.val:
            self.instructions['text'] = f'Sorry too large! Turns: {self.tryCount}'
            self.tryCount += 1
        elif self.guess < self.val:
            self.instructions['text'] = f'Sorry too low! Turns: {self.tryCount}'
            self.tryCount += 1
                   
    def nextGame(self):
        self.tryCount = 1
        self.input.setNumber(0)
        self.instructions['text'] = 'Guess a number between 1 and 100'
        self.nextGuessBtn['state'] = 'normal'
        self.nextGameBtn['state'] = 'disabled'
        self.val = random.randint(1, 100)
        print('player score:', self.score)

    def quitGame(self):
        self.tryCount = 1
        self.input.setNumber(0)
        self.instructions['text'] = 'Guess a number between 1 and 100'
        self.nextGuessBtn['state'] = 'normal'
        self.nextGameBtn['state'] = 'disabled'
        self.val = random.randint(1, 100)
    
    def hintVal(self):
        self.instructions['text'] = f'You are {abs(self.input.getNumber() - self.val)} numbers away from the winnning guess!!! \n Lose 1 score point for hint!!!'
        self.score -= 1
        self.hintFlag = True

def main():
    GuessingGame().mainloop()

if __name__ == '__main__':
    main()
