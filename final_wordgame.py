import pyglet
from pyglet.window import key
from pyglet.window import Window
from pyglet.gl import gl
import time

word_list = [] #Letters are added here to see if they form a word
correct = 0 #Number of correct words
grade = "Unknown" #Initial declaration of the grade (A, B, C)
answer = "nothing" #Initial declaration of the answer - answer is the correct word they type

#Sets all the words as true initally and when they are correctly typed in the game, it sets these as false so that the user can't retype these words to get already received points
correct_catholic = True
correct_church = True
correct_priest = True
correct_swansea = True
correct_candle = True
correct_stdavids = True
correct_bishop = True
correct_canon = True
correct_baptism = True
correct_hymns = True
correct_parish = True
correct_organ = True
correct_pope = True
correct_diocese = True

#Background color
background_color = (0.6, 0.4, 0.2, 1)
gl.glClearColor(*background_color)

window = pyglet.window.Window(500,500)

#All code for the text that shows up in the introduction screen
test = pyglet.text.Label('World Religions Test',
							font_name='Times New Roman',
							font_size=34,
							x=window.width//2, y=window.height*7/8,
							anchor_x='center', anchor_y='center')

#String variables in order to make the pyglet text code more efficient
word_instructions1 = "Your test is a word search. There are 14 words to find."
word_instructions2 = "Type the word you find and press 'enter'."
word_instructions3 = "Make sure to type the word correctly to get points."
word_instructions4 = "If you mistype a word, start from the beginning letter."
word_instructions5 = "If you are done finding words, type 'done' and then 'enter'."
word_instructions6 = "Press any key to begin"

#Variables above are just put into these blocks and the parameters are set to fit well with each other
word_instructions_text1 = pyglet.text.Label(word_instructions1,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2+40,
							anchor_x='center', anchor_y='center')

word_instructions_text2 = pyglet.text.Label(word_instructions2,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2+20,
							anchor_x='center', anchor_y='center')

word_instructions_text3 = pyglet.text.Label(word_instructions3,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2,
							anchor_x='center', anchor_y='center')

word_instructions_text4 = pyglet.text.Label(word_instructions4,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-20,
							anchor_x='center', anchor_y='center')

word_instructions_text5 = pyglet.text.Label(word_instructions5,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-40,
							anchor_x='center', anchor_y='center')

word_instructions_text6 = pyglet.text.Label(word_instructions6,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//4,
							anchor_x='center', anchor_y='center')

#Text for final screen
final = ("Leave the window to return back to the Choate life.")

final_text = pyglet.text.Label(final,
							font_name='Times New Roman',
							font_size=15,
							x=window.width//2, y=window.height//6,
							anchor_x='center', anchor_y='center')

#Loads image and scales it to fit better in the window
word_search = pyglet.image.load('wordsearch.png')
word = pyglet.sprite.Sprite(word_search, x=window.width//5.5-10, y=window.height//5)
word.scale=0.8

#-------------------------------------------------------------------------

#Main Code - everything is used and applied here under the built in on_key_press function
@window.event
def on_key_press(symbol, modifiers):
	global correct, correct_catholic, correct_church, correct_priest, correct_swansea, correct_candle, correct_stdavids, correct_bishop, correct_canon, correct_baptism, correct_hymns, correct_parish, correct_organ, correct_pope, correct_diocese

	letter_pressed = str(pyglet.window.key.symbol_string(symbol)) #Code for receiving the string value of the letter pressed
	word_list.append(letter_pressed) #Takes the letter pressed and adds to list so that it can be checked later on

	#Text for showing only the letter that the user pressed
	letter = pyglet.text.Label(letter_pressed,
							font_name='Times New Roman',
							font_size=36,
							x=window.width//2, y=window.height//9,
							anchor_x='center', anchor_y='center')

	#Score (number of words the user got) at the top left of the screen.
	score = pyglet.text.Label ('Words: ' + str(correct),
							font_name = 'Times New Roman',
							font_size = 14,
							x = (window.width//10), y = window.height*(17/18),
							anchor_x = 'center', anchor_y = 'center')

	#Draws the contents in the window
	@window.event
	def on_draw():
		window.clear()
		test.draw() #"World Religions Test"
		word.draw() #Image for word search board
		letter.draw() #Letter that user types
		score.draw() #Score
		gl.glClearColor(*background_color) #Background color for window

#-------------------------------------------------------------------------

	#Used for checking before and after the letters in the list to see if they come together to spell one of the words
	for x in range(len(word_list)):

		#Checks to see if the letters are in order of the correct word
		if (correct_catholic == True):
			if (letter_pressed == "ENTER"):
				if (word_list[x] == "C"):
					if (word_list[x+1] == "A"):
						if (word_list[x+2] == "T"):
							if (word_list[x+3] == "H"):
								if (word_list[x+4] == "O"):
									if (word_list[x+5] == "L"):
										if (word_list[x+6] == "I"):
											if (word_list[x+7] == "C"):

												print("You got 'catholic'!")
												correct += 1 #adds to the score in this mini game
												answer = "catholic"
												correct_catholic = False #Set to false so that user can't get it twice

												#Text that prints the correct word that the user got
												correct_answer = pyglet.text.Label ("You got '" + answer + "'!",
																			font_name = 'Times New Roman',
																			font_size = 36,
																			x = (window.width//2), y = (window.height//9),
																			anchor_x = 'center', anchor_y = 'center')

												#Text that updates the score
												score = pyglet.text.Label ('Words: ' + str(correct),
																			font_name = 'Times New Roman',
																			font_size = 14,
																			x = (window.width//10), y = window.height*(17/18),
																			anchor_x = 'center', anchor_y = 'center')

												#Draws all of the updates made on the board
												@window.event
												def on_draw():
													window.clear() #Clear statement
													test.draw() #"World Religions Test"
													word.draw() #Word Search Image
													correct_answer.draw() #Shows correct statement
													score.draw() #Updated Score
													gl.glClearColor(*background_color) #Keeps the background color the same

#--------------------------------------------------------------------------
#Everything is the same as shown above - only the words and printed statements are different to revolve around the letters and words typed

		if (correct_church == True):
			if (letter_pressed == "ENTER"):
				if (word_list[x] == "C"):
					if (word_list[x+1] == "H"):
						if (word_list[x+2] == "U"):
							if (word_list[x+3] == "R"):
								if (word_list[x+4] == "C"):
									if (word_list[x+5] == "H"):
										print("You got 'church'!")
										correct += 1
										answer = "church"
										correct_church = False

										correct_answer = pyglet.text.Label ("You got '" + answer + "'!",
																	font_name = 'Times New Roman',
																	font_size = 36,
																	x = (window.width//2), y = (window.height//9),
																	anchor_x = 'center', anchor_y = 'center')

										score = pyglet.text.Label ('Words: ' + str(correct),
																	font_name = 'Times New Roman',
																	font_size = 14,
																	x = (window.width//10), y = window.height*(17/18),
																	anchor_x = 'center', anchor_y = 'center')

										@window.event
										def on_draw():
											window.clear()
											test.draw()
											word.draw()
											correct_answer.draw()
											score.draw()
											gl.glClearColor(*background_color)

#--------------------------------------------------------------------------
		if (correct_priest == True):
			if (letter_pressed == "ENTER"):
				if (word_list[x] == "P"):
					if (word_list[x+1] == "R"):
						if (word_list[x+2] == "I"):
							if (word_list[x+3] == "E"):
								if (word_list[x+4] == "S"):
									if (word_list[x+5] == "T"):
										print("You got 'priest'!")
										correct += 1
										answer = "priest"
										correct_priest = False

										correct_answer = pyglet.text.Label ("You got '" + answer + "'!",
																	font_name = 'Times New Roman',
																	font_size = 36,
																	x = (window.width//2), y = (window.height//9),
																	anchor_x = 'center', anchor_y = 'center')

										score = pyglet.text.Label ('Words: ' + str(correct),
																	font_name = 'Times New Roman',
																	font_size = 14,
																	x = (window.width//10), y = window.height*(17/18),
																	anchor_x = 'center', anchor_y = 'center')

										@window.event
										def on_draw():
											window.clear()
											test.draw()
											word.draw()
											correct_answer.draw()
											score.draw()
											gl.glClearColor(*background_color)

#--------------------------------------------------------------------------

		if (correct_swansea == True):
			if (letter_pressed == "ENTER"):
				if (word_list[x] == "S"):
					if (word_list[x+1] == "W"):
						if (word_list[x+2] == "A"):
							if (word_list[x+3] == "N"):
								if (word_list[x+4] == "S"):
									if (word_list[x+5] == "E"):
										if (word_list[x+6] == "A"):
											print("You got 'swansea'!")
											correct += 1
											answer = "swansea"
											correct_swansea = False

											correct_answer = pyglet.text.Label ("You got '" + answer + "'!",
																		font_name = 'Times New Roman',
																		font_size = 36,
																		x = (window.width//2), y = (window.height//9),
																		anchor_x = 'center', anchor_y = 'center')

											score = pyglet.text.Label ('Words: ' + str(correct),
																		font_name = 'Times New Roman',
																		font_size = 14,
																		x = (window.width//10), y = window.height*(17/18),
																		anchor_x = 'center', anchor_y = 'center')

											@window.event
											def on_draw():
												window.clear()
												test.draw()
												word.draw()
												correct_answer.draw()
												score.draw()
												gl.glClearColor(*background_color)

#--------------------------------------------------------------------------

		if (correct_candle == True):
			if (letter_pressed == "ENTER"):
				if (word_list[x] == "C"):
					if (word_list[x+1] == "A"):
						if (word_list[x+2] == "N"):
							if (word_list[x+3] == "D"):
								if (word_list[x+4] == "L"):
									if (word_list[x+5] == "E"):
										print("You got 'candle'!")
										correct += 1
										answer = "candle"
										correct_candle = False

										correct_answer = pyglet.text.Label ("You got '" + answer + "'!",
																	font_name = 'Times New Roman',
																	font_size = 36,
																	x = (window.width//2), y = (window.height//9),
																	anchor_x = 'center', anchor_y = 'center')

										score = pyglet.text.Label ('Words: ' + str(correct),
																	font_name = 'Times New Roman',
																	font_size = 14,
																	x = (window.width//10), y = window.height*(17/18),
																	anchor_x = 'center', anchor_y = 'center')

										@window.event
										def on_draw():
											window.clear()
											test.draw()
											word.draw()
											correct_answer.draw()
											score.draw()
											gl.glClearColor(*background_color)

#--------------------------------------------------------------------------

		if (correct_stdavids == True):
			if (letter_pressed == "ENTER"):
				if (word_list[x] == "S"):
					if (word_list[x+1] == "T"):
						if (word_list[x+2] == "D"):
							if (word_list[x+3] == "A"):
								if (word_list[x+4] == "V"):
									if (word_list[x+5] == "I"):
										if (word_list[x+6] == "D"):
											if (word_list[x+7] == "S"):
												print("You got 'St Davids'!")
												correct += 1
												answer = "st davids"
												correct_stdavids = False

												correct_answer = pyglet.text.Label ("You got '" + answer + "'!",
																			font_name = 'Times New Roman',
																			font_size = 36,
																			x = (window.width//2), y = (window.height//9),
																			anchor_x = 'center', anchor_y = 'center')

												score = pyglet.text.Label ('Words: ' + str(correct),
																			font_name = 'Times New Roman',
																			font_size = 14,
																			x = (window.width//10), y = window.height*(17/18),
																			anchor_x = 'center', anchor_y = 'center')

												@window.event
												def on_draw():
													window.clear()
													test.draw()
													word.draw()
													correct_answer.draw()
													score.draw()
													gl.glClearColor(*background_color)

#--------------------------------------------------------------------------

		if (correct_bishop == True):
			if (letter_pressed == "ENTER"):
				if (word_list[x] == "B"):
					if (word_list[x+1] == "I"):
						if (word_list[x+2] == "S"):
							if (word_list[x+3] == "H"):
								if (word_list[x+4] == "O"):
									if (word_list[x+5] == "P"):
										print("You got 'bishop'!")
										correct += 1
										answer = "bishop"
										correct_bishop = False

										correct_answer = pyglet.text.Label ("You got '" + answer + "'!",
																	font_name = 'Times New Roman',
																	font_size = 36,
																	x = (window.width//2), y = (window.height//9),
																	anchor_x = 'center', anchor_y = 'center')

										score = pyglet.text.Label ('Words: ' + str(correct),
																	font_name = 'Times New Roman',
																	font_size = 14,
																	x = (window.width//10), y = window.height*(17/18),
																	anchor_x = 'center', anchor_y = 'center')

										@window.event
										def on_draw():
											window.clear()
											test.draw()
											word.draw()
											correct_answer.draw()
											score.draw()
											gl.glClearColor(*background_color)

#--------------------------------------------------------------------------

		if (correct_canon == True):
			if (letter_pressed == "ENTER"):
				if (word_list[x] == "C"):
					if (word_list[x+1] == "A"):
						if (word_list[x+2] == "N"):
							if (word_list[x+3] == "O"):
								if (word_list[x+4] == "N"):
									print("You got 'canon'!")
									correct += 1
									answer = "canon"
									correct_canon = False

									correct_answer = pyglet.text.Label ("You got '" + answer + "'!",
																font_name = 'Times New Roman',
																font_size = 36,
																x = (window.width//2), y = (window.height//9),
																anchor_x = 'center', anchor_y = 'center')

									score = pyglet.text.Label ('Words: ' + str(correct),
																font_name = 'Times New Roman',
																font_size = 14,
																x = (window.width//10), y = window.height*(17/18),
																anchor_x = 'center', anchor_y = 'center')

									@window.event
									def on_draw():
										window.clear()
										test.draw()
										word.draw()
										correct_answer.draw()
										score.draw()
										gl.glClearColor(*background_color)
#--------------------------------------------------------------------------

		if (correct_baptism == True):
			if (letter_pressed == "ENTER"):
				if (word_list[x] == "B"):
					if (word_list[x+1] == "A"):
						if (word_list[x+2] == "P"):
							if (word_list[x+3] == "T"):
								if (word_list[x+4] == "I"):
									if (word_list[x+5] == "S"):
										if (word_list[x+6] == "M"):
											print("You got 'baptism'!")
											correct += 1
											answer = "baptism"
											correct_baptism = False

											correct_answer = pyglet.text.Label ("You got '" + answer + "'!",
																		font_name = 'Times New Roman',
																		font_size = 36,
																		x = (window.width//2), y = (window.height//9),
																		anchor_x = 'center', anchor_y = 'center')

											score = pyglet.text.Label ('Words: ' + str(correct),
																		font_name = 'Times New Roman',
																		font_size = 14,
																		x = (window.width//10), y = window.height*(17/18),
																		anchor_x = 'center', anchor_y = 'center')

											@window.event
											def on_draw():
												window.clear()
												test.draw()
												word.draw()
												correct_answer.draw()
												score.draw()
												gl.glClearColor(*background_color)

#--------------------------------------------------------------------------

		if (correct_organ == True):
			if (letter_pressed == "ENTER"):
				if (word_list[x] == "O"):
					if (word_list[x+1] == "R"):
						if (word_list[x+2] == "G"):
							if (word_list[x+3] == "A"):
								if (word_list[x+4] == "N"):
									print("You got 'organ'!")
									correct += 1
									answer = "organ"
									correct_organ = False

									correct_answer = pyglet.text.Label ("You got '" + answer + "'!",
																font_name = 'Times New Roman',
																font_size = 36,
																x = (window.width//2), y = (window.height//9),
																anchor_x = 'center', anchor_y = 'center')

									score = pyglet.text.Label ('Words: ' + str(correct),
																font_name = 'Times New Roman',
																font_size = 14,
																x = (window.width//10), y = window.height*(17/18),
																anchor_x = 'center', anchor_y = 'center')

									@window.event
									def on_draw():
										window.clear()
										test.draw()
										word.draw()
										correct_answer.draw()
										score.draw()
										gl.glClearColor(*background_color)

#--------------------------------------------------------------------------

		if (correct_hymns == True):
			if (letter_pressed == "ENTER"):
				if (word_list[x] == "H"):
					if (word_list[x+1] == "Y"):
						if (word_list[x+2] == "M"):
							if (word_list[x+3] == "N"):
								if (word_list[x+4] == "S"):
									print("You got 'hymns'!")
									correct += 1
									answer = "hymns"
									correct_hymns = False

									correct_answer = pyglet.text.Label ("You got '" + answer + "'!",
																font_name = 'Times New Roman',
																font_size = 36,
																x = (window.width//2), y = (window.height//9),
																anchor_x = 'center', anchor_y = 'center')

									score = pyglet.text.Label ('Words: ' + str(correct),
																font_name = 'Times New Roman',
																font_size = 14,
																x = (window.width//10), y = window.height*(17/18),
																anchor_x = 'center', anchor_y = 'center')

									@window.event
									def on_draw():
										window.clear()
										test.draw()
										word.draw()
										correct_answer.draw()
										score.draw()
										gl.glClearColor(*background_color)

#--------------------------------------------------------------------------

		if (correct_parish == True):
			if (letter_pressed == "ENTER"):
				if (word_list[x] == "P"):
					if (word_list[x+1] == "A"):
						if (word_list[x+2] == "R"):
							if (word_list[x+3] == "I"):
								if (word_list[x+4] == "S"):
									if (word_list[x+5] == "H"):
										print("You got 'parish'!")
										correct += 1
										answer = "parish"
										correct_parish = False

										correct_answer = pyglet.text.Label ("You got '" + answer + "'!",
																	font_name = 'Times New Roman',
																	font_size = 36,
																	x = (window.width//2), y = (window.height//9),
																	anchor_x = 'center', anchor_y = 'center')

										score = pyglet.text.Label ('Words: ' + str(correct),
																	font_name = 'Times New Roman',
																	font_size = 14,
																	x = (window.width//10), y = window.height*(17/18),
																	anchor_x = 'center', anchor_y = 'center')

										@window.event
										def on_draw():
											window.clear()
											test.draw()
											word.draw()
											correct_answer.draw()
											score.draw()
											gl.glClearColor(*background_color)

#--------------------------------------------------------------------------

		if (correct_pope == True):
			if (letter_pressed == "ENTER"):
				if (word_list[x] == "P"):
					if (word_list[x+1] == "O"):
						if (word_list[x+2] == "P"):
							if (word_list[x+3] == "E"):
								print("You got 'pope'!")
								correct += 1
								answer = "pope"
								correct_pope = False

								correct_answer = pyglet.text.Label ("You got '" + answer + "'!",
															font_name = 'Times New Roman',
															font_size = 36,
															x = (window.width//2), y = (window.height//9),
															anchor_x = 'center', anchor_y = 'center')

								score = pyglet.text.Label ('Words: ' + str(correct),
															font_name = 'Times New Roman',
															font_size = 14,
															x = (window.width//10), y = window.height*(17/18),
															anchor_x = 'center', anchor_y = 'center')

								@window.event
								def on_draw():
									window.clear()
									test.draw()
									word.draw()
									correct_answer.draw()
									score.draw()
									gl.glClearColor(*background_color)

#--------------------------------------------------------------------------

		if (correct_diocese == True):
			if (letter_pressed == "ENTER"):
				if (word_list[x] == "D"):
					if (word_list[x+1] == "I"):
						if (word_list[x+2] == "O"):
							if (word_list[x+3] == "C"):
								if (word_list[x+4] == "E"):
									if (word_list[x+5] == "S"):
										if (word_list[x+6] == "E"):
											print("You got 'diocese'!")
											correct += 1
											answer = "diocese"
											correct_diocese = False

											correct_answer = pyglet.text.Label ("You got '" + answer + "'!",
																		font_name = 'Times New Roman',
																		font_size = 36,
																		x = (window.width//2), y = (window.height//9),
																		anchor_x = 'center', anchor_y = 'center')

											score = pyglet.text.Label ('Words: ' + str(correct),
																		font_name = 'Times New Roman',
																		font_size = 14,
																		x = (window.width//10), y = window.height*(17/18),
																		anchor_x = 'center', anchor_y = 'center')

											@window.event
											def on_draw():
												window.clear()
												test.draw()
												word.draw()
												correct_answer.draw()
												score.draw()
												gl.glClearColor(*background_color)

#--------------------------------------------------------------------------
#Code that is similar as the code above but is for when the user is done

		if (letter_pressed == "ENTER"):
			if (word_list[x] == "D"):
				if (word_list[x+1] == "O"):
					if (word_list[x+2] == "N"):
						if (word_list[x+3] == "E"):

							#Sets the string variable "grade" depending on what the user's score is
							if (correct >= 13):
								grade = "A+"
							elif (correct >= 11):
								grade = "A"
							elif (correct >= 9):
								grade = "A-"
							elif (correct >= 7):
								grade = "B+"
							elif (correct >= 5):
								grade = "B"
							elif (correct >= 3):
								grade = "B-"
							else:
								grade = "F"

							#Text block for the grade the user got
							grade_received = pyglet.text.Label ('Your grade: ' + grade,
														font_name = 'Times New Roman',
														font_size = 36,
														x = (window.width//2), y = (window.height//2),
														anchor_x = 'center', anchor_y = 'center')
							
							#Draws the final screen with their grade
							@window.event
							def on_draw():
								window.clear()
								test.draw()
								grade_received.draw()
								final_text.draw()
								gl.glClearColor(*background_color)


#--------------------------------------------------------------------------

	#Another final screen drawing, but only for if they get all the words
	if (correct == 14):
		@window.event
		def on_draw():
			window.clear()
			test.draw()
			grade_received.draw()
			final_text.draw()
			gl.glClearColor(*background_color)

#-----------------------------------------------------------------------
#Display

#Updated score text
score = pyglet.text.Label ('Words: ' + str(correct),
							font_name = 'Times New Roman',
							font_size = 14,
							x = (window.width//10), y = window.height*(17/18),
							anchor_x = 'center', anchor_y = 'center')

#Sets the background color
background_color = (0.6, 0.4, 0.2, 1)
gl.glClearColor(*background_color)


#Draws the initial screen
@window.event
def on_draw():
	window.clear()
	gl.glClearColor(*background_color)
	test.draw()
	word_instructions_text1.draw()
	word_instructions_text2.draw()
	word_instructions_text3.draw()
	word_instructions_text4.draw()
	word_instructions_text5.draw()
	word_instructions_text6.draw()

pyglet.app.run()
