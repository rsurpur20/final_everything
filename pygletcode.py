# Roshni and Ryan
# On my Honor
# Feb 20, 2019

import pyglet
from pyglet.window import key
from pyglet.window import mouse
from pyglet.window import Window
import random
import math

window = pyglet.window.Window(500, 500) #x, y

# LOADING THE SALAD
salad_image = pyglet.image.load('salad.png')
salad = pyglet.sprite.Sprite(salad_image, x=random.randint(0,window.width-100), y=window.height)
salad.scale=.3


# LOADING THE USER
user_image=pyglet.image.load('user.png')
user = pyglet.sprite.Sprite(user_image, x=random.randint(0,window.width), y=10)
user.scale=.4

moved=1000
# LOADING THE BANANA
banana_image=pyglet.image.load('banana .png')
banana = pyglet.sprite.Sprite(banana_image, x=random.randint(0,400), y=random.randint(window.height,window.height+moved))
banana.scale=.15


# LOADING THE PIZZA
pizza_image=pyglet.image.load('pizza.png')
pizza = pyglet.sprite.Sprite(pizza_image, x=random.randint(0,400), y=random.randint(window.height,window.height+moved))
pizza.scale=.2

# LOADING THE BURGER
burger_image=pyglet.image.load('burger.png')
burger = pyglet.sprite.Sprite(burger_image, x=random.randint(0,400), y=random.randint(window.height,window.height+moved))
burger.scale=.1

# LOADING THE SODA
soda_image=pyglet.image.load('soda.png')
soda = pyglet.sprite.Sprite(soda_image, x=random.randint(0,400), y=random.randint(window.height,window.height+moved))
soda.scale=.1

# LOADING THE WATER
water_image=pyglet.image.load('water.png')
water = pyglet.sprite.Sprite(water_image, x=random.randint(0,400), y=random.randint(window.height,window.height+moved))
water.scale=.4


# LOADING THE FRENCH FRY
frenchfry_image=pyglet.image.load('frenchfry.png')
frenchfry = pyglet.sprite.Sprite(frenchfry_image, x=random.randint(0,400), y=random.randint(window.height,window.height+moved))
frenchfry.scale=.1


# changing all the anchors, this is the point at which the picture con rotate around
salad.anchor_x = salad.width // 2
salad.anchor_y = salad.height // 2
user.anchor_x = user.width // 2
user.anchor_y = user.height // 2
banana.anchor_x = banana.width // 2
banana.anchor_y = banana.height // 2
pizza.anchor_x = pizza.width // 2
pizza.anchor_y = pizza.height // 2
burger.anchor_x = burger.width // 2
burger.anchor_y = burger.height // 2
soda.anchor_x = soda.width // 2
soda.anchor_y = soda.height // 2
water.anchor_x = water.width // 2
water.anchor_y = water.height // 2
frenchfry.anchor_x = frenchfry.width // 2
frenchfry.anchor_y = frenchfry.height // 2
collisiondistancex=salad.width/2+user.width/2
collisiondistancey=salad.height/2+user.height/2
bananadistancex=banana.width/2+user.width/2
bananadistancey=banana.height/2+user.height/2
pizzadistancex=pizza.width/2+user.width/2
pizzadistancey=pizza.height/2+user.height/2
burgerdistancex=burger.width/2+user.width/2
burgerdistancey=burger.height/2+user.height/2
sodadistancex=soda.width/2+user.width/2
sodadistancey=soda.height/2+user.height/2
waterdistancex=water.width/2+user.width/2
waterdistancey=water.height/2+user.height/2
frenchfrydistancex=frenchfry.width/2+user.width/2
frenchfrydistancey=frenchfry.height/2+user.height/2

score=0
time=10 #given 90 seconds

# this is as soon as the user begins the game
@window.event
def on_key_press(symbol, modifiers):
    global score, time, salad, user, water, frenchfry, soda, pizza, burger, banana

    if symbol == key.LEFT and user.x>0:
    # if user presses left
        user.x-=50
    if symbol == key.RIGHT and user.x<window.width-50:
    # if user presses right
        user.x+=50
    if symbol == key.ENTER:
        def update(dt): #this is for moving all the images down the screen
            salad.y -= dt * 125
            if salad.y<0:
                salad.set_position(random.randint(0,window.width-100),window.height) #reset the position
            frenchfry.y -= dt * 110
            if frenchfry.y<0:
                frenchfry.set_position(random.randint(0,400),random.randint(window.height,window.height+moved))#reset the position
            water.y -= dt * 110
            if water.y<0:
                water.set_position(random.randint(0,400),random.randint(window.height,window.height+moved))#reset the position
            soda.y -= dt * 110
            if soda.y<0:
                soda.set_position(random.randint(0,400),random.randint(window.height,window.height+moved))#reset the position
            burger.y -= dt * 70
            if burger.y<0:
                burger.set_position(random.randint(0,400),random.randint(window.height,window.height+moved))#reset the position
            pizza.y -= dt * 100
            if pizza.y<0:
                pizza.set_position(random.randint(0,400),random.randint(window.height,window.height+moved))#reset the position
            banana.y -= dt * 150
            if banana.y<0:
                banana.set_position(random.randint(0,400),random.randint(window.height,window.height+moved))#reset the position
        pyglet.clock.schedule_interval(update, 1/10)

        # this is to draw all the images on the window
        @window.event
        def on_draw():
            window.clear()
            salad.draw()
            user.draw()
            banana.draw()
            pizza.draw()
            burger.draw()
            soda.draw()
            water.draw()
            frenchfry.draw()

            # score and time
            global score, time
            score_label = pyglet.text.Label('Score:'+str(score),
                                      font_name='Times New Roman',
                                      font_size=36,
                                      x=10, y=window.height-30,
                                     )
            score_label.draw()
            time_label = pyglet.text.Label('Time:'+str(time/10),
                                      font_name='Times New Roman',
                                      font_size=36,
                                      x=10, y=window.height-70,
                                     )
            time-=1
            time_label.draw()
            # collison with salad
            if 0<=abs(user.x-salad.x)<=collisiondistancex and 0<=abs(user.y-salad.y)<=collisiondistancey:
                    score+=10
            # collison with pizza
            if 0<=abs(user.x-pizza.x)<=pizzadistancex and 0<=abs(user.y-pizza.y)<=pizzadistancey:
                    score-=10
                    user.draw()
            # collison with banana
            if 0<=abs(user.x-banana.x)<=bananadistancex and 0<=abs(user.y-banana.y)<=bananadistancey:
                    score+=10
                    user.draw()
            # collison with burger
            if 0<=abs(user.x-burger.x)<=burgerdistancex and 0<=abs(user.y-burger.y)<=burgerdistancey:
                    score-=10
                    user.draw()
            # collison with soda
            if 0<=abs(user.x-soda.x)<=sodadistancex and 0<=abs(user.y-soda.y)<=sodadistancey:
                    score-=10
                    user.draw()
            # collison with water
            if 0<=abs(user.x-water.x)<=waterdistancex and 0<=abs(user.y-water.y)<=waterdistancey:
                    score+=10
                    user.draw()
            # collison with french fry
            if 0<=abs(user.x-frenchfry.x)<=frenchfrydistancex and 0<=abs(user.y-frenchfry.y)<=frenchfrydistancey:
                    score-=10
                    user.draw()

            # if time up
            if time<=0:
                window.clear()
                user.set_position(window.width+100,0)
                timeup="Time's Up!"
                timeup_label = pyglet.text.Label(timeup,
                                          font_name='Times New Roman',
                                          font_size=40,
                                          x=window.width/2, y=window.height/2+25,
                                          anchor_x='center', anchor_y='center'
                                         )
                finalscore="Score: "+str(score)
                finalscore_label = pyglet.text.Label(finalscore,
                                          font_name='Times New Roman',
                                          font_size=36,
                                          x=window.width/2, y=window.height/2-25,
                                          anchor_x='center', anchor_y='center'
                                         )
                # assessing the score:
                if score>=2000:
                    veryhealthy_label = pyglet.text.Label("You had a very healthy meal!",
                                              font_name='Times New Roman',
                                              font_size=20,
                                              x=window.width/2, y=window.height/2-75,
                                              anchor_x='center', anchor_y='center'
                                             )
                    veryhealthy_label.draw()
                elif 1500<score<2000:
                    healthy_label = pyglet.text.Label("You had a somewhat healthy meal!",
                                              font_name='Times New Roman',
                                              font_size=20,
                                              x=window.width/2, y=window.height/2-75,
                                              anchor_x='center', anchor_y='center'
                                             )
                    healthy_label.draw()
                else:
                    nothealthy_label = pyglet.text.Label("You did not have a healthy meal!",
                                              font_name='Times New Roman',
                                              font_size=20,
                                              x=window.width/2, y=window.height/2-75,
                                              anchor_x='center', anchor_y='center'
                                             )
                    nothealthy_label.draw()
                endinstructions="Click back into the main game to keep playing"
                endinstructions_label = pyglet.text.Label(endinstructions,
                                          font_name='Times New Roman',
                                          font_size=15,
                                          x=window.width/2, y=window.height/2-120,
                                          anchor_x='center', anchor_y='center'
                                         )
                timeup_label.draw()
                finalscore_label.draw()
                endinstructions_label.draw()

@window.event #this event helps refresh the window if there are changes within it
def on_draw():
    # below is a introduction screen
    window.clear()
    # front page when the game is first opened
    start="Dinner Time"
    start_label = pyglet.text.Label(start,
                              font_name='Times New Roman',
                              font_size=40,
                              x=window.width/2, y=window.height/2+150,
                              anchor_x='center', anchor_y='center'
                             )
    instructions=("You have very limited time to eat as many healthy foods!")
    instructions2=("Within 90 seconds hover over as many healthy foods to")
    instructions3=("increase your score but if you hover over unhealthy foods,")
    instructions4=("your score will decrease.")
    instructions4a=("Then, you are rated: not healthy, somewhat healthy,")
    instructions4b= ("or very healthy.")
    instructions5=("Use your left and right arrow keys to move")
    instructions_label = pyglet.text.Label(instructions,
                              font_name='Times New Roman',
                              font_size=15,
                              x=window.width/2, y=window.height/2-50,
                              anchor_x='center', anchor_y='center'
                             )
    instructions2_label = pyglet.text.Label(instructions2,
                              font_name='Times New Roman',
                              font_size=15,
                              x=window.width/2, y=window.height/2-75,
                              anchor_x='center', anchor_y='center'
                             )
    instructions3_label = pyglet.text.Label(instructions3,
                              font_name='Times New Roman',
                              font_size=15,
                              x=window.width/2, y=window.height/2-100,
                              anchor_x='center', anchor_y='center'
                             )
    instructions4_label = pyglet.text.Label(instructions4,
                           font_name='Times New Roman',
                           font_size=15,
                           x=window.width/2, y=window.height/2-125,
                           anchor_x='center', anchor_y='center'
                          )
    instructions4a_label = pyglet.text.Label(instructions4a,
                           font_name='Times New Roman',
                           font_size=15,
                           x=window.width/2, y=window.height/2-150,
                           anchor_x='center', anchor_y='center'
                          )
    instructions4b_label = pyglet.text.Label(instructions4b,
                           font_name='Times New Roman',
                           font_size=15,
                           x=window.width/2, y=window.height/2-175,
                           anchor_x='center', anchor_y='center'
                          )
    instructions5_label = pyglet.text.Label(instructions5,
                           font_name='Times New Roman',
                           font_size=15,
                           x=window.width/2, y=window.height/2-200,
                           anchor_x='center', anchor_y='center'
                          )
    key="Press ENTER to start play"
    key_label = pyglet.text.Label(key,
                              font_name='Times New Roman',
                              font_size=20,
                              x=window.width/2, y=window.height/2-230,
                              anchor_x='center', anchor_y='center'
                             )
    start_label.draw()
    instructions_label.draw()
    instructions2_label.draw()
    instructions3_label.draw()
    instructions4_label.draw()
    instructions4a_label.draw()
    instructions4b_label.draw()
    instructions5_label.draw()
    key_label.draw()
pyglet.app.run()#this command should always be at the end of your code because it runs your code
# ------------------------------------------------------------------------------------------------
