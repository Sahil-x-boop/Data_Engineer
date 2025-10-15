import logging
import random


logging.basicConfig(
    level=logging.DEBUG,
    filename="hangman.log",
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class Hangman:
    def __init__(self):
        self.words = ["list", "csv", "tuples", "loops", "Generator"]
        self.word = random.choice(self.words).lower()
        self.guessing_state = ["_"] * len(self.word)
        self.attempts = 5
        self.letters = len(self.word)

        logging.info(f"Game started. Word length: {len(self.word)}")
        logging.debug(f"Chosen word (hidden from player): {self.word}")

    def right_guess(self) -> bool:
        self.guess = input("Guess a letter : ")
        logging.info(f"User guessed: {self.guess}")
        return self.guess in self.word

    def play(self):
        while self.attempts > 0 and "_" in self.guessing_state:
            print(f"Guessing State: {' '.join(self.guessing_state)}")
            logging.debug(f"Current state: {' '.join(self.guessing_state)}")

            if self.right_guess():
                logging.info(f"Correct guess: {self.guess}")
                for i, ch in enumerate(self.word):
                    if (
                        ch == self.guess
                        and self.guessing_state[i] == "_"
                    ):
                        self.guessing_state[i] = self.guess
                        break
            else:
                self.attempts -= 1
                print("You Guessed wrong")
                logging.warning(f"Wrong guess: {self.guess}."
                                f" Attempts left: {self.attempts}")

            print(f"Now you have {self.attempts} attempts left\n")
            logging.debug(f"Attempts left: {self.attempts}")

            if "_" not in self.guessing_state:
                print(f"Right the word is {' '.join(self.guessing_state)}")
                logging.info("Player won the game!")
                break

        if "_" in self.guessing_state:
            logging.error(f"Player lost. The word was: {self.word}")


hangman = Hangman()
hangman.play()


# import random


# def hangman():
#     words = ["list", "csv", "tuples", "loops", "Generators"]
#     word = random.choice(words)
#     guessing_state = ["_"] * len(word)
#     attempts = 6
#     while attempts > 0 and "_" in guessing_state:
#         print(f"Guessing State: {guessing_state}\n")
#         guess = input("Guess a letter : ")
#         if guess in word:
#             for i, ch in enumerate(word):
#                 if ch == guess and guessing_state[i] == "_":
#                     guessing_state[i] = guess
#                     break
#         else:
#             attempts -= 1
#             print("You Guessed wrong")
#         print(f"Now you have {attempts} attempts left\n")
#         if "_" not in guessing_state:
#             print(f"Right the word is {guessing_state}")
#             break


# hangman()

# # -- rough work ----
# guess = ["_"] * 5
# word = "hello"
# attempts = 5
# while attempts > 0:
#     char = input("Guess a letter : ")
#     for i, ch in enumerate(word):
#         if ch == char:
#             guess[i] = char
#             break
#     attempts -= 1
# print(guess)
# print(attempts)

def test(a, b, c, d=1, e=2):
    pass


test(3, 5, 7, d=2, e=7)
