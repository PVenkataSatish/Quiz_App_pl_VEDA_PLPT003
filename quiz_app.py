import json
import os

QUIZ_FILE = "quizzes.json"
SCORE_FILE = "scores.txt"

def load_quizzes():
    if os.path.exists(QUIZ_FILE):
        with open(QUIZ_FILE, "r") as f:
            return json.load(f)
    return {}

def save_quizzes(quizzes):
    with open(QUIZ_FILE, "w") as f:
        json.dump(quizzes, f, indent=4)

def create_quiz():
    quiz_name = input("Enter a name for the new quiz: ").strip()
    quizzes = load_quizzes()
    
    if quiz_name in quizzes:
        print("Quiz with that name already exists!")
        return

    num_questions = input("How many questions? ")
    while not num_questions.isdigit():
        num_questions = input("Enter a valid number: ")
    
    questions = []
    for i in range(int(num_questions)):
        print(f"\nQuestion {i+1}")
        q_text = input("Enter the question: ").strip()
        options = []
        for j in range(4):
            options.append(input(f"Option {chr(65 + j)}: "))
        correct = input("Enter correct option (A/B/C/D): ").upper()
        while correct not in ['A', 'B', 'C', 'D']:
            correct = input("Invalid. Enter A, B, C, or D: ").upper()
        
        questions.append({
            "question": q_text,
            "options": options,
            "answer": correct
        })

    quizzes[quiz_name] = questions
    save_quizzes(quizzes)
    print(f"Quiz '{quiz_name}' saved successfully!\n")

def take_quiz():
    quizzes = load_quizzes()
    if not quizzes:
        print("No quizzes available!")
        return

    print("Available quizzes:")
    for quiz in quizzes:
        print("-", quiz)
    
    quiz_name = input("Enter quiz name to attempt: ").strip()
    if quiz_name not in quizzes:
        print("Quiz not found!")
        return
    
    questions = quizzes[quiz_name]
    score = 0

    for i, q in enumerate(questions):
        print(f"\nQ{i+1}: {q['question']}")
        for idx, opt in enumerate(q['options']):
            print(f"  {chr(65 + idx)}. {opt}")
        
        answer = input("Your answer (A/B/C/D): ").upper()
        while answer not in ['A', 'B', 'C', 'D']:
            answer = input("Invalid. Enter A, B, C, or D: ").upper()
        
        if answer == q['answer']:
            score += 1
    
    print(f"\nYour Score: {score}/{len(questions)}")

    with open(SCORE_FILE, "a") as f:
        f.write(f"{quiz_name} - Score: {score}/{len(questions)}\n")

def main_menu():
    while True:
        print("\n-- Quiz App Menu--")
        print("1. Create a new quiz")
        print("2. Take a quiz")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ").strip()

        if choice == '1':
            create_quiz()
        elif choice == '2':
            take_quiz()
        elif choice == '3':
            print("Exiting app. Bye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main_menu()
