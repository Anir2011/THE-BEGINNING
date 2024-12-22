import random

# قائمة الكلمات التي سيتم خلط حروفها
words = ["python", "javascript", "java", "programming", "computer", "algorithm", "developer", "machine", "learning"]

# دالة لخلط حروف الكلمة
def scramble_word(word):
    scrambled = ''.join(random.sample(word, len(word)))
    return scrambled

# دالة لبدء اللعبة
def start_game():
    print("Welcome to the Word Scramble Game!")
    score = 0  # عدد النقاط

    # تحديد عدد الجولات
    rounds = 5
    for round_number in range(1, rounds + 1):
        print(f"\nRound {round_number} of {rounds}")

        # اختيار كلمة عشوائية من القائمة
        word = random.choice(words)
        scrambled = scramble_word(word)

        # عرض الكلمة المختلطة للاعب
        print(f"Scrambled word: {scrambled}")

        # طلب إدخال اللاعب
        player_guess = input("Unscramble the word: ").lower()

        # التحقق من صحة الإجابة
        if player_guess == word:
            score += 1
            print("Correct! You've earned a point.")
        else:
            print(f"Wrong! The correct word was '{word}'.")

    print(f"\nGame over! Your final score is: {score}/{rounds}")

# بدء اللعبة
if __name__ == "__main__":
    start_game()
