import random
import numpy as np
from reportlab.pdfgen import canvas

class MatrixQuestionGenerator:
    def __init__(self):
        self.question_types = [
            self.generate_transpose_question,
            self.generate_multiplication_question,
            self.generate_determinant_question,
            self.generate_inverse_question
        ]
        self.filename = "matrix_questions.pdf"
        self.pdf = canvas.Canvas(self.filename)

    def generate_transpose_question(self):
        matrix = np.random.randint(1, 10, size=(3, 3))
        question = f"What is the transpose of the matrix:\n{matrix}?"
        answer = np.transpose(matrix)
        return question, answer

    def generate_multiplication_question(self):
        matrix1 = np.random.randint(1, 10, size=(2, 2))
        matrix2 = np.random.randint(1, 10, size=(2, 2))
        question = f"What is the result of multiplying the matrices:\n{matrix1}\nand\n{matrix2}?"
        answer = np.dot(matrix1, matrix2)
        return question, answer

    def generate_determinant_question(self):
        matrix = np.random.randint(1, 10, size=(2, 2))
        question = f"What is the determinant of the matrix:\n{matrix}?"
        answer = np.linalg.det(matrix)
        return question, answer

    def generate_inverse_question(self):
        matrix = np.random.randint(1, 10, size=(2, 2))
        question = f"What is the inverse of the matrix:\n{matrix}?"
        answer = np.linalg.inv(matrix)
        return question, answer

    def generate_question(self):
        question_func = random.choice(self.question_types)
        return question_func()

    def solve_question(self, question, user_answer):
        if isinstance(user_answer, np.ndarray):
            return np.array_equal(question[1], user_answer)
        return question[1] == user_answer

    def show_solution(self, question, answer):
        solution = f"Solution:\n{answer}"
        self.pdf.setFont("Helvetica", 12)
        self.pdf.drawString(50, self.pdf._pagesize[1] - 100, solution)

    def evaluate_user_answer(self, question, user_answer):
        is_correct = self.solve_question(question, user_answer)
        if is_correct:
            self.pdf.setFont("Helvetica-Bold", 12)
            self.pdf.drawString(50, self.pdf._pagesize[1] - 100, "Correct!")
        else:
            self.pdf.setFont("Helvetica-Bold", 12)
            self.pdf.drawString(50, self.pdf._pagesize[1] - 100, "Incorrect.")
            self.show_solution(question, question[1])

        self.pdf.showPage()

    def generate_and_solve_questions(self, num_questions):
        for i in range(num_questions):
            question, answer = self.generate_question()
            self.pdf.setFont("Helvetica-Bold", 14)
            self.pdf.drawString(50, self.pdf._pagesize[1] - 50, f"Question {i+1}:")
            self.pdf.setFont("Helvetica", 12)
            self.pdf.drawString(50, self.pdf._pagesize[1] - 75, question)
            user_answer = input("Enter your answer: ")
            self.evaluate_user_answer(question, user_answer)

        self.pdf.save()
        print(f"Questions and answers have been written to '{self.filename}'.")

