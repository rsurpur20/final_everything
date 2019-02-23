"""////
Ryan Kim and Roshni Surpur
Due: February 22, 2019
Honor Code: On our honor, we have neither given nor received unauthorized aid.
Project Description: As the prompt of this project was to create a program that solved or fixed a problem, we used a game to address this. The user would have to solve the game and attempt to get the highest score possible. We created a 'choose your own adventure' game where the user made specific choices and played mini game, ultimately affecting their final score. Throughout our programming experience, we made various games before and wanted our final, culminating project to be unique. We drew inspiration from the very school which we attend, particularizing the game around the specific life at Choate. We based the storyline and each user decision after typical Choate students' lives. In order to capture the academic rigor, extracurricular activities, and difficult decisions that all exist at Choate, we chose particular points throughout the day that would demonstrate these defining Choate characteristics.

We started off our project by settling on using Processing to code our game. However, as we shifted our ideas, we decided to go with Python. We thought it would be a good way to end the two-term course as we were using Python throughout the entire length of the course. Additionally, as we had just studied the Pyglet library, we wanted to combine all that we had learned in our last project and in our time within CS550 to end with a culminating project. Although our goals for our program would be difficult to code with Python, we decided there was no better way to end the course than with a challenge.

Within our game, we chose specific moments throughout the day where students had to make critical decisions. A few of these include waking up in the morning, what to do during free blocks, how to persevere through sports, a various others. The choices that the user made at these points of the game would affect their overarching score and rating. In addition to these choices, we both made mini games that would also affect the bigger game. These came into play during particular Choate moments as well.

Ryan made a word search game. The user was given a word search board and had to find and type out the words they saw. The amount of correct words they got would affect both their grade and their score in the game. We integrated this mini game by setting it up as a vocabulary test for a World Religions class, just one of the many experiences that most Choate students go through. Within this mini game, there were many challenges. Specifically, it was hard to get the letters to show up on the screen as the user typed them. They would get stuck and wouldn't clear or be replaced by other letters that the user tried to type. Additionally, the process of correctly typing a word and moving on was extremely difficult as there were many points where the code had to be completely reassessed and reordered in order to make the errors disappear. Using pyglet, a newly learned library, in a majority of the code made it an extra challenge as more research in the functions and uses had to be explored.

Roshni made the dinner game. The premise of this game is to reflect Choate life. Espeically having lots of club meetings and homework,
students are usually on a time crunch when it comes to dinner, and it's also difficult to have a healthy meal as well. This game reflects
both the time constraint and the need to eat healthy foods. This game was especially fun to make but also very difficult. Some of the challenges I
faced was collision dectection. I figure out a way to fix this problem- I made the image's x and y location at the middle of the image
then, using if statements, I checked if an image's location was in the range of another image's x + or - half the width of the image,
or the image's y location + or - half the width of the imageself.This is also easier for the computer to run quickly. Overall making this game, especially using a library that I was unfamilar with was a fun learning experience.
Also the black color background was intentional, because any other color would distract from the objects falling down.

Also as far as our code, we could not use certain key topics from class such as while loops and classes because they didn't work well with Pyglet.
In order to run the program, the files all load the first time they are run from the terminal. We also found that if the other files don't load,
it isn't an issue with our code, but just the computer not loading the files. We found that restarting the terminal when the files don't load, works.

Sources
https://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/programming_guide/keyboard.html#keyboard-events
https://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/modules/window_key.html#module-pyglet.window.key
- These sources was also used to explore the key bindings and namings for pyglet

https://stackoverflow.com/questions/1186789/what-is-the-best-way-to-call-a-script-from-another-script
https://stackoverflow.com/questions/17254603/little-confused-with-import-python/17255637#17255637
- These sources helped us understand how to open a python file within another python file

https://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/
- This source gave us a lot of information on the basic uses of pyglet and helped in many aspects

http://www.poketcode.com/en/pyglet/index.html
- This source was used to help change the background color

Maxwell Brown'21 made the music using Garage Band
"""

import pyglet
from pyglet.window import key
from pyglet.window import Window
import time
from pyglet.gl import gl

window = pyglet.window.Window(800,600)

#Variables that determine the user's final score
game_score = 0
total_score = 10

#Intro Screen - adds the initial text boxes that appear on running the code
# importing choate crest image_______
choatecrest_image = pyglet.image.load('choatecrest.png')

choate_crest = pyglet.sprite.Sprite(choatecrest_image)
choate_crest.anchor_x=choate_crest.width/2
choate_crest.anchor_y=choate_crest.height/2
choate_crest.x=window.width//2-125
choate_crest.y=window.height//2-50
choate_crest.scale=0.8
# _______

#These are simple strings that will be used when adding the text. It was easier to create string variables and add them to the text code
instructions1 = ("You will live as a Choate student and go through a typical day at Choate.")
instructions2 = ("You will make decisions and undergo the rigors and choices that students make.")
instructions3 = ("At the end of the day, you will receive a grade based on your performance.")
instructions4 = ("Good luck.")
instructions5 = ("Press '1' to start")

#Here is the text code where the variables are input to make it more efficient
game_title = pyglet.text.Label('Day in the Life: Choate Student',
							font_name='Times New Roman',
							font_size=28,
							x=window.width//2, y=window.height*6/8+90,
							anchor_x='center', anchor_y='center')
x=80
instructions_text1 = pyglet.text.Label(instructions1,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-x,
							anchor_x='center', anchor_y='center')

instructions_text2 = pyglet.text.Label(instructions2,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-x-20,
							anchor_x='center', anchor_y='center')

instructions_text3 = pyglet.text.Label(instructions3,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-x-40,
							anchor_x='center', anchor_y='center')

instructions_text4 = pyglet.text.Label(instructions4,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-x-60,
							anchor_x='center', anchor_y='center')

instructions_text5 = pyglet.text.Label(instructions5,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-200,
							anchor_x='center', anchor_y='center')



#Waking Up Text - Same method for coding but used for waking up decision
# importing room image_______
room_image = pyglet.image.load('room.png')

room = pyglet.sprite.Sprite(room_image)
room.anchor_x=room.width/2
room.anchor_y=room.height/2
room.x=window.width//2-160
room.y=window.height//2-30
room.scale=0.08
# _______
wake_title = ("Wake Up")

wake_description = ("7:30AM")

wake1 = ("In the faint distance of your mind, you hear your alarm start to go off.")

wake2 = ("You instinctively grab your phone and press the snooze button.")

wake3 = ("You know you should get up now, but your mind and body push you to close your eyes.")

wake4 = ("Your roommate has a sleep-in, and you know he will not wake you up if you go back to sleep.")

wake5 = ("You are faced with a choice.")

wake6 = ("Let your body rest and skip your first period class")

wake7 = ("or")

wake8 = ("Suffer through the morning challenges and get ready for school")

wake9 = ("Press 'w' to wake up or 's' to continue sleeping")

wake_title_text = pyglet.text.Label(wake_title,
							font_name='Times New Roman',
							font_size=20,
							x=window.width//2, y=window.height*10/11+20,
							anchor_x='center', anchor_y='center')

wake_description_text = pyglet.text.Label(wake_description,
							font_name='Times New Roman',
							font_size=15,
							x=window.width//2, y=window.height*10/11 - 30+20,
							anchor_x='center', anchor_y='center')

wake_text1 = pyglet.text.Label(wake1,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-40,
							anchor_x='center', anchor_y='center')

wake_text2 = pyglet.text.Label(wake2,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-60,
							anchor_x='center', anchor_y='center')

wake_text3 = pyglet.text.Label(wake3,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-80,
							anchor_x='center', anchor_y='center')

wake_text4 = pyglet.text.Label(wake4,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-100,
							anchor_x='center', anchor_y='center')

wake_text5 = pyglet.text.Label(wake5,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-120,
							anchor_x='center', anchor_y='center')

wake_text6 = pyglet.text.Label(wake6,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-160,
							anchor_x='center', anchor_y='center')

wake_text7 = pyglet.text.Label(wake7,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-190,
							anchor_x='center', anchor_y='center')

wake_text8 = pyglet.text.Label(wake8,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-220,
							anchor_x='center', anchor_y='center')

wake_text9 = pyglet.text.Label(wake9,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-270,
							anchor_x='center', anchor_y='center')

#Decision Text - shows the decisions the user made

sleep_decision1 = ("You slept through your first class.")

sleep_decision2 = ("Your roommate woke you up when his alarm went off, and you feel much better now.")

sleep_decision3 = ("You are more prepared for your next class and will be more efficient while working.")

wake_decision1 = ("You decided to push yourself and got up.")

wake_decision2 = ("You were groggy but got through your first class where you learned a lot for an upcoming test.")

sleep_decision_text1 = pyglet.text.Label(sleep_decision1,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2+40,
							anchor_x='center', anchor_y='center')

sleep_decision_text2 = pyglet.text.Label(sleep_decision2,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2,
							anchor_x='center', anchor_y='center')

sleep_decision_text3 = pyglet.text.Label(sleep_decision3,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-40,
							anchor_x='center', anchor_y='center')

wake_decision_text1 = pyglet.text.Label(wake_decision1,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2+20,
							anchor_x='center', anchor_y='center')

wake_decision_text2 = pyglet.text.Label(wake_decision2,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-20,
							anchor_x='center', anchor_y='center')

continue2 = ("Press '2' to continue")

continue_text2 = pyglet.text.Label(continue2,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-200,
							anchor_x='center', anchor_y='center')

#Free Block Text - text code for the free block
# importing library image_______
library_image = pyglet.image.load('library.png')

library = pyglet.sprite.Sprite(library_image)
library.x=window.width//2+30
library.y=window.height//2
library.scale=0.07
# ______

# importing gameroom image _______
gameroom_image = pyglet.image.load('gameroom.png')

gameroom = pyglet.sprite.Sprite(gameroom_image)

gameroom.x=window.width//2-300
gameroom.y=window.height//2
gameroom.scale=0.07
# _______

free_title = ("Free Block")

free1 = ("After your first class, you had Math which was extremely boring. At 10:50AM, you rush out of class to beat the lunch lines.")

free2 = ("You had an amazing lunch, and now you have a double free.")

free3 = ("You are on your way back to your room when you get a text from a friend.")

free4 = ("'Let's play Fortnite'")

free5 = ("You really want to play but you know you should get work done for tomorrow as you have a lot piled up.")

free6 = ("A.) Homework is for losers. Play Fortnite!")

free7 = ("B.) Play Fortnite for one free and do homework during another.")

free8 = ("C.) Fortnite can wait. Go to the library and finish my homework.")

free9 = ("Press 'a' or 'b' or 'c'")

free_title_text = pyglet.text.Label(free_title,
							font_name='Times New Roman',
							font_size=20,
							x=window.width//2, y=window.height*10/11,
							anchor_x='center', anchor_y='center')

free_text1 = pyglet.text.Label(free1,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-20,
							anchor_x='center', anchor_y='center')

free_text2 = pyglet.text.Label(free2,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-40,
							anchor_x='center', anchor_y='center')

free_text3 = pyglet.text.Label(free3,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-60,
							anchor_x='center', anchor_y='center')

free_text4 = pyglet.text.Label(free4,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-100,
							anchor_x='center', anchor_y='center')

free_text5 = pyglet.text.Label(free5,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-140,
							anchor_x='center', anchor_y='center')

free_text6 = pyglet.text.Label(free6,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//3-50, y=window.height//2-190,
							anchor_x='left', anchor_y='center')

free_text7 = pyglet.text.Label(free7,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//3-50, y=window.height//2-210,
							anchor_x='left', anchor_y='center')

free_text8 = pyglet.text.Label(free8,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//3-50, y=window.height//2-230,
							anchor_x='left', anchor_y='center')

free_text9 = pyglet.text.Label(free9,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-270,
							anchor_x='center', anchor_y='center')

free_decisionA1 = ("You chose to play Fortnite with your friend during both free blocks.")

free_decisionA2 = ("It was a lot of fun, but now you have a lot of work to do later on.")

free_decisionB1 = ("You chose to play during one block and work during the next.")

free_decisionB2 = ("You split your time well and had a great time playing games before going to the library and working hard.")

free_decisionB3 = ("You got some homework done, but there is still a good amount left for later.")

free_decisionC1 = ("You chose to go to the library and do your homework.")

free_decisionC2 = ("In the library, you weren't distracted by anything and got most of your homework done.")

free_decisionA1_text = pyglet.text.Label(free_decisionA1,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2+20,
							anchor_x='center', anchor_y='center')

free_decisionA2_text = pyglet.text.Label(free_decisionA2,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-20,
							anchor_x='center', anchor_y='center')

free_decisionB1_text = pyglet.text.Label(free_decisionB1,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2+40,
							anchor_x='center', anchor_y='center')

free_decisionB2_text = pyglet.text.Label(free_decisionB2,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2,
							anchor_x='center', anchor_y='center')

free_decisionB3_text = pyglet.text.Label(free_decisionB3,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-40,
							anchor_x='center', anchor_y='center')

free_decisionC1_text = pyglet.text.Label(free_decisionC1,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2+20,
							anchor_x='center', anchor_y='center')

free_decisionC2_text = pyglet.text.Label(free_decisionC2,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-20,
							anchor_x='center', anchor_y='center')

continue3 = ("Press '3' to continue")

continue_text3 = pyglet.text.Label(continue3,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-120,
							anchor_x='center', anchor_y='center')

#Test Text - Same method for coding but used for test taking
#importing classroom image _______
classroom_image = pyglet.image.load('classroom.png')

classroom = pyglet.sprite.Sprite(classroom_image)
classroom.anchor_x=classroom.width/2
classroom.anchor_y=classroom.height/2
classroom.x=window.width//2-140
classroom.y=window.height//2-10
classroom.scale=.07
# _______

test_title = ("World Religions")

test_description = ("Vocabulary Test")

test1 = ("You go to the Humanities building after your free for the last class of the day: World Religions.")

test2 = ("You have a test! Your teacher starts handing out a vocabulary test for you all to solve.")

test_title_text = pyglet.text.Label(test_title,
							font_name='Times New Roman',
							font_size=20,
							x=window.width//2, y=window.height*10/11,
							anchor_x='center', anchor_y='center')

test_description_text = pyglet.text.Label(test_description,
							font_name='Times New Roman',
							font_size=15,
							x=window.width//2, y=window.height*10/11-30,
							anchor_x='center', anchor_y='center')

test_text1 = pyglet.text.Label(test1,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-20,
							anchor_x='center', anchor_y='center')

test_text2 = pyglet.text.Label(test2,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-60,
							anchor_x='center', anchor_y='center')

continue4 = ("Press '4' to take the test")

continue_text4 = pyglet.text.Label(continue4,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-150,
							anchor_x='center', anchor_y='center')

continue5 = ("Press '5' to continue")

continue_text5 = pyglet.text.Label(continue5,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-180,
							anchor_x='center', anchor_y='center')

#Sports Text - Same method for coding but used for sports decision

#importing court image _______
court_image = pyglet.image.load('bballcourt.png')

court = pyglet.sprite.Sprite(court_image)
court.anchor_x=court.width/2
court.anchor_y=court.height/2
court.x=window.width//2-140
court.y=window.height//2+10
court.scale=0.07
# _______

sports_title = ("Sports")

sports_description = ("4PM - 6PM")

sports1 = ("You finished the test just before time ran out.")

sports2 = ("You head back to your dorm to grab your things before going to sports.")

sports3 = ("At practice, your coach is mad about your team's recent loss and is pushing you hard.")

sports4 = ("You and your teammates are exhausted, and everyone is dispirited.")

sports5 = ("As the captain, you see an opportunity to raise the team's morale. However, you are already so tired.")

sports6 = ("You can:")

sports7 = ("Life up your team's spirits")

sports8 = ("or")

sports9 = ("Let your exhaustion consume you")

sports10 = ("Press 'L' to raise spirits or 'e' to do nothing")

sports_title_text = pyglet.text.Label(sports_title,
							font_name='Times New Roman',
							font_size=20,
							x=window.width//2, y=window.height*10/11+20,
							anchor_x='center', anchor_y='center')

sports_description_text = pyglet.text.Label(sports_description,
							font_name='Times New Roman',
							font_size=15,
							x=window.width//2, y=window.height*10/11-30+20,
							anchor_x='center', anchor_y='center')

sports_text1 = pyglet.text.Label(sports1,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2,
							anchor_x='center', anchor_y='center')

sports_text2 = pyglet.text.Label(sports2,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-20,
							anchor_x='center', anchor_y='center')

sports_text3 = pyglet.text.Label(sports3,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-40,
							anchor_x='center', anchor_y='center')

sports_text4 = pyglet.text.Label(sports4,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-60,
							anchor_x='center', anchor_y='center')

sports_text5 = pyglet.text.Label(sports5,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-80,
							anchor_x='center', anchor_y='center')

sports_text6 = pyglet.text.Label(sports6,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-110,
							anchor_x='center', anchor_y='center')

sports_text7 = pyglet.text.Label(sports7,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-150,
							anchor_x='center', anchor_y='center')

sports_text8 = pyglet.text.Label(sports8,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-175,
							anchor_x='center', anchor_y='center')

sports_text9 = pyglet.text.Label(sports9,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-200,
							anchor_x='center', anchor_y='center')

sports_text10 = pyglet.text.Label(sports10,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-260,
							anchor_x='center', anchor_y='center')

cheer1 = ("You persevered through your tiredness and attempted to cheer on your teammates.")

cheer2 = ("They followed your leadership and pushed themselves hard in practice.")

cheer3 = ("You guys became better and closer as a sports team.")

exhaust1 = ("You were too tired to do anything other than follow your coach's shouting.")

exhaust2 = ("Your teammates stayed dispirited and struggled through practice.")

exhaust3 = ("The team's morale dropped, and everyone played worse than before.")

cheer_text1 = pyglet.text.Label(cheer1,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2+40,
							anchor_x='center', anchor_y='center')

cheer_text2 = pyglet.text.Label(cheer2,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2,
							anchor_x='center', anchor_y='center')

cheer_text3 = pyglet.text.Label(cheer3,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-40,
							anchor_x='center', anchor_y='center')

exhaust_text1 = pyglet.text.Label(exhaust1,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2+40,
							anchor_x='center', anchor_y='center')

exhaust_text2 = pyglet.text.Label(exhaust2,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2,
							anchor_x='center', anchor_y='center')

exhaust_text3 = pyglet.text.Label(exhaust3,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-40,
							anchor_x='center', anchor_y='center')

continue6 = ("Press '6' to continue")

continue_text6 = pyglet.text.Label(continue6,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-200,
							anchor_x='center', anchor_y='center')

#Club Text - Same method for coding but used for club decision
# importing club image_______
club_image = pyglet.image.load('projectroom.png')

clubpic = pyglet.sprite.Sprite(club_image)
clubpic.anchor_x=clubpic.width/2
clubpic.anchor_y=clubpic.height/2
clubpic.x=window.width//2-140
clubpic.y=window.height//2+10
clubpic.scale=0.07
# _______


club_title = ("Club Meeting")

club_description = ("6PM")

club1 = ("You leave sports at 6PM completely drained.")

club2 = ("You are walking back to your dorm when a notification pops up.")

club3 = ("'Reminder: Club Meeting @ 6:15")

club4 = ("N.) Skip the meeting and rely on your other cabinet members")

club5 = ("or")

club6 = ("P.) Push through your exhaustion and go to the club meeting")

club7 = ("Press 'n' or 'p'")

club_intersection = ("------------------------------------------")

club_title_text = pyglet.text.Label(club_title,
							font_name='Times New Roman',
							font_size=20,
							x=window.width//2, y=window.height*10/11+20,
							anchor_x='center', anchor_y='center')

club_description_text = pyglet.text.Label(club_description,
							font_name='Times New Roman',
							font_size=15,
							x=window.width//2, y=window.height*10/11-30+20,
							anchor_x='center', anchor_y='center')

club_text1 = pyglet.text.Label(club1,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-20,
							anchor_x='center', anchor_y='center')

club_text2 = pyglet.text.Label(club2,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-40,
							anchor_x='center', anchor_y='center')

club_text3 = pyglet.text.Label(club3,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-100,
							anchor_x='center', anchor_y='center')

club_text4 = pyglet.text.Label(club4,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//4, y=window.height//2-160,
							anchor_x='left', anchor_y='center')

club_text5 = pyglet.text.Label(club5,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-190,
							anchor_x='center', anchor_y='center')

club_text6 = pyglet.text.Label(club6,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//4, y=window.height//2-220,
							anchor_x='left', anchor_y='center')

club_text7 = pyglet.text.Label(club7,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-270,
							anchor_x='center', anchor_y='center')

club_intersection_text = pyglet.text.Label(club_intersection,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-70,
							anchor_x='center', anchor_y='center')

club_intersection_text2 = pyglet.text.Label(club_intersection,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-130,
							anchor_x='center', anchor_y='center')

club_decisionP1 = ("You followed your duties as a club leader and went to the meeting.")

club_decisionP2 = ("The club meeting went well and you got many members to sign up for an upcoming event.")

club_decisionN1 = ("You decided you were too tired to follow through your duties as a club leader.")

club_decisionN2 = ("You went back to your room and took a quick power nap on your bed.")

club_decisionP1_text = pyglet.text.Label(club_decisionP1,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2+20,
							anchor_x='center', anchor_y='center')

club_decisionP2_text = pyglet.text.Label(club_decisionP2,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-20,
							anchor_x='center', anchor_y='center')

club_decisionN1_text = pyglet.text.Label(club_decisionN1,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2+20,
							anchor_x='center', anchor_y='center')

club_decisionN2_text = pyglet.text.Label(club_decisionN2,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-20,
							anchor_x='center', anchor_y='center')

continue7 = ("Press '7' to continue")

continue_text7 = pyglet.text.Label(continue7,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-200,
							anchor_x='center', anchor_y='center')

#Dinner Text - Same method for coding but used for dinner game
#importing dinner image _______
dinner_image = pyglet.image.load('dh.png')

dinning_hall = pyglet.sprite.Sprite(dinner_image)
dinning_hall.anchor_x=dinning_hall.width/2
dinning_hall.anchor_y=dinning_hall.height/2
dinning_hall.x=window.width//2-140
dinning_hall.y=window.height//2+10
dinning_hall.scale=0.07
# _______
dinner_title = ("Dinner")

dinner_description = ("7PM")

dinner1 = ("You leave your club meeting and head to dinner.")

dinner2 = ("You look around and see a lot of things you want to eat.")

dinner3 = ("However, you remember you started going on a diet a few days ago.")

dinner4 = ("Decide how you will go about your dinner options.")

dinner_title_text = pyglet.text.Label(dinner_title,
							font_name='Times New Roman',
							font_size=20,
							x=window.width//2, y=window.height*10/11+20,
							anchor_x='center', anchor_y='center')

dinner_description_text = pyglet.text.Label(dinner_description,
							font_name='Times New Roman',
							font_size=15,
							x=window.width//2, y=window.height*10/11-30+20,
							anchor_x='center', anchor_y='center')

dinner_text1 = pyglet.text.Label(dinner1,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-20,
							anchor_x='center', anchor_y='center')

dinner_text2 = pyglet.text.Label(dinner2,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-60,
							anchor_x='center', anchor_y='center')

dinner_text3 = pyglet.text.Label(dinner3,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-100,
							anchor_x='center', anchor_y='center')

dinner_text4 = pyglet.text.Label(dinner4,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-140,
							anchor_x='center', anchor_y='center')

continue8 = ("Press '8' to eat dinner")

continue_text8 = pyglet.text.Label(continue8,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-200,
							anchor_x='center', anchor_y='center')

continue9 = ("Press '9' to continue")

continue_text9 = pyglet.text.Label(continue9,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-230,
							anchor_x='center', anchor_y='center')

#Study Hours Text - Same method for coding but used for study hours decision
#importing desk image _______
desk_image = pyglet.image.load('desk.png')

desk = pyglet.sprite.Sprite(desk_image)
desk.anchor_x=desk.width/2
desk.anchor_y=desk.height/2
desk.x=window.width//2-110
desk.y=window.height//2+5
desk.scale=.49
# _______
study_title = ("Study Hours")

study_description = ("8PM")

study1 = ("You finished eating dinner and get back to your room just in time for study hours.")

study2 = ("You work hard for a while and finish all your homework for tomorrow, but have a lot due the next day.")

study3 = ("You can hear your friends having a blast in another room, and you really want to join them.")

study4 = ("You know that working now will help later, but you've had a tough day and you did finish all your immediate work.")

study5 = ("----------------------------------------------------------------------------------------------")

study6 = ("R.) Acknowledge the work you've done and seek out your friends")

study7 = ("Q.) Keep on grinding to make your life tomorrow easier")

study8 = ("Press 'r' or 'q'")

study_title_text = pyglet.text.Label(study_title,
							font_name='Times New Roman',
							font_size=20,
							x=window.width//2, y=window.height*10/11,
							anchor_x='center', anchor_y='center')

study_description_text = pyglet.text.Label(study_description,
							font_name='Times New Roman',
							font_size=15,
							x=window.width//2, y=window.height*10/11-30,
							anchor_x='center', anchor_y='center')

study_text1 = pyglet.text.Label(study1,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2,
							anchor_x='center', anchor_y='center')

study_text2 = pyglet.text.Label(study2,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-20,
							anchor_x='center', anchor_y='center')

study_text3 = pyglet.text.Label(study3,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-40,
							anchor_x='center', anchor_y='center')

study_text4 = pyglet.text.Label(study4,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-60,
							anchor_x='center', anchor_y='center')

study_text5 = pyglet.text.Label(study5,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-100,
							anchor_x='center', anchor_y='center')

study_text6 = pyglet.text.Label(study6,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//4, y=window.height//2-140,
							anchor_x='left', anchor_y='center')

study_text7 = pyglet.text.Label(study7,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//4, y=window.height//2-180,
							anchor_x='left', anchor_y='center')

study_text8 = pyglet.text.Label(study8,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-240,
							anchor_x='center', anchor_y='center')

study_decisionR1 = ("You chose to understand your progress and grant yourself some relaxing, fun time.")

study_decisionR2 = ("More at ease, you walk over to your friends' room and have a great time with them.")

study_decisionR3 = ("You spent the second half of study hours laughing and having fun before going to bed at 12AM.")

study_decisionQ1 = ("You chose to continue working in order to get ahead for tomorrow.")

study_decisionQ2 = ("You work through the entire study hours and get a solid amount of tomorrow's work done.")

study_decisionQ3 = ("At 12PM, your eyes are shutting on their own and your brain is fried. You crawl into bed and sleep.")

study_decisionR1_text = pyglet.text.Label(study_decisionR1,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2+40,
							anchor_x='center', anchor_y='center')

study_decisionR2_text = pyglet.text.Label(study_decisionR2,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2,
							anchor_x='center', anchor_y='center')

study_decisionR3_text = pyglet.text.Label(study_decisionR3,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-40,
							anchor_x='center', anchor_y='center')

study_decisionQ1_text = pyglet.text.Label(study_decisionQ1,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2+40,
							anchor_x='center', anchor_y='center')

study_decisionQ2_text = pyglet.text.Label(study_decisionQ2,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2,
							anchor_x='center', anchor_y='center')

study_decisionQ3_text = pyglet.text.Label(study_decisionQ3,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-40,
							anchor_x='center', anchor_y='center')

continue0 = ("Press '0' to continue")

continue_text0 = pyglet.text.Label(continue0,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-230,
							anchor_x='center', anchor_y='center')

#-------------------------------------------------------------------

#Built in pyglet function for key pressed
@window.event
def on_key_press(symbol, modifiers):
	global game_score

	if (symbol == key._1): #GAME STARTS
		#Resets the screen and draws the waking up decision screen
		@window.event
		def on_draw():
			window.clear()
			wake_title_text.draw()
			room.draw()
			wake_text1.draw()
			wake_text2.draw()
			wake_text3.draw()
			wake_text4.draw()
			wake_text5.draw()
			wake_text6.draw()
			wake_text7.draw()
			wake_text8.draw()
			wake_text9.draw()
			wake_text9.draw()
			wake_description_text.draw()

	if (symbol == key.S): #If user decides to keep sleeping, it redraws the window with updated text
		game_score += 0
		@window.event
		def on_draw():
			window.clear()
			sleep_decision_text1.draw()
			sleep_decision_text2.draw()
			sleep_decision_text3.draw()
			continue_text2.draw()
			continue_text2.draw()

	elif (symbol == key.W): #If user decides to wake up, the score increases and the text is updated for their respective decision
		game_score += 1
		@window.event
		def on_draw():
			window.clear()
			wake_decision_text1.draw()
			wake_decision_text2.draw()
			continue_text2.draw()
			continue_text2.draw()

	#-------------------------------------------

	if (symbol == key._2): #Continues onto the next decision (free block)
		@window.event
		def on_draw():
			window.clear()
			free_title_text.draw()
			gameroom.draw()
			library.draw()
			free_text1.draw()
			free_text2.draw()
			free_text3.draw()
			free_text4.draw()
			free_text5.draw()
			free_text6.draw()
			free_text7.draw()
			free_text8.draw()
			free_text9.draw()
			free_text9.draw()

	if (symbol == key.A): #If the user plays fortnite the entire time
		game_score += 0
		@window.event
		def on_draw():
			window.clear()
			free_decisionA1_text.draw()
			free_decisionA2_text.draw()
			continue_text3.draw()
			continue_text3.draw()

	elif (symbol == key.B): #If the user splits their time to study and play
		game_score += 1
		@window.event
		def on_draw():
			window.clear()
			free_decisionB1_text.draw()
			free_decisionB2_text.draw()
			free_decisionB3_text.draw()
			continue_text3.draw()
			continue_text3.draw()

	elif (symbol == key.C): #If the user only studies
		game_score += 2
		@window.event
		def on_draw():
			window.clear()
			free_decisionC1_text.draw()
			free_decisionC2_text.draw()
			continue_text3.draw()
			continue_text3.draw()

	#-------------------------------------------

	if (symbol == key._3): #Moves onto the next screen where student takes test
		@window.event
		def on_draw():
			window.clear()
			test_title_text.draw()
			test_description_text.draw()
			classroom.draw()
			test_text1.draw()
			test_text2.draw()
			continue_text4.draw()
			continue_text4.draw()
			continue_text5.draw()
			continue_text5.draw()

	if (symbol == key._4): #Student takes the test
		#This imports the mini game which is in another file as well as the variable that will affect the game_score
		import final_wordgame.py
		final_wordgame
		if (final_wordgame.correct >= 9):
			game_score += 2
		elif (final_wordgame.correct >= 5):
			game_score += 1
		else:
			game_score += 0
		print(final_wordgame.correct)

	#-------------------------------------------

	if (symbol == key._5): #Moves onto next decision which is the sports one
		@window.event
		def on_draw():
			gl.glClearColor(0,0,0,1)
			window.clear()
			sports_title_text.draw()
			sports_description_text.draw()
			court.draw()
			sports_text1.draw()
			sports_text2.draw()
			sports_text3.draw()
			sports_text4.draw()
			sports_text5.draw()
			sports_text6.draw()
			sports_text7.draw()
			sports_text8.draw()
			sports_text9.draw()
			sports_text10.draw()
			sports_text10.draw()

	if (symbol == key.L): #If user cheers their teammates on
		game_score += 1
		@window.event
		def on_draw():
			window.clear()
			cheer_text1.draw()
			cheer_text2.draw()
			cheer_text3.draw()
			continue_text6.draw()
			continue_text6.draw()

	elif (symbol == key.E): #If user is too tired to do anything
		game_score += 0
		@window.event
		def on_draw():
			window.clear()
			exhaust_text1.draw()
			exhaust_text2.draw()
			exhaust_text3.draw()
			continue_text6.draw()
			continue_text6.draw()

	#-------------------------------------------

	if (symbol == key._6): #Next screen that shows the club decision
		@window.event
		def on_draw():
			window.clear()
			club_title_text.draw()
			club_description_text.draw()
			clubpic.draw()
			club_text1.draw()
			club_text2.draw()
			club_text3.draw()
			club_text4.draw()
			club_text5.draw()
			club_text6.draw()
			club_text7.draw()
			club_text7.draw()
			club_intersection_text.draw()
			club_intersection_text2.draw()

	if (symbol == key.N): #If the user does not go to their club meeting
		game_score += 0
		@window.event
		def on_draw():
			window.clear()
			club_decisionN1_text.draw()
			club_decisionN2_text.draw()
			continue_text7.draw()
			continue_text7.draw()

	if (symbol == key.P): #If the user participates in their club meeting
		game_score += 1
		@window.event
		def on_draw():
			window.clear()
			club_decisionP1_text.draw()
			club_decisionP2_text.draw()
			continue_text7.draw()
			continue_text7.draw()

	#-------------------------------------------

	if (symbol == key._7): #Shows the next screen which leads into the mini game
		@window.event
		def on_draw():
			window.clear()
			dinner_title_text.draw()
			dinner_description_text.draw()
			dinning_hall.draw()
			dinner_text1.draw()
			dinner_text2.draw()
			dinner_text3.draw()
			dinner_text4.draw()
			continue_text8.draw()
			continue_text8.draw()
			continue_text9.draw()
			continue_text9.draw()

	if (symbol == key._8): #Plays the game
		#Similar to the last import for the other mini game

		import pygletcode.py
		pygletcode
		if (pygletcode.score >= 2250):
			game_score += 2
		elif (pygletcode.score >= 1500):
			game_score += 1
		else:
			game_score += 0

	#-------------------------------------------

	if (symbol == key._9): #Moves onto the next screen which shows the study hours decision
		@window.event
		def on_draw():
			window.clear()
			study_title_text.draw()
			study_description_text.draw()
			desk.draw()
			study_text1.draw()
			study_text2.draw()
			study_text3.draw()
			study_text4.draw()
			study_text5.draw()
			study_text6.draw()
			study_text7.draw()
			study_text8.draw()
			study_text8.draw()

	if (symbol == key.R): #If user decides to go play with their friends
		game_score += 0
		@window.event
		def on_draw():
			window.clear()
			study_decisionR1_text.draw()
			study_decisionR2_text.draw()
			study_decisionR3_text.draw()
			continue_text0.draw()
			continue_text0.draw()

	if (symbol == key.Q): #If user decides to keep working
		game_score += 1
		@window.event
		def on_draw():
			window.clear()
			study_decisionQ1_text.draw()
			study_decisionQ2_text.draw()
			study_decisionQ3_text.draw()
			continue_text0.draw()
			continue_text0.draw()

	#-------------------------------------------

	#End screen

	grade = str((str(game_score) + "/" + str(total_score))) #sets the grade as their score out of 10

	#Text for end screen

	end_title = ("Game Over")

	end1 = ("Congratulations! You got through a day at Choate!")

	end2 = ("Your performance rating is shown above.")

	end3 = ("Great job!")

	end_title_text = pyglet.text.Label(end_title,
							font_name='Times New Roman',
							font_size=20,
							x=window.width//2, y=window.height*10/11,
							anchor_x='center', anchor_y='center')

	grade_text = pyglet.text.Label(grade,
							font_name='Times New Roman',
							font_size=38,
							x=window.width//2, y=window.height//2+100,
							anchor_x='center', anchor_y='center')

	end_text1 = pyglet.text.Label(end1,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-80,
							anchor_x='center', anchor_y='center')

	end_text2 = pyglet.text.Label(end2,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-120,
							anchor_x='center', anchor_y='center')

	end_text3 = pyglet.text.Label(end3,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-160,
							anchor_x='center', anchor_y='center')

	if (symbol == key._0): #Prints the end screen into the window
		@window.event
		def on_draw():
			window.clear()
			end_title_text.draw()
			grade_text.draw()
			grade_text.draw()
			end_text1.draw()
			end_text2.draw()
			end_text3.draw()






#-------------------------------------------------------------------

music = pyglet.resource.media("background_music.wav")
#This is the initial draw screen which displays the intro screen
@window.event
def on_draw():
	window.clear()
	game_title.draw()
	choate_crest.draw()
	instructions_text1.draw()
	instructions_text2.draw()
	instructions_text3.draw()
	instructions_text4.draw()
	instructions_text5.draw()
	instructions_text5.draw()
# adding music_____________________

	music.play()
# _________________________________

pyglet.app.run() #Runs the code










"""
To Do
- Take/Add Pictures
- Change Color
- Music
- Comments
"""
