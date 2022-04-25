import random

class Person:
    def __init__(self):
        self.bank = 500
        self.current_bet = 0
        self.num_choice = 40
        self.choice = ''
        self.odds = 0

    def get_input(self):
        i = input()
        return i


class Roulette:
    def __init__(self):
        self.numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
        self.colors = ['green','red','black','red','black','red','black','red','black','red','black','black','red','black','red','black','red','black','red','red','black','red','black','red','black','red','black','red','black','black','red','black','red','black','red','black','red']
        self.number = 0
        self.color = ''
        self.dozen = ''
        self.even_odd = ''
        self.low_high = ''
        self.min = 1
        self.max = 1000

    def make_choice(self, player):
        choice = 5
        print('There are 3 main types of bet in roulette: even bets, dozen bets, and straight up bets')
        print('Even bets pay out 1 to 1 and require betting on red vs black, even vs odd, or low (1-18) vs high (19-36)')
        print('Dozen bets pay 2 to 1 bets require betting on the first dozen (1-12), second dozen (13-24), or third dozen (25-36)')
        print('Straight up bets pay out 35 to 1, and require picking one number between 1 and 36')
        while (choice > 3 or choice < 0):
            print('What type of bet would you like to place? Please enter the integer of your choice')
            print('1. Even')
            print('2. Dozen')
            print('3. Straight up')
            print('0. Quit')
            input = player.get_input()
            try:
                choice = int(input)
            except ValueError:
                print("")
            if (choice < 0 or choice > 3):
                print("Sorry, that's not a valid option. Please try again")
        return choice

    def bet_even(self, player):
        choice = 9
        player.odds = 1
        while (choice > 6 or choice < 0):
            print("You've picked an even bet!")
            print('What type of even bet would you like to place? Please enter the integer of your choice')
            print('1. Red')
            print('2. Black')
            print('3. Even')
            print('4. Odd')
            print('5. Low')
            print('6. High')
            print('0. Quit')
            input = player.get_input()
            try:
                choice = int(input)
            except ValueError:
                return False
            if (choice == 0):
                return False
            if (choice < 1 or choice > 6):
                print("Sorry, that's not a valid option. Please try again")
            if (choice == 1):
                player.choice = "red"
                return True
            if (choice == 2):
                player.choice = "black"
                return True
            if (choice == 3):
                player.choice = "Even"
                return True
            if (choice == 4):
                player.choice = "Odd"
                return True
            if (choice == 5):
                player.choice = "Low"
                return True
            if (choice == 6):
                player.choice = "High"
                return True

    def bet_dozen(self, player):
        choice = 9
        player.odds = 2
        while (choice > 6 or choice < 0):
            print("You've picked a dozen bet!")
            print('What dozen? Please enter the integer of your choice')
            print('1. First (1-12)')
            print('2. Second (13-24)')
            print('3. Thirst (25-36)')
            print('0. Quit')
            input = player.get_input()
            try:
                choice = int(input)
            except ValueError:
                return False
            if (choice == 0):
                return False
            if (choice < 1 or choice > 3):
                print("Sorry, that's not a valid option. Please try again")
            if (choice == 1):
                player.choice = "first"
                return True
            if (choice == 2):
                player.choice = "second"
                return True
            if (choice == 3):
                player.choice = "third"
                return True

    def bet_straight(self, player):
        choice = 40
        player.odds = 35
        while (choice > 36 or choice < 0):
            print("You've picked a straight up bet!")
            print('What number between 1 and 36 would you like to bet on? Please enter the integer of your choice')
            input = player.get_input()
            try:
                choice = int(input)
            except ValueError:
                return False
            if (choice == 0):
                return False
            if (choice < 1 or choice > 36):
                print("Sorry, that's not a valid option. Please try again, or bet 0 to quit")
            if (choice > 0 and choice < 37):
                player.num_choice = choice
                return True     

    def spin(self, num):
        self.number = num
        self.color = self.colors[num]
        print("The roulette has been spun, and it's a", self.color, self.number)
        if (num == 0):
            self.dozen = 'zero'
            self.even_odd = 'zero'
            self.low_high = 'zero'
            return False
        if (num > 0 and num < 13):
            self.dozen = 'first'
        if (num > 12 and num < 25):
            self.dozen = 'second'
        if (num > 24 and num < 37):
            self.dozen = 'third'
        if (num % 2 == 0):
            self.even_odd = 'Even'
        if (num % 2 == 1):
            self.even_odd = 'Odd'
        if (num < 19):
            self.low_high = 'Low'
        if (num > 18):
            self.low_high = 'High'
        return True

    def check_winner(self, p):
        if(p.num_choice == self.number or p.choice == self.color or p.choice == self.dozen or p.choice == self.even_odd or p.choice == self.low_high):
            print('Congratulations, you won!')
            return True
        else:
            print("Sorry, you didn't win. Your bank is now down to $", p.bank, ". Better luck next time!", sep='')
            return False
    
    def payout(self, p):
        p.bank += p.current_bet * p.odds + p.current_bet
        print("Your winnings this round total $", p.current_bet * p.odds, " so you know have $", p.bank, "!", sep='')



        

    def make_bet(self, player):
        print("How much would you like to bet? You have $", player.bank, ", the minimum bet is $", self.min, ", and the maximum bet is $", self.max, sep='')
        choice = player.get_input()
        try:
            bet = int(choice)
        except ValueError:
            print("Sorry, that's not a valid bet. Please try again")
            return False
        if (bet > player.bank):
            print("Sorry, you don't have enough money for that. Please try a smaller bet")
            return False
        if (bet < self.min or bet > self.max):
            print("Sorry, for this table the minimum bet is $", self.min, " and the maximum bet is $", self.max, sep='')
            return False
        player.current_bet = bet
        player.bank -= bet
        return True

    def play_again(self, p):
        if (p.bank > 0):
            print('Would you like to play again? Y/N')
            choice = p.get_input()
            try:
                answer = str(choice)
            except ValueError:
                return False
            if (answer == "y" or answer == "Y"):
                return True
        else:
            return False

