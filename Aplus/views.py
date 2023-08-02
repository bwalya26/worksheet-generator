from django.shortcuts import render
from .models import Algebra
from Aplus.indices import Evaluate, Simplify, QuadraticEquationSolver
#from Aplus.matrices import MatrixQuestionGenerator
from django.http import HttpResponse
import random
import numpy as np
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.views import View
import sympy as sp
import math, numexpr

import random, string, math
import IPython
from IPython.display import display
import sympy
from sympy import *
from sympy.abc import a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z
from sympy import evaluate,  parse_expr
import contextlib
from contextlib import redirect_stdout

import random
import turtle
from django.http import HttpResponse
from django.template import loader
from PIL import Image
import imgkit
import io

# Create your views here.
def index(request):
    topics = Algebra.objects.all()
    context = {'topics': topics}
    return render(request, 'Aplus/index.html', context)


def evaluate(request):
    file1 = HttpResponse(content_type='application/html')
    file1['Content-Disposition'] = 'attachment; filename="Evaluate.html"'

    # Add inline CSS for increasing font size
    file1.write("<style>")
    file1.write("body {font-size: 18px; background-color: #f2f2f2; color: #000000;}")
    file1.write("div {background-color: #dddddd; padding: 10px; margin: 10px;}")
    file1.write("p {margin-bottom: 8px;}")
    file1.write("</style>\n")


    for m in range(0, 6):
        random_list = [x**2 for x in range(2, 15)]
        random_lits = [x**3 for x in range(2, 10)]
        random_lists = [x for x in range(1, 15)]
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

        solutions = []

        """QUESTION 1"""
        file1.write(f"<p><strong>1</strong>.&nbspEvaluate &nbsp:  &nbsp\
        {new_expression.signs()}{new_expression.coeffient_three()}<sup>2</sup> + {new_expression.coeffient_five()}<sup>2</sup>  </p>")

        # solution
        file1.write(f"<p><strong>workings</strong> <br> &nbsp &nbsp\
        &nbsp&nbsp-1 x ({new_expression.coeffient_three()} x {new_expression.coeffient_three()})  =  {str(-1*new_expression.coeffient_three() * new_expression.coeffient_three())}<br> &nbsp &nbsp\
        &nbsp&nbsp{new_expression.coeffient_five()} x {new_expression.coeffient_five()}  =  {str(new_expression.coeffient_five() * new_expression.coeffient_five())}<br> &nbsp &nbsp\
        &nbsp&nbspAdding the two numbers gives {str((-1*new_expression.coeffient_three() * new_expression.coeffient_three()) + (new_expression.coeffient_five() * new_expression.coeffient_five()))} </p>")

        """QUESTION 2"""
        file1.write(f"<p><strong>2</strong>.&nbspEvaluate &nbsp:  &nbsp\
        {new_expression.coeffient_one()}<sup>1&nbsp&frasl;<sub>2<sub></sup> + \
        {new_expression.coeffient_three()} </p>")

        # solution
        file1.write(f"<p><strong>workings</strong> <br> &nbsp &nbsp\
        &nbsp&nbspThis means square root: {new_expression.coeffient_one()}<sup>1&nbsp&frasl;<sub>2<sub></sup> = {str(int(math.sqrt(new_expression.coeffient_one())))}<br> &nbsp &nbsp\
        &nbsp&nbsp{str(int(math.sqrt(new_expression.coeffient_one())))} + {str(int(new_expression.coeffient_three()))} = {str(int(math.sqrt(new_expression.coeffient_one()) + new_expression.coeffient_three()))}   </p>")

        """QUESTION 3"""
        file1.write(f"<p><strong>3</strong>.&nbspEvaluate &nbsp:  &nbsp\
        ({new_expression.coeffient_two()}&nbsp&frasl;&nbsp{new_expression.coeffient_four()})<sup>1&nbsp&frasl;&nbsp<sub>3<sub></sup> </p>")

        # solution
        file1.write(f"<p><strong>workings</strong> <br> &nbsp &nbsp\
        &nbsp&nbspThis means cube root: {new_expression.coeffient_two()}<sup>1&nbsp&frasl;<sub>3<sub></sup> = {str(int(round(new_expression.coeffient_two()**(1/3), 1)))}<br> &nbsp &nbsp\
        &nbsp&nbspThis means cube root: {new_expression.coeffient_four()}<sup>1&nbsp&frasl;<sub>3<sub></sup> = {str(int(round(new_expression.coeffient_four()**(1/3), 1)))}<br> &nbsp &nbsp\
        &nbsp&nbspThe solution is = {str(int(round(new_expression.coeffient_two()**(1/3), 1)))}&nbsp &frasl; &nbsp{str(int(round(new_expression.coeffient_four()**(1/3), 1)))} </p>")

        """QUESTION 4"""
        file1.write(f"<p><strong>4</strong>.Evaluate &nbsp:  &nbsp\
        ({new_expression.signs()}{new_expression.coeffient_three()}) &nbsp x  &nbsp{new_expression.coeffient_five()}<sup>2</sup> </p>")

        # solution
        file1.write(f"<p><strong>answer</strong>&nbsp:  &nbsp\
        &nbsp&nbsp{str(-1*new_expression.coeffient_three()*new_expression.coeffient_five()**2)} </p>")

        """QUESTION 5"""
        file1.write(f"<p><strong>5</strong>.&nbspEvaluate &nbsp:  &nbsp\
        {new_expression.coeffient_two()}<sup>2&nbsp&frasl;<sub>3<sub></sup> </p>")

        # solution
        file1.write(
            f"<p><strong>workings</strong> <br> &nbsp &nbsp\
            &nbsp&nbspWe take the cube root of: {new_expression.coeffient_two()} = {str(int(round(new_expression.coeffient_two()**(1/3), 1)))}<br> &nbsp &nbsp\
            &nbsp&nbspThen we square:  {str(int(round(new_expression.coeffient_two()**(1/3), 1)))} = {str(int(round(new_expression.coeffient_two()**(2/3), 1)))}<br> &nbsp &nbsp\
            &nbsp&nbspThe answer is then: {str(int(round(new_expression.coeffient_two()**(2/3), 1)))} </p>")

        """QUESTION 6"""
        file1.write(f"<p><strong>6</strong>.&nbspSolve the equation &nbsp &nbsp\
        &#8730;{new_expression.coeffient_four()} &nbsp=&nbsp {new_expression.coeffient_four()}<sup>x</sup>  </p>")

        # solution
        file1.write(
            f"<p><strong>workings</strong>&nbsp: <br> &nbsp\
            &nbsp&nbsp&#8730;{new_expression.coeffient_four()} = {new_expression.coeffient_four()}<sup>1&nbsp&frasl;<sub>2<sub></sup><br> &nbsp\
            &nbsp&nbspThen&nbsp{new_expression.coeffient_four()}<sup>1&nbsp&frasl;<sub>2<sub></sup> &nbsp=&nbsp {new_expression.coeffient_four()}<sup>x</sup><br> &nbsp\
            &nbsp&nbspSince we have the same base, we equate the roots or powers together <br> &nbsp\
            &nbsp&nbsp1&nbsp&frasl;&nbsp2 = x  &nbsp or &nbsp x = 1&nbsp&frasl;&nbsp2 </p>")

        """QUESTION 7"""
        file1.write(
            f"<p><strong>7</strong>.&nbspSolve the equation&nbsp &nbsp\
            {str(new_expression.coeffient_three()**3)}<sup>x</sup> &nbsp=&nbsp 1&nbsp&frasl;&nbsp{str(new_expression.coeffient_three()**2)} </p>")

        # solution
        file1.write(
            f"<p><strong>workings</strong> &nbsp: <br> &nbsp\
            &nbsp&nbspwe make the two sides have the same base  &nbsp: <br> &nbsp\
            &nbsp&nbsp{str(new_expression.coeffient_three()**3)}<sup>x</sup> &nbsp=&nbsp{str(int(round((new_expression.coeffient_three()**3)**(1/3))))}<sup>3x</sup><br> &nbsp\
            &nbsp&nbsp1&nbsp&frasl;&nbsp{str(new_expression.coeffient_three()**2)} &nbsp=&nbsp{str(int(round((new_expression.coeffient_three()**2)**(1/2))))}<sup>-2</sup><br> &nbsp\
            &nbsp&nbspSince we have the same base, we equate the roots or powers together <br> &nbsp\
            &nbsp&nbsp3x &nbsp=&nbsp -2 <br> &nbsp\
            &nbsp&nbspx = -2&nbsp&frasl;&nbsp3</p>")

        file1.write("<br>\n")
        file1.write("</div>")
    file1.close()

    return file1

    
    return file1

def simplify(request):
    file1 = HttpResponse(content_type='application/html')
    file1['Content-Disposition'] = 'attchment; filename="Simplify.html"'

    # Add inline CSS for increasing font size
    file1.write("<style>")
    file1.write("body {font-size: 18px; background-color: #f2f2f2; color: #000000;}")
    file1.write("div {background-color: #dddddd; padding: 10px; margin: 10px;}")
    file1.write("p {margin-bottom: 8px;}")
    file1.write("</style>\n")


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
        a = random.randint(3, 10)
        b =  a*a

        numerator = f"x - {a}"
        denominator = f"x<sup>2</sup> - {b}"

        file1.write(f"<p>Simplify &nbsp: &nbsp\
        ({numerator})&nbsp&frasl;&nbsp({denominator})</p>")

        
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



def generate_quadratic_equation(request):
    file1 = HttpResponse(content_type='application/html')
    file1['Content-Disposition'] = 'attachment; filename="Quadratics.html"'

    # Add inline CSS for increasing font size
    file1.write("<style>")
    file1.write("body {font-size: 18px; background-color: #f2f2f2; color: #000000;}")
    file1.write("div {background-color: #dddddd; padding: 10px; margin: 10px;}")
    file1.write("p {margin-bottom: 8px;}")
    file1.write("</style>\n")


    for m in range(0, 15):
        has_real_solution = False

        while not has_real_solution:
            a = random.randint(2, 10)
            b = random.randint(2, 10)
            c = random.randint(2, 10)

            discriminant = b ** 2 - 4 * a * c

            if discriminant >= 0 and a != 0:
                has_real_solution = True
                quadratics = QuadraticEquationSolver(a, b, c)

                file1.write("<div>\n")

                file1.write(f"<p>&nbsp\
                {quadratics.coefficient_1()}x<sup>2</sup> + {quadratics.coefficient_2()}x + {quadratics.coefficient_3()} = 0&nbsp\
                <ul>&nbsp\
                <li>Determine the coefficient values (a, b, c) from the equation.</li>&nbsp\
                <li>a = {quadratics.coefficient_1()}, b = {quadratics.coefficient_2()}, c = {quadratics.coefficient_3()}</li>&nbsp\
                <li>Apply the quadratic formula to find the solutions.</li>&nbsp\
                <li>Note: Calculate the discriminant (b² - 4ac) first.</li>&nbsp\
                <li>The discriminant is {discriminant}</li>\
                </ul>\
                </p>")

                if discriminant == 0:
                    root = -quadratics.coefficient_2() / (2 * quadratics.coefficient_1())
                    file1.write(f"<li>The equation has a single real root: {root}</li>&nbsp\
                    ")
                else:
                    root1 = (-quadratics.coefficient_2() + math.sqrt(discriminant)) / (2 * quadratics.coefficient_1())
                    root2 = (-quadratics.coefficient_2() - math.sqrt(discriminant)) / (2 * quadratics.coefficient_1())
                    file1.write(f"<li>The equation has two real roots: {root1} and {root2}</li>&nbsp\
                    ")
                file1.write("</div>\n")

    file1.close()
    return file1

from django.http import HttpResponse
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from PIL import Image, ImageDraw, ImageFont
import random

# Function to calculate the velocity at a given time
def calculate_velocity(time, total_time):
    if time <= 5:
        acceleration = (24 - 4) / 5  # Accelerating phase
        velocity = 4 + acceleration * time
    elif time <= 10:
        velocity = 24  # Constant velocity phase
    else:
        deceleration = -24 / (total_time - 10)  # Decelerating phase
        velocity = 24 + deceleration * (time - 10)
    return velocity

# Function to draw the velocity-time graph using Pillow
def draw_velocity_time_graph(total_time):
    width = 800
    height = 600
    initial_velocity = random.randint(1, 10)
    constant_velocity = random.randint(25, 40)  # Ensuring constant_velocity is greater than 24
    intial_time = random.randint(3, 9)
    deceleration_time = random.randint(10, 15)
    afterdece_time = random.randint(16, 19)
    
    

    # Create a blank image
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)

    # Draw x-axis (time)
    draw.line([(50, height - 50), (width - 50, height - 50)], fill="black", width=2)

    # Draw y-axis (velocity)
    draw.line([(50, height - 50), (50, 50)], fill="black", width=2)

    # Draw velocity axis labels
    font = ImageFont.truetype("arial.ttf", 12)
    draw.text((20, height - 97), str(initial_velocity), font=font, fill="black")
    draw.text((20, height - 300), str(constant_velocity), font=font, fill="black")
    draw.text((-15, 250), "speed(ms)", font=font, fill="black")

       
    # Generate random time axis labels
    time_labels = [0, intial_time, deceleration_time, afterdece_time, 't    Time(s)']
    x_axis_positions = [50, 50 + 5 * (width - 100) / total_time, 50 + 10 * (width - 100) / total_time, width - 275, width - 50]


    # Draw time axis labels
    for time_label, x_pos in zip(time_labels, x_axis_positions):
        draw.text((x_pos, height - 40), str(time_label), font=font, fill="black")

    # Draw the velocity-time graph with solid lines
    prev_point = None
    for time in range(int(total_time) + 1):
        velocity = calculate_velocity(time, total_time)
        x_pos = 50 + time * (width - 100) / total_time
        y_pos = height - 50 - velocity * 10

        if prev_point is not None:
            draw.line([prev_point, (x_pos, y_pos)], fill="blue", width=2)

        prev_point = (x_pos, y_pos)

    questions = [
        "The graph below shows the speed time graph of a moving object",
        "1. Find the acceleration of the object in the first 3 seconds.",
        "2. Given that the object decelerates at 3 m/s squared, find the value of t.",
        "3. Calculate the average speed of the object in the first 10 seconds.",
        "4. Calculate the distance traveled from the time the object started decelerating until it comes to rest.",
    ]

    y_pos = 30 # Y-position for the first question

    for question in questions:
        draw.text((80, y_pos), question, font=font, fill="black")
        y_pos += 50

    # Save the image to a file
    file_path = "velocity_time_graph.png"
    img.save(file_path)
    return file_path

def generate_graph(request):
    total_time = 20
    file_path = draw_velocity_time_graph(total_time)

    # Read the image file and return it as an attachment
    with open(file_path, "rb") as f:
        response = HttpResponse(f.read(), content_type="image/png")
        response["Content-Disposition"] = 'attachment; filename="velocity_time_graph.png"'
    default_storage.delete(file_path)  # Delete the image file from the server after sending it
    return response
