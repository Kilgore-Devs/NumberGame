def main():
    import random  # imports rng
    import sys  # imports python details

    def display_title():
        msg = f"Project Program using {sys.version}."  # get sys version from line 3
        print(msg)  # Displays the title of the program and the current version of python.

    display_title()

    class PlayGame:  # defines class

        def __init__(self):  # selecting the range of numbers
            self.LOWEST = 1  # lowest possible number allowed
            self.HIGHEST = 10  # highest possible number allowed, can be higher if preferred

        def get_random_number(self):  # get a random number using line 2
            return random.randint(self.LOWEST, self.HIGHEST)

        def start(self):  # game start method
            random_number = self.get_random_number()  # generating the random number
            print(f"Guess a number between {self.LOWEST} and {self.HIGHEST}. No cheating or you go to hell!")
            # the actual game
            while True:
                user_number = int(input("Pick a number goober..Type it out and hit enter: "))
                if user_number == random_number:
                    restart = (
                        input('Fuck me you go it right! Do you want to play this dumb shit again? Yes or No. ').lower())
                    if restart == 'yes':
                        main()  # reruns program if user inputs yes
                    else:
                        break  # stops program if no or anything else is input
                elif user_number < random_number:
                    print("WRONG...Too low dumb fuck")  # prints too low if the guess is too low
                else:
                    print("HAHAHA you're wrong..too high")  # prints too high if the guess is too high

    PlayGame = PlayGame()  # instantiates and starts
    PlayGame.start()


main()
