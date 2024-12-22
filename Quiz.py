import random
import time

# الأسئلة والخيارات (تم إضافة أسئلة جديدة)
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Paris", "B) London", "C) Berlin", "D) Madrid"],
        "answer": "A"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A) Earth", "B) Jupiter", "C) Mars", "D) Saturn"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A) Shakespeare", "B) Dickens", "C) Tolstoy", "D) Austen"],
        "answer": "A"
    },
    {
        "question": "What is the smallest country in the world?",
        "options": ["A) Vatican City", "B) Monaco", "C) San Marino", "D) Liechtenstein"],
        "answer": "A"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["A) Oxygen", "B) Osmium", "C) Ozone", "D) Opium"],
        "answer": "A"
    },
    # أسئلة جديدة:
    {
        "question": "Who won the 2018 World Cup?",
        "options": ["A) Brazil", "B) France", "C) Germany", "D) Argentina"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean in the world?",
        "options": ["A) Atlantic Ocean", "B) Pacific Ocean", "C) Indian Ocean", "D) Arctic Ocean"],
        "answer": "B"
    },
    {
        "question": "Who invented the telephone?",
        "options": ["A) Thomas Edison", "B) Alexander Graham Bell", "C) Nikola Tesla", "D) Albert Einstein"],
        "answer": "B"
    },
    {
        "question": "What is the capital of Japan?",
        "options": ["A) Beijing", "B) Seoul", "C) Tokyo", "D) Hong Kong"],
        "answer": "C"
    },
    {
        "question": "Who was the first person to walk on the moon?",
        "options": ["A) Yuri Gagarin", "B) Neil Armstrong", "C) Buzz Aldrin", "D) Michael Collins"],
        "answer": "B"
    }
]

# دالة لطرح الأسئلة مع مؤقت زمني
def ask_question(question_data):
    print("\n" + question_data["question"])
    for option in question_data["options"]:
        print(option)

    # تحديد الوقت المخصص للإجابة (10 ثواني)
    start_time = time.time()

    # طلب الإجابة من اللاعب مع التأكد أنها واحدة من A, B, C, D
    while True:
        player_answer = input("Your answer (A/B/C/D): ").upper()
        
        # التأكد من أن المدخلات صحيحة
        if player_answer not in ["A", "B", "C", "D"]:
            print("Invalid choice! Please choose from A, B, C, or D.")
            continue  # إذا كانت المدخلات غير صالحة، طلب الإدخال مرة أخرى
        
        # إذا كانت المدخلات صالحة، نخرج من الحلقة
        break

    elapsed_time = time.time() - start_time

    # التأكد من أن اللاعب جاوب في الوقت المحدد
    if elapsed_time > 10:
        print(f"Time's up! You didn't answer in time (Time taken: {elapsed_time:.2f}s).")
        return False

    # التحقق من صحة الإجابة
    if player_answer == question_data["answer"]:
        return True
    else:
        return False

# دالة لبدء اللعبة
def start_game():
    print("Welcome to the Trivia Quiz Game!")
    score = 0  # عدد النقاط
    random.shuffle(questions)  # خلط الأسئلة لتكون عشوائية

    # طرح الأسئلة على اللاعب
    for i, question_data in enumerate(questions):
        print(f"\nQuestion {i + 1}:")
        if ask_question(question_data):
            print("Correct answer!")
            score += 1
        else:
            print(f"Wrong answer! The correct answer was {question_data['answer']}.")

        # عرض النتيجة الحالية بعد كل سؤال
        print(f"Your current score is: {score}/{i + 1}")

    # عرض النتيجة النهائية
    print(f"\nGame over! Your final score is: {score}/{len(questions)}")

# بدء اللعبة
if __name__ == "__main__":
    start_game()
