import random
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class BearingsGame:
    def __init__(self):
        self.questions = []

    def add_question(self, diagram, bearing):
        self.questions.append((diagram, bearing))

    def generate_question(self):
        if not self.questions:
            return None
        index = random.randint(0, len(self.questions) - 1)
        diagram, bearing = self.questions.pop(index)
        return (diagram, bearing)

    def generate_pdf(self):
        pdf = canvas.Canvas("21_questions.pdf", pagesize=letter)

        pdf.setFont("Helvetica-Bold", 16)
        pdf.drawString(50, 750, "21 Questions on Three-Figure Bearings")

        pdf.setFont("Helvetica", 12)

        for i in range(21):
            question = self.generate_question()
            if question is None:
                break
            diagram, correct_answer = question
            pdf.setFont("Helvetica-Bold", 14)
            pdf.drawString(50, 700, f"Question {i + 1}:")
            pdf.setFont("Helvetica", 12)
            pdf.drawString(50, 675, diagram)

            guess = int(input("Enter your answer (in degrees): "))
            if guess == correct_answer:
                pdf.drawString(50, 650, "Correct!")
            else:
                pdf.drawString(50, 650, f"Wrong! The correct answer is {correct_answer} degrees.")

            pdf.showPage()

        pdf.save()
        print("PDF file generated successfully.")

game = BearingsGame()

# Add your questions and answers using the `add_question` method
game.add_question("Diagram 1", 45)
game.add_question("Diagram 2", 90)
game.add_question("Diagram 3", 135)
# Add more questions...

game.generate_pdf()
