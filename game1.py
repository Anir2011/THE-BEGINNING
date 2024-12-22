import random

# دالة لتحديد الفائز بين اللاعب والكمبيوتر
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

# دالة لبدء اللعبة
def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    choices = ['rock', 'paper', 'scissors']  # خيارات اللعبة

    while True:
        player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

        # التأكد من أن الإدخال صالح
        if player_choice not in choices:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
            continue

        # اختيار الكمبيوتر عشوائيًا
        computer_choice = random.choice(choices)

        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        # تحديد الفائز
        result = determine_winner(player_choice, computer_choice)
        print(result)

        # سؤال اللاعب إذا كان يريد اللعب مرة أخرى
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

# تشغيل اللعبة
if __name__ == "__main__":
    play_game()
