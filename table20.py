import random
import math

def generate_question():
    num1 = random.randint(2, 20)
    num2 = random.randint(2, 10)
    if random.choice([True, False]):
        return f"{num1}x{num2}", num1*num2
    else:
        return f"{num2}x{num1}", num1*num2

def main():
    total_questions = 0
    correct_answers = 0
    wrong_answers = 0

    while True:
        question, answer = generate_question()
        user_input = input(f"{question} = ")
        
        if user_input.lower() == "exit":
            break
        
        try:
            if int(user_input) == answer:
                print("CORRECT!")
                correct_answers += 1
            else:
                print(f"WRONG! it's {answer}")
                wrong_answers += 1
        except ValueError:
            print("Invalid input. Please enter a number.")
            wrong_answers += 1
        
        total_questions += 1

    if total_questions > 0:
        percentage = (correct_answers / total_questions) * 100
    else:
        percentage = 0
    
    print("\nScore-board:")
    print(f"Total Questions: {total_questions}")
    print(f"Correct Answers: {correct_answers}")
    print(f"Wrong Answers: {wrong_answers}")
    print(f"Percentage Right: {percentage:.2f}%")

if __name__ == "__main__":
    main()



