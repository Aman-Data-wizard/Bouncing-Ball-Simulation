import turtle
import time

# --- Setup the screen ---
screen = turtle.Screen()
screen.title("Bouncing Ball Simulation")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0) # Turns off screen updates

# --- Create the ball ---
ball = turtle.Turtle()
ball.speed(-1)
ball.shape("circle")
ball.color("green")
ball.shapesize(stretch_wid=3, stretch_len=3) # Ball size
ball.penup()
# Start near the top-left
ball.goto(-280, 200) 

# --- Simulation physics variables ---
ball.dy = 0 # Initial vertical speed (starts by falling)
ball.dx = 1 # Initial horizontal speed (the "throw" forwards)
gravity = -0.1 # A slightly stronger gravity for a better arc
bounce_dampening = 0.85 # Energy loss on each bounce2
friction = 0.999 # Gradual horizontal slowdown

# --- Function to stop the ball on click ---
def stop_ball(x, y):
    """Stops the ball if the click is inside the ball."""
    # The ball's radius is approximately 20 pixels (shapesize 2 * 10)
    if ball.distance(x, y) < 20:
        ball.dx = 0
        ball.dy = 0
        ball.color("Red") # Change color to show it's stopped

# --- Bind the click event to the ball ---
ball.onclick(stop_ball)

# --- Main game loop ---
try:
    while True:
        screen.update() # Manually update the screen

        # Apply gravity to the vertical speed
        ball.dy += gravity

        # Apply friction to the horizontal speed
        ball.dx *= friction

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # --- Border checking and bouncing ---

        # Right border
        if ball.xcor() > 280:
            ball.setx(280)
            ball.dx *= -1

        # Left border
        if ball.xcor() < -280:
            ball.setx(-280)
            ball.dx *= -1
        
        # Top border
        if ball.ycor() > 280:
            ball.sety(280)
            ball.dy *= -1

        # Bottom border (the "ground")
        if ball.ycor() < -280:
            # Set position to the floor to prevent it from going through
            ball.sety(-280)
            
            # Reverse direction and apply dampening to lose energy
            ball.dy *= -bounce_dampening

            # If the bounce is too small, stop the ball completely (dead position)
            # This logic is now handled by the onclick event
            # if abs(ball.dy) < 2.5:
            #     ball.dy = 0
            #     ball.dx = 0


        # A small delay to control the animation speed
        time.sleep(0.01)

except turtle.Terminator:
    # This handles the error when the user closes the window
    pass


