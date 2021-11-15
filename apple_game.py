#   a123_apple_1.py
import turtle as trtl
import random as rand
#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
pear_image = "pear.gif"

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) 
wn.addshape(pear_image)

wn.bgpic("background.gif")
apple = trtl.Turtle()
appl = trtl.Turtle()
app = trtl.Turtle()
ap = trtl.Turtle()
a = trtl.Turtle()

drawer = trtl.Turtle()
drawer.hideturtle()

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
the_letter = rand.choice(letters)
the_letter_two = rand.choice(letters)
the_letter_three = rand.choice(letters)
the_letter_four = rand.choice(letters)
the_letter_five = rand.choice(letters)

#-----functions-----
def setup():
  apple.penup()
  appl.penup()
  app.penup()
  ap.penup()
  a.penup()

  apple.goto(rand.randint(-150, 150), rand.randint(0, 150))
  appl.goto(rand.randint(-150, 150), rand.randint(0, 150))
  app.goto(rand.randint(-150, 150), rand.randint(0, 150))
  ap.goto(rand.randint(-150, 150), rand.randint(0, 150))
  a.goto(rand.randint(-150, 150), rand.randint(0, 150))

def draw_turtle(active_apple, active_gif):
  active_apple.shape(active_gif)
  wn.update()

def draw_letter(which_letter):
  drawer.color("white")
  drawer.write(which_letter, font=("Arial", 74, "bold")) 

#-----apple functions----
def apple_fall():
  drawer.clear()
  apple.penup()
  apple.goto(0, -200)
  apple.hideturtle()
  draw_letter(the_letter_two)

def appl_fall():
  drawer.clear()
  appl.penup()
  appl.goto(0, -200)
  appl.hideturtle()
  draw_letter(the_letter_three)

def app_fall():
  drawer.clear()
  app.penup()
  app.goto(0, -200)
  app.hideturtle()
  draw_letter(the_letter_four)

def ap_fall():
  drawer.clear()
  ap.penup()
  ap.goto(0, -200)
  ap.hideturtle()
  draw_letter(the_letter_five)

def a_fall():
  drawer.clear()
  a.penup()
  a.goto(0, -200)
  a.hideturtle()

#-----function calls-----
draw_turtle(apple, apple_image)
draw_turtle(appl, apple_image)
draw_turtle(app, apple_image)
draw_turtle(ap, apple_image)
draw_turtle(a, apple_image)

setup()

draw_letter(the_letter)
wn.onkeypress(apple_fall, the_letter)
wn.onkeypress(appl_fall, the_letter_two)
wn.onkeypress(app_fall, the_letter_three)
wn.onkeypress(ap_fall, the_letter_four)
wn.onkeypress(a_fall, the_letter_five)

wn.listen()
wn.mainloop()