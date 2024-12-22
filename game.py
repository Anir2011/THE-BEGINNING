import random  # Importing the random module to generate random numbers

def start_game():
    secret_number = random.randint(1, 100)  # Generate a secret random number between 1 and 100
    attempts = 0  # Variable to count the number of attempts

    print("Welcome to the Guess the Number game!")
    print("Try to guess the number I am thinking of, between 1 and 100.")

    while True:
        try:
            # Asking the player to input their guess
            guess = int(input("Enter your guess: "))
            attempts += 1  # Incrementing the number of attempts

            # Comparing the guess with the secret number
            if guess < secret_number:
                print("Your guess is lower than the secret number.")
            elif guess > secret_number:
                print("Your guess is higher than the secret number.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break  # Exit the loop if the player guesses correctly
        except ValueError:
            print("Please enter a valid number.")  # If the input is not a valid number

def play_again():
    while True:
        choice = input("Do you want to play again? (yes/no): ").lower()
        if choice == 'yes':
            start_game()  # Restart the game if the player wants to play again
        elif choice == 'no':
            print("Thank you for playing! Goodbye.")
            exit()  # Exit the program if the player doesn't want to play again
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

if __name__ == "__main__":
    start_game()  # Start the game
    play_again()  # Ask if the player wants to play again
