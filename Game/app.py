import time
import turtle

# Setup Screen
wn = turtle.Screen()
wn.title("Physics Game")
wn.setup(width=500, height=500)
wn.bgcolor("white")
wn.tracer(0)

class Sprite:
    def __init__(self, x, y, color, shape, base):
        self.pen = turtle.Turtle()
        self.pen.penup()
        self.pen.shape(shape)
        self.pen.color(color)
        
        self.x = x
        self.y = y
        self.base = base
        
        self.dy = 0
        self.pen.goto(self.x, self.y)

    def jump(self):
        if self.y == self.base:
            self.dy = 10  # Jump height adjusted for 60 FPS

    def move_left(self):
        self.x -= 8

    def move_right(self):
        self.x += 8

    def update(self):
        # Apply Gravity
        if self.y > self.base or self.dy > 0:
            self.dy -= 0.5  # Gravity strength per frame
            self.y += self.dy

        # Base / Ground Collision
        if self.y <= self.base:
            self.y = self.base
            self.dy = 0

        # Boundary Collisions
        if self.x > 230:
            self.x = 230
        elif self.x < -230:
            self.x = -230

        if self.y > 230:
            self.y = 230

        self.pen.goto(self.x, self.y)

# Initialize Player
player = Sprite(0, -200, "blue", "triangle", -200)

# Keyboard Controls
wn.listen()
wn.onkeypress(player.jump, "Up")
wn.onkeypress(player.move_left, "Left")
wn.onkeypress(player.move_right, "Right")

# Main Game Loop (Targeting ~60 FPS)
FPS = 83
frame_delay = 1 / FPS

while True:
    start_time = time.time()
    
    player.update()
    wn.update()
    
    # Calculate sleep duration to lock frame rate
    elapsed = time.time() - start_time
    if frame_delay > elapsed:
        time.sleep(frame_delay - elapsed)