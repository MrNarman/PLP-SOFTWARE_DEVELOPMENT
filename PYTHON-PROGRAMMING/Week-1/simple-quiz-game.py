def run_quiz():
    # A list of dictionary quiz questions
    # Each dictionary contains a question, options, and the correct answer
    quiz_questions = [
        {
            "question": "What is the output of print(2 ** 3)?",
            "options": ["6", "8", "9", "12"],
            "answer": "8"
        },
        {
            "question": "Who directed the movie 'Inception'?",
            "options": ["Christopher Nolan", "James Cameron", "Steven Spielberg", "Quentin Tarantino"],
            "answer": "Christopher Nolan"
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["func", "define", "def", "function"],
            "answer": "def"
        },
        {
            "question": "What is the capital of Wakanda in the Marvel universe?",
            "options": ["Birnin Zana", "Asgard", "Zamunda", "Kamar-Taj"],
            "answer": "Birnin Zana"
        },
        {
            "question": "Which data structure does a FIFO system represent?",
            "options": ["Stack", "Queue", "List", "Dictionary"],
            "answer": "Queue"
        }
    ]

    score = 0
    options = ["A", "B", "C", "D"]

    for quiz in quiz_questions:
        print("\n" + quiz["question"])

        #Using index manually
        i = 0
        while i < len(quiz["options"]):
            print(f"{options[i]}. {quiz['options'][i]}")
            i += 1
        
        user_answer = input("Please enter the letter of your answer: ").upper()

        if user_answer in options:
            selected_index = options.index(user_answer)
            if quiz["options"][selected_index] == quiz["answer"]:
                print("Correct!")
                score += 1
            else:
                correct_index = quiz["options"].index(quiz["answer"])
                print(f"Incorrect! The correct answer was {options[correct_index]}. {quiz['options'][correct_index]}.")
        else:
            print("Invalid option. Please enter A, B, C, or D.")

    print(f"Your final score is {score} out of {len(quiz_questions)}.")
    
# Loop to allow the user to play the quiz multiple times
while True:
    run_quiz()
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break