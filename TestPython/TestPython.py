

if __name__ == "__main__":

    stages = [ "" , "________ " , "| | " , "| L0" , "| /|\ " , "| / \ " , "| " ]
    while True:
        wrong_guesses = 0
        wrong_guessed = set()
        right_guessed = []
        word = input("\t Word: ").upper()
        right_guessed = ["_" for i in word]

        while wrong_guesses < len(stages)-1:
           
            print('\n \t', " ".join(right_guessed), "\n")

            guess = ""
            while not guess.isalpha() or len(guess) != 1:
                guess = input("\t Type a letter: ").upper()

            if guess not in word or guess in right_guessed:
                if guess in right_guessed:
                    print("You've already guessed that!")
                wrong_guesses += 1
                wrong_guessed.add(guess)
                print("\n","Guesses: ", sorted(wrong_guessed), "\n")
                print("\n","\n".join(stages[:wrong_guesses]), "\n")
            else:
                for index, letter in enumerate(word):
                    if letter == guess:
                        right_guessed[index] = letter
        
            if right_guessed == list(word):
                print("\nYou won!!\n")
                break
        if wrong_guesses >= 6:
            print ("\nYou lost!\n")
        print("\tThe word was:", word)
                


