from classes import *

def Game():
    r = Roulette()
    p = Person()
    play = True
    while (play):
        choice = r.make_choice(p)
        if (choice == 0):
            break
        if (choice == 1):
                if(r.bet_even(p)):
                    r.make_bet(p)
                else:
                    break
        if (choice == 2):
                if(r.bet_dozen(p)):
                    r.make_bet(p)
                else:
                    break
        if (choice == 3):
                if(r.bet_straight(p)):
                    r.make_bet(p)
                else:
                    break
        r.spin(random.randint(0,36))
        if (r.check_winner(p)):
            r.payout(p)

        play = r.play_again(p)

    print('Thanks for playing!')




if __name__ == "__main__":
    Game()