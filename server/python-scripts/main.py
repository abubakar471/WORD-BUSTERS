import sys
import random

guess = sys.stdin.read();
next_guess = sys.stdin.read();
wordlist = ['minister', 'king', 'horse', 'buggati', 'ant'];
display_word = [];
secret_word = random.choice(wordlist);
empty_string = ""
retry_chance = 0

print('working scripts')

# for letter in secret_word:
#     display_word += "_";

# print(display_word)

# for index, letter in enumerate(secret_word):
    # if (letter == guess):
    #     empty_string += letter
    #     display_word[index] = letter
    #     print(display_word)

    #     if (len(empty_string) < len(secret_word)):
    #         print("")
    #         ask = next_guess
    #         guess = ask
        
    #     if(len(empty_string) == len(secret_word)):
    #         print("Congratulations :)  \nyou have correctly guessed the word");

    # else:
    #     if retry_chance < 5:
    #         retry_chance += 1;
    #         print(f"wrong :< you have {5 - retry_chance} chances");
    #         # if(retry_chance == 0):
    #         #     print(f"wrong :< you have 4 chances");
    #         # else:
    #         #     print(f"wrong :< you have {5 - (retry_chance - 1)} chances");
            
            

    #         guess = input("guess the letter : ").lower()

    #         if (letter == guess):
    #             empty_string += letter
    #             display_word[index] = letter
    #             print(display_word);
    #             if (len(empty_string) < len(secret_word)):
    #                 ask = input("Guess the next letter : ")
    #                 guess = ask
                
    #             if(len(empty_string) == len(secret_word)):
    #                 print("Congratulations :)  \nyou have correctly guessed the word");
            
    #     else:
    #         print("Game Over :(")
    #         break