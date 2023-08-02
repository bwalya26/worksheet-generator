from django.shortcuts import render
from .models import Algebra
from Aplus.indices import Evaluate, Simplify
#from Aplus.matrices import MatrixQuestionGenerator
from django.http import HttpResponse
import random
import numpy as np
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.views import View

import random, string, math
import IPython
from IPython.display import display
import sympy
from sympy import *
from sympy.abc import a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z
from sympy import evaluate
import contextlib
from contextlib import redirect_stdout

# Create your views here.
def index(request):
    topics = Algebra.objects.all()
    context = {'topics': topics}
    return render(request, 'Aplus/index.html', context)


def evaluate(request):
    file1 = HttpResponse(content_type='application/html')
    file1['Content-Disposition'] = 'attchment; filename="Evaluate.html"'

    for m in range(0, 6):
        random_list = [x**2 for x in range(2, 15)]
        random_lits = [x**3 for x in range(2, 10)]
        random_lists = [x for x in range(1, 15) ]
        random_sign = ["-", "-", "-"]
        
        a = random.choice(random_list)
        b = random.choice(random_lits)
        c = random.choice(random_lists)
        d = random.choice(random_sign)
        e = random.choice(random_lits)
        f = random.choice(random_lists)
        
        new_expression = Evaluate(a, b, c, d, e, f)
        file1.write("<div>\n")
        file1.write(f"<h3>Problem {m + 1}</h3>")
        
        solutions = [ ]
        
        
        
        """QUESTION 1"""
        file1.write(f"<p><strong>1</strong>.&nbspEvaluate &nbsp:  &nbsp\
        {new_expression.signs()}{new_expression.coeffient_three()}<sup>2</sup> + {new_expression.coeffient_five()}<sup>2</sup>  </p>" )
        
        #solution
        file1.write(f"<p><strong>workings</strong> <br> &nbsp &nbsp\
        &nbsp&nbsp-1 x ({new_expression.coeffient_three()} x {new_expression.coeffient_three()})  =  {str(-1*new_expression.coeffient_three() * new_expression.coeffient_three())}<br> &nbsp &nbsp\
        &nbsp&nbsp{new_expression.coeffient_five()} x {new_expression.coeffient_five()}  =  {str(new_expression.coeffient_five() * new_expression.coeffient_five())}<br> &nbsp &nbsp\
        &nbsp&nbspAdding the two numbers gives {str((-1*new_expression.coeffient_three() * new_expression.coeffient_three()) + (new_expression.coeffient_five() * new_expression.coeffient_five()))} </p>")

            
        """QUESTION 2"""
        file1.write(f"<p><strong>2</strong>.&nbspEvaluate &nbsp:  &nbsp\
        {new_expression.coeffient_one()}<sup>1&nbsp&frasl;<sub>2<sub></sup> + \
        {new_expression.coeffient_three()} </p>" )
        
        #solution
        file1.write(f"<p><strong>workings</strong> <br> &nbsp &nbsp\
        &nbsp&nbspThis means square root: {new_expression.coeffient_one()}<sup>1&nbsp&frasl;<sub>2<sub></sup> = {str(int(math.sqrt(new_expression.coeffient_one())))}<br> &nbsp &nbsp\
        &nbsp&nbsp{str(int(math.sqrt(new_expression.coeffient_one())))} + {str(int(new_expression.coeffient_three()))} = {str(int(math.sqrt(new_expression.coeffient_one()) + new_expression.coeffient_three()))}   </p>" )
        
        """QUESTION 3"""
        file1.write(f"<p><strong>3</strong>.&nbspEvaluate &nbsp:  &nbsp\
        ({new_expression.coeffient_two()}&nbsp&frasl;&nbsp{new_expression.coeffient_four()})<sup>1&nbsp&frasl;&nbsp<sub>3<sub></sup> </p>" )
        
        #solution
        file1.write(f"<p><strong>workings</strong> <br> &nbsp &nbsp\
        &nbsp&nbspThis means cube root: {new_expression.coeffient_two()}<sup>1&nbsp&frasl;<sub>3<sub></sup> = {str(int(round(new_expression.coeffient_two()**(1/3), 1)))}<br> &nbsp &nbsp\
        &nbsp&nbspThis means cube root: {new_expression.coeffient_four()}<sup>1&nbsp&frasl;<sub>3<sub></sup> = {str(int(round(new_expression.coeffient_four()**(1/3), 1)))}<br> &nbsp &nbsp\
        &nbsp&nbspThe solution is = {str(int(round(new_expression.coeffient_two()**(1/3), 1)))}&nbsp &frasl; &nbsp{str(int(round(new_expression.coeffient_four()**(1/3), 1)))} </p>" )
        
        
        """QUESTION 4"""
        file1.write(f"<p><strong>4</strong>.Evaluate &nbsp:  &nbsp\
        ({new_expression.signs()}{new_expression.coeffient_three()}) &nbsp x  &nbsp{new_expression.coeffient_five()}<sup>2</sup> </p>" )
        
        #solution
        file1.write(f"<p><strong>answer</strong>&nbsp:  &nbsp\
        &nbsp&nbsp{str(-1*new_expression.coeffient_three()*new_expression.coeffient_five()**2)} </p>" )
        
        
        """QUESTION 5"""
        file1.write(f"<p><strong>5</strong>.&nbspEvaluate &nbsp:  &nbsp\
        {new_expression.coeffient_two()}<sup>2&nbsp&frasl;<sub>3<sub></sup> </p>" )
        
        #solution
        file1.write(f"<p><strong>workings</strong> <br> &nbsp &nbsp\
        &nbsp&nbspWe take the cube root of: {new_expression.coeffient_two()} = {str(int(round(new_expression.coeffient_two()**(1/3), 1)))}<br> &nbsp &nbsp\
        &nbsp&nbspThen we sqaure:  {str(int(round(new_expression.coeffient_two()**(1/3), 1)))} = {str(int(round(new_expression.coeffient_two()**(2/3), 1)))}<br> &nbsp &nbsp\
        &nbsp&nbspThe answer is then: {str(int(round(new_expression.coeffient_two()**(2/3), 1)))} </p>" )
        
         
        """QUESTION 6"""
        file1.write(f"<p><strong>6</strong>.&nbspSolve the equation &nbsp &nbsp\
        &#8730;{new_expression.coeffient_four()} &nbsp=&nbsp {new_expression.coeffient_four()}<sup>x</sup>  </p>" )
        
        #solution
        file1.write(f"<p><strong>workings</strong>&nbsp: <br> &nbsp\
        &nbsp&nbsp&#8730;{new_expression.coeffient_four()} = {new_expression.coeffient_four()}<sup>1&nbsp&frasl;<sub>2<sub></sup><br> &nbsp\
        &nbsp&nbspThen&nbsp{new_expression.coeffient_four()}<sup>1&nbsp&frasl;<sub>2<sub></sup> &nbsp=&nbsp {new_expression.coeffient_four()}<sup>x</sup><br> &nbsp\
        &nbsp&nbspSince we have the same base, we equity the roots or powers together <br> &nbsp\
        &nbsp&nbsp1&nbsp&frasl;&nbsp2 = x  &nbsp or &nbsp x = 1&nbsp&frasl;&nbsp2 </p>" )
        
        """QUESTION 7"""
        file1.write(f"<p><strong>7</strong>.&nbspSolve the equation&nbsp &nbsp\
        {str(new_expression.coeffient_three()**3)}<sup>x</sup> &nbsp=&nbsp 1&nbsp&frasl;&nbsp{str(new_expression.coeffient_three()**2)} </p>" )
        
        #solution
        file1.write(f"<p><strong>workings</strong> &nbsp: <br> &nbsp\
        &nbsp&nbspwe make the the two sides have the same base  &nbsp: <br> &nbsp\
        &nbsp&nbsp{str(new_expression.coeffient_three()**3)}<sup>x</sup> &nbsp=&nbsp{str(int(round((new_expression.coeffient_three()**3)**(1/3))))}<sup>3x</sup><br> &nbsp\
        &nbsp&nbsp1&nbsp&frasl;&nbsp{str(new_expression.coeffient_three()**2)} &nbsp=&nbsp{str(int(round((new_expression.coeffient_three()**2)**(1/2))))}<sup>-2</sup><br> &nbsp\
        &nbsp&nbspSince we have the same base, we equity the roots or powers together <br> &nbsp\
        &nbsp&nbsp3x &nbsp=&nbsp -2 <br> &nbsp\
        &nbsp&nbspx = -2&nbsp&frasl;&nbsp3</p>" )
        
        
        file1.write("<br>\n")
        file1.write("</div>")
    file1.close()

    
    return file1

def simplify(request):
    file1 = HttpResponse(content_type='application/html')
    file1['Content-Disposition'] = 'attchment; filename="Simplify.html"'

    for m in range(0, 45):
        random_list = [x for x in range(2, 5)]
        random_list2 = [x**2 for x in random_list]
        keys = random_list
        values = random_list
        random_list3 = {k:v for (k,v) in zip(keys,values)}
        random_term = ["xy", "x<sup>2</sup>", "x<sup>2</sup>y", "xy<sup>2</sup>", "y<sup>2</sup>",  "x", "y"]
        random_term2 = [x*y, x**2, x**2*y, x*y**2, y**2,  x, y]
        
        a = random.choice(random_list)
        b = random.choice(random_list)
        c = random.choice(random_list)
        d = random.choice(random_list)
        e = random.choice(random_list)
        
        f = random.choice(random_term)
        g = random.choice(random_term)
        h = random.choice(random_term)
        i = random.choice(random_term)
        j = random.choice(random_term)
        
        k = random.choice(random_list)
        l = random.choice(random_list)
        m = random.choice(random_list2)
        n = random.choice(random_list2)
        o = random.choice(random_list2)
          
        
        new_equation = Simplify(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o)
        file1.write("<div>\n")
        #file1.write(f"<h3>Problem {m + 1}</h3>")
        
        """QUESTION 1"""
        file1.write(f"<p>Simplify &nbsp:  &nbsp\
        {new_equation.coeffient_one()}y - \
        {new_equation.coeffient_two()}({new_equation.term_one()} - {new_equation.coeffient_three()}) - {new_equation.term_one()} </p>" )
        
        """QUESTION 2"""
        file1.write(f"<p>Simplify &nbsp: &nbsp\
        {new_equation.coeffient_three()}{new_equation.term_one()} + {new_equation.term_two()} - \
        {new_equation.coeffient_four()}{new_equation.term_one()} - {new_equation.term_two()} + {new_equation.coeffient_four()}{new_equation.term_two()}</p>" )
        
        """QUESTION 3"""
        file1.write(f"<p>Simplify &nbsp: &nbsp\
        {new_equation.coeffient_three()}{new_equation.term_one()} + {new_equation.term_two()} - \
        ({new_equation.coeffient_four()}{new_equation.term_two()} + {new_equation.coeffient_two()}{new_equation.term_one()})</p>" )
        
        """QUESTION 4"""
        file1.write(f"<p>Simplify &nbsp: &nbsp\
        {new_equation.coeffient_three()}{new_equation.term_two()}({new_equation.coeffient_one()}{new_equation.term_one()}  - \
        {new_equation.coeffient_one()}) + {new_equation.term_two()}</p>" )
        
        """QUESTION 5"""
        file1.write(f"<p>Simplify &nbsp: &nbsp\
        (<sup>a -  {new_equation.coeffient_five()})</sup>&frasl;\
        <sub>a<sup>2</sup> + {new_equation.coeffient_six()}</sub></p>" )
        
        
        """QUESTION 6"""
        file1.write(f"<p>Solve the equation &nbsp: &nbsp\
        ({new_equation.coeffient_three()}x - {new_equation.coeffient_one()})(x + {new_equation.coeffient_two()}) = 0</p>" )
        
        """QUESTION 7"""
        file1.write(f"<p>Factorise completly &nbsp: &nbsp\
        {new_equation.coeffient_four()}x<sup>3</sup> - {new_equation.constant_term()}xy<sup>2</sup></p>" )
        
        file1.write("<br>\n")
        file1.write("</div>")
        
    file1.close()
    return file1


class MatrixQuestionGenerator(View):
    def generate_transpose_question(self):
        matrix = np.random.randint(1, 10, size=(3, 3))
        question = f"What is the transpose of the matrix:\n{matrix}?"
        answer = np.transpose(matrix)
        print(matrix)
        print(question)
        print(answer)
        return question, answer

    def generate_multiplication_question(self):
        matrix1 = np.random.randint(1, 10, size=(2, 2))
        matrix2 = np.random.randint(1, 10, size=(2, 2))
        question = f"What is the result of multiplying the matrices:\n{matrix1}\nand\n{matrix2}?"
        answer = np.dot(matrix1, matrix2)
        print(matrix1)
        print(matrix2)
        print(answer)
        print(answer)
        print(question)
        print(answer)
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
        question_types = [
            self.generate_transpose_question,
            self.generate_multiplication_question,
            self.generate_determinant_question,
            self.generate_inverse_question
        ]
        question_func = random.choice(question_types)
        return question_func()

    def solve_question(self, question, user_answer):
        if isinstance(user_answer, np.ndarray):
            return np.array_equal(question[1], user_answer)
        return question[1] == user_answer

    def show_solution(self, question, answer):
        solution = f"Solution:\n{answer}"
        return solution

    def generate_and_solve_questions(self, num_questions):
        pdf = canvas.Canvas("matrix_questions.pdf")
        for i in range(num_questions):
            question, answer = self.generate_question()
            pdf.setFont("Helvetica-Bold", 14)
            pdf.drawString(50, pdf._pagesize[1] - 50, f"Question {i+1}:")
            pdf.setFont("Helvetica", 12)
            pdf.drawString(50, pdf._pagesize[1] - 75, question)
            user_answer = input("Enter your answer: ")
            is_correct = self.solve_question(question, user_answer)
            if is_correct:
                pdf.setFont("Helvetica-Bold", 12)
                pdf.drawString(50, pdf._pagesize[1] - 100, "Correct!")
            else:
                pdf.setFont("Helvetica-Bold", 12)
                pdf.drawString(50, pdf._pagesize[1] - 100, "Incorrect.")
                solution = self.show_solution(question, question[1])
                pdf.setFont("Helvetica", 12)
                pdf.drawString(50, pdf._pagesize[1] - 150, solution)

            pdf.showPage()

        pdf.save()
        return "matrix_questions.pdf"

    def get(self, request):
        num_questions = 20
        pdf_filename = self.generate_and_solve_questions(num_questions)
        with open(pdf_filename, "rb") as pdf_file:
            response = HttpResponse(pdf_file.read(), content_type="application/pdf")
            response["Content-Disposition"] = 'attchment; filename="matrices.pdf"'
            return response
