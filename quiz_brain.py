class QuizBrain:
    def __init__(self , question_bank):
        self.question_number = 0
        self.score = 0
        self.question_list = question_bank

    def next_question(self):
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {self.question_list[self.question_number - 1].question}.  (True/False): ")
        correct_answer = self.question_list[self.question_number - 1].answer
        self.check_answer(user_answer, correct_answer)


    def still_has_questions(self):
        return self.question_number < (len(self.question_list))

    def check_answer(self,user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it Right !")
        else:
            print("You got it Wrong !")
        print(f"The correct answer was {correct_answer}")
        print(f"Your score is {self.score}/{self.question_number}")
        print("\n")