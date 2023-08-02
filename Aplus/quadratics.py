import random
import math
from reportlab.pdfgen import canvas

class QuadraticEquationSolver:
    def __init__(self, num_equations, filename):
        self.num_equations = num_equations
        self.equations = []
        self.solutions = []
        self.filename = filename

    # Function to generate a random quadratic equation
    def generate_quadratic_equation(self):
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)
        equation = f"{a}x^2 + {b}x + {c} = 0"
        return equation

    # Function to solve a quadratic equation
    def solve_quadratic_equation(self, a, b, c):
        discriminant = b**2 - 4*a*c

        if discriminant > 0:
            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            x2 = (-b - math.sqrt(discriminant)) / (2*a)
            return (x1, x2)
        elif discriminant == 0:
            x = -b / (2*a)
            return (x,)
        else:
            return ()

    def generate_and_solve_equations(self):
        for _ in range(self.num_equations):
            equation = self.generate_quadratic_equation()
            self.equations.append(equation)

            # Extract coefficients from the equation
            a, b, c = [int(coeff) for coeff in equation.split('x^2')[0].split('x') if coeff]

            # Solve the equation
            equation_solutions = self.solve_quadratic_equation(a, b, c)
            self.solutions.append(equation_solutions)

    def write_solutions_to_pdf(self):
        pdf = canvas.Canvas(self.filename)
        pdf.setFont("Helvetica", 12)

        for equation, solution in zip(self.equations, self.solutions):
            pdf.drawString(50, 750, f"Equation: {equation}")
            pdf.drawString(50, 730, "Solving the equation:")

            # Step-by-step solution
            pdf.drawString(70, 710, "1. Calculate the discriminant: b^2 - 4ac")
            discriminant = b**2 - 4*a*c
            pdf.drawString(90, 690, f"   Discriminant = {b}^2 - 4*{a}*{c} = {discriminant}")

            if discriminant > 0:
                pdf.drawString(70, 670, "2. Since the discriminant is positive, the equation has two real solutions.")
                pdf.drawString(70, 650, "3. Calculate the solutions using the quadratic formula:")
                pdf.drawString(90, 630, f"   x1 = (-b + sqrt(discriminant)) / (2*a)")
                pdf.drawString(90, 610, f"   x1 = (-{b} + sqrt({discriminant})) / (2*{a})")
                pdf.drawString(90, 590, f"   x1 = {(-b + math.sqrt(discriminant)) / (2*a)}")
                pdf.drawString(90, 570, f"   x2 = (-b - sqrt(discriminant)) / (2*a)")
                pdf.drawString(90, 550, f"   x2 = (-{b} - sqrt({discriminant})) / (2*{a})")
                pdf.drawString(90, 530, f"   x2 = {(-b - math.sqrt(discriminant)) / (2*a)}")
            elif discriminant == 0:
                pdf.drawString(70, 670, "2. Since the discriminant is zero, the equation has one real solution.")
                pdf.drawString(70, 650, "3. Calculate the solution using the quadratic formula:")
                pdf.drawString(90, 630, f"   x = -b / (2*a)")
                pdf.drawString(90, 610, f"   x = -{b} / (2*{a})")
                pdf.drawString(90, 590, f"   x = {-b / (2*a)}")
            else:
                pdf.drawString(70, 670, "2. Since the discriminant is negative, the equation has no real solutions.")

            pdf.drawString(50, 520, "")

            if solution:
                pdf.drawString(50, 500, "Solution:")
                pdf.drawString(70, 480, f"   x = {', '.join(str(s) for s in solution)}")
            else:
                pdf.drawString(50, 500, "No real solutions")

            pdf.showPage()

        pdf.save()

# Create an instance of the QuadraticEquationSolver class
solver = QuadraticEquationSolver(num_equations=20, filename="quadratic_solutions.pdf")

# Generate and solve the equations
solver.generate_and_solve_equations()

# Write the solutions to a PDF file
solver.write_solutions_to_pdf()
