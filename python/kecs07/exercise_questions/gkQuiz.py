# a program that asks 5 gk question(in random order) and records the responses to 
# give a final remark based on how many questions were answered correctly

# we will use a list of dictionaries, each dictionary will have 3 key-value pairs, question, options(a list), correct option

import random

def get_questions() -> list:
    question_set = []
    n = int(input("Enter the number of questions you wish to add: "))

    for i in range(n):
        temp = {}
        temp["qus"] = input(f"Enter question {i + 1}:\n")
        temp["ans"] = input("Enter answer: ")
        temp["options"] = [temp["ans"]]

        #adding 3 other options in the option list other than the correct answer
        print("Enter 3 other incorrect options: ")
        for i in range(3):
            temp["options"].append(input())

        #adding the question, it's answer and options all bundled in a single dict to the set of questions
        question_set.append(temp)
    
    return question_set

def display_quiz(questions: list) -> int:
    """
        the questions parameter is a list of dictionaries, each dictionary corresponds to a question
        it returns the number of correctly answered questions
    """
    random.shuffle(questions)
    count = 0

    for i in range(len(questions)):
        qus = questions[i]["qus"]
        options = questions[i]["options"]
        ans = questions[i]["ans"]

        #ask question
        print(f"Q{i + 1}. {qus}")

        #display options
        random.shuffle(options)
        for i in range(4):
            print(f"Option{i+1}: {options[i]}")
        
        #get and verify answer
        #   get answer
        while True:
            choice = int(input("Enter your choice(1/2/3/4): "))
            if choice in range(1, 5):
                break
            else:
                print("Not a valid input.")
        
        #   get index of the answer in options
        correct_index = options.index(ans)
        
        #   verify if the answer is correct
        if (choice - 1) == correct_index:
            count += 1

    return count
    
def evaluate(x: int, y: int):
    """
    x -> no of correct answers
    y -> total questions
    """

    print(f"Your score: {x}/{y}")
    perc = x / y * 100

    if perc >= 90:
        print("Shabaas! Ehi tarah mehnat kro...")
    elif perc >= 80:
        print("Bdiya! Mehnat krte rho...")
    elif perc >= 70:
        print("Thik h, pr aur behtar kro...")
    elif perc >= 60:
        print("Gadbad h! Padhaai kro...")
    elif perc >= 50:
        print("Haalat kharab h...")


paper = get_questions()
correct = display_quiz(paper)
evaluate(correct, len(paper))