import random

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_welcome_message(self):
        print("The Quiz Game!")
        input("Press Enter to Start the quiz game ")

        print("Let's get started!\n")
        print("WELCOME \n")
        input("Press Enter for the rules of quiz ")

        print(" fill-in-the-blank questions on the some general knowledge questions.")
        print("RULES FOR THE QUIZ ARE : \n 1. YOU WILL GET ONLY ONE CHANCE TO ANSWER THE QUESTION.\n"
              "2.THERE ARE 7 QUESTIONS IN TOTAL , EACH QUESTION IS COMPULSORY.\n"
              "3.THE CORRECT ANSWER WILL BE DISPLAYED AFTER ANSWERING EACH QUESTION.\n"
              "4.THE SCORES OF THE GAME WILL BE DISPLAYED IN THE END ")
        input("Press Enter to play !")


    def present_quiz_questions(self):
        for i, question in enumerate(self.questions, 1):
            print(f"Question {i}: {question['question']}")
            if 'choices' in question:
                for choice_num, choice in enumerate(question['choices'], 1):
                    print(f"{choice_num}. {choice}")
            user_answer = input("Your answer: ")
            self.evaluate_user_answer(question, user_answer)

    def evaluate_user_answer(self, question, user_answer):
        if user_answer.lower() == question['answer'].lower():
            print("Correct!\n")
            self.score += 1
        else:
            print("Incorrect.")
            print(f"The correct answer is: {question['answer']}\n")

    def display_final_results(self):
        print("Quiz Finished!")
        print(f"Your final score is: {self.score}/{len(self.questions)}")

    def play_again(self):
        play_again = input("Do you want to play again? (yes/no): ").upper()
        return play_again == 'YES'


# quiz questions
quiz_questions = [
    {
        'question': "What is the capital of France?",
        'answer': "Paris"
    },
    {
        'question': "Which planet is known as the 'Red Planet'?",
        'answer': "Mars"
    },
    {
        'question': "Who was the Ancient Greek God of the Sun?",
        'answer': "Apollo"
    },
    {
        'question': "What was the name of the crime boss who was head of the feared Chicago Outfit?",
        'answer': "Al Capone"
    },
    {
        'question': "What city is known as The Eternal City?",
        'answer': "Rome"
    },
    {
        'question': "Who discovered that the earth revolves around the sun?",
        'answer': "Nicolaus Copernicus"
    },
    {
        'question': "What art form is described as decorative handwriting or handwritten lettering?",
        'answer': "Caligraphy"
    }
]

# Main game loop
while True:
    game = QuizGame(quiz_questions)
    game.display_welcome_message()
    game.present_quiz_questions()
    game.display_final_results()

    if not game.play_again():
        print("THANK YOU FOR PLAYING!")
        break
