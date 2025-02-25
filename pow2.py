import random
import math

def generate_question():
    num = random.randint(0, 16)
    if random.choice([True, False, True]):  # Randomly decide between square or square root
        return f"2^{num}", pow(2,num)
    else:
        return f"log2({pow(2,num)})", num

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

