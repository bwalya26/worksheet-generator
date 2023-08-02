import turtle
import random

# Function to calculate the velocity at a given time
def calculate_velocity(time, total_time, initial_velocity, acceleration, constant_velocity_time):
    if time <= constant_velocity_time:
        velocity = initial_velocity + acceleration * time  # Accelerating phase
    elif time <= constant_velocity_time + 10:
        velocity = initial_velocity + acceleration * constant_velocity_time  # Constant velocity phase
    else:
        deceleration = acceleration  # Decelerating phase
        velocity = initial_velocity + acceleration * constant_velocity_time - deceleration * (time - constant_velocity_time - 10)
    return velocity

# Function to draw the velocity-time graph
def draw_velocity_time_graph(total_time, initial_velocity, acceleration, constant_velocity_time, start_with_acceleration=True):
    window = turtle.Screen()
    window.setup(width=800, height=600)
    window.title("Velocity-Time Graph using Turtle")
    window.bgcolor("white")

    graph_turtle = turtle.Turtle()
    graph_turtle.speed(0)

    # Draw x-axis (time)
    graph_turtle.penup()
    graph_turtle.goto(-300, -200)
    graph_turtle.pendown()
    graph_turtle.goto(300, -200)
    graph_turtle.penup()

    # Draw y-axis (velocity)
    graph_turtle.goto(-300, -200)
    graph_turtle.pendown()
    graph_turtle.goto(-300, 200)
    graph_turtle.penup()

    # Draw velocity axis labels
    graph_turtle.goto(-320, -160)
    graph_turtle.write(str(initial_velocity), font=("Arial", 12, "normal"))
    graph_turtle.goto(-320, 180)
    graph_turtle.write("24", font=("Arial", 12, "normal"))

    # Draw time axis labels
    time_labels = [0, constant_velocity_time, constant_velocity_time + 10, total_time]
    for time_label in time_labels:
        x_pos = time_label * (600 // total_time) - 300
        graph_turtle.goto(x_pos, -220)
        graph_turtle.write(str(time_label), font=("Arial", 12, "normal"))

    # Determine the starting phase (acceleration or deceleration)
    if start_with_acceleration:
        initial_velocity += acceleration * constant_velocity_time
    else:
        initial_velocity += acceleration * constant_velocity_time - acceleration * 10

    # Draw the velocity-time graph
    graph_turtle.penup()
    graph_turtle.goto(0, initial_velocity * constant_velocity_time - 200)  # Starting point
    graph_turtle.pendown()

    for time in range(int(total_time) + 1):
        velocity = calculate_velocity(time, total_time, initial_velocity, acceleration, constant_velocity_time)
        x_pos = time * (600 // total_time) - 300
        y_pos = velocity * 10 - 200
        graph_turtle.goto(x_pos, y_pos)
        graph_turtle.dot(5, "blue")

    graph_turtle.hideturtle()

    window.mainloop()

if __name__ == "__main__":
    # Generate random values for acceleration and constant_velocity_time
    acceleration = random.randint(1, 10)
    constant_velocity_time = random.randint(5, 10)

    # Calculate the total time based on constant_velocity_time and the decelerating phase
    total_time = constant_velocity_time + 10 + constant_velocity_time

    # Generate random boolean to determine the starting phase
    start_with_acceleration = random.choice([True, False])

    if start_with_acceleration:
        initial_velocity = random.randint(1, 10)
    else:
        initial_velocity = random.randint(25, 40)  # Ensure initial_velocity is greater than 24

    draw_velocity_time_graph(total_time, initial_velocity, acceleration, constant_velocity_time, start_with_acceleration)
