import random


def get_int(prompt: str, min_val: int = None, max_val: int = None) -> int:
    """Safely get an integer from the user."""
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                raise ValueError
            if max_val is not None and value > max_val:
                raise ValueError
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_questions() -> list:
    questions = []
    total = get_int("Enter the number of questions you wish to add: ", 1)

    for q_no in range(1, total + 1):
        print(f"\n--- Question {q_no} ---")
        question_text = input("Enter question: ")
        correct_answer = input("Enter correct answer: ")

        options = [correct_answer]
        print("Enter 3 incorrect options:")
        while len(options) < 4:
            opt = input()
            if opt not in options:
                options.append(opt)
            else:
                print("Option already exists. Enter a different one.")

        random.shuffle(options)
        correct_index = options.index(correct_answer)

        questions.append({
            "question": question_text,
            "options": options,
            "correct_index": correct_index
        })

    return questions


def ask_question(question_data: dict, q_no: int) -> bool:
    """Ask one question and return True if answered correctly."""
    print(f"\nQ{q_no}. {question_data['question']}")

    for idx, option in enumerate(question_data["options"], start=1):
        print(f"Option{idx}: {option}")

    choice = get_int("Enter your choice (1-4): ", 1, 4)
    return (choice - 1) == question_data["correct_index"]


def display_quiz(questions: list) -> int:
    random.shuffle(questions)
    score = 0

    for q_no, question in enumerate(questions, start=1):
        if ask_question(question, q_no):
            score += 1

    return score


def evaluate(score: int, total: int) -> None:
    percentage = (score / total) * 100
    print(f"\nYour score: {score}/{total}")

    if percentage >= 90:
        print("Shabaas! Ehi tarah mehnat kro...")
    elif percentage >= 80:
        print("Bdiya! Mehnat krte rho...")
    elif percentage >= 70:
        print("Thik h, pr aur behtar kro...")
    elif percentage >= 60:
        print("Gadbad h! Padhaai kro...")
    else:
        print("Haalat kharab h...")


def main():
    questions = get_questions()
    score = display_quiz(questions)
    evaluate(score, len(questions))


if __name__ == "__main__":
    main()
