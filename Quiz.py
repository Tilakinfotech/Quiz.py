import tkinter as tk
from tkinter import messagebox

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "Berlin", "London", "Madrid"],
                "correct_option": 0
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Mars", "Venus", "Jupiter", "Saturn"],
                "correct_option": 0
            },
            {
                "question": "What is the largest mammal?",
                "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
                "correct_option": 1
            }
        ]
        
        self.current_question = 0
        self.score = 0
        
        self.question_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.question_label.pack(pady=10)
        
        self.option_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", command=lambda i=i: self.check_answer(i))
            self.option_buttons.append(button)
            button.pack(pady=5)
        
        self.submit_button = tk.Button(root, text="Submit Quiz", command=self.show_result)
        self.submit_button.pack(pady=10)
        
        self.next_question()
    
    def next_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])
            
            options = question_data["options"]
            for i in range(4):
                self.option_buttons[i].config(text=options[i])
            
            self.current_question += 1
        else:
            self.submit_button.config(state=tk.NORMAL)
    
    def check_answer(self, selected_option):
        question_data = self.questions[self.current_question - 1]
        correct_option = question_data["correct_option"]
        
        if selected_option == correct_option:
            self.score += 1
        
        self.next_question()
    
    def show_result(self):
        result_message = f"Your score: {self.score}/{len(self.questions)}"
        
        correct_answers = "\n\nCorrect answers:\n"
        for i, question in enumerate(self.questions, start=1):
            correct_option = question["correct_option"]
            correct_answer = question["options"][correct_option]
            correct_answers += f"Question {i}: {correct_answer}\n"
        
        result_message += correct_answers
        
        messagebox.showinfo("Quiz Completed", result_message)
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGame(root)
    root.mainloop()
