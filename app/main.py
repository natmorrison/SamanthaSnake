import json
import os
import random
import bottle

from app.api import left_space, right_space, top_space, bottom_space, is_snake, is_wall, is_food, go, get_head, dont_go

LEFT = 'left'
RIGHT = 'right'
UP = 'up'
DOWN = 'down'

@bottle.route('/')
def index():
	return "<h1>I'm Nat and this is my snake</h1>"

@bottle.route('/static/<path:path>')
def static(path):
	return bottle.static_file(path, root='static/')

@bottle.post('/ping')
def ping():
	return {}

@bottle.post('/start')
def start():
	return {
		"color": '#AA22AA',
		"taunt": "My first program, go nice"
	}

@bottle.post('/end')
def end():
	return {}




@bottle.post('/move')
def move():
	data = bottle.request.json
	directions = ['up', 'down', 'left', 'right']

	"""
	 _  _   _ _____
	| \| | /_\_   _|
	| .` |/ _ \| |
	|_|\_/_/ \_\_|

	get_head(data)

	left_space(data, space)
	right_space(data, space)
	top_space(data, space)
	bottom_space(data, space)

	is_snake(data, space)
	is_wall(data, space)
	is_food(data, space)

	dont_go(directions, direction)
	go(directions, direction)

	"""

	#head = get_head(data)
	# head = (3, 2)
	#right = right_space(data, head)
	# The space to the right of head
	# right = (4, 2)
	#right_of_the_right = right_space(data, right)
	# right_of_the_right = (5, 2)
	#if is_wall(data, right_of_the_right):
		#directions = dont_go(directions, RIGHT)


	# Get your head
	headmyhead = get_head(data)

	# Get the space to your right, left, up, and down
	left = left_space(data, headmyhead)
	right = right_space(data, headmyhead)
	down = bottom_space(data, headmyhead)
	up = top_space(data, headmyhead)
	
	leftleft = left_space(data, left)
	rightright = right_space(data, right)
	downdown = down_space(data, down)
	upup = up_space(data, up)
	

	# Don't hit a wall
	if is_wall(data, left):
		directions = dont_go(directions, LEFT)
	if is_wall(data, right):
		directions = dont_go(directions, RIGHT)
	if is_wall(data, down):
		directions = dont_go(directions, DOWN)
	if is_wall (data, up):
		directions = dont_go(directions, UP)
	
	# Don't hit a snake
	if is_snake (data, left):
		directions = dont_go(directions, LEFT)
	if is_snake(data, right):
		directions = dont_go(directions, RIGHT)
	if is_snake(data, down):
		directions = dont_go(directions, DOWN)
	if is_snake(data, up):
		directions = dont_go(directions, UP)
	
	# Get yer food boi
	if is_food(data, left):
		directions = go(directions, LEFT)
	if is_food(data, right):
		directions = go(directions, RIGHT)
	if is_food(data, down):
		directions = go(directions, DOWN)
	if is_food (data, up):
		directions = go(directions, UP)
		
	directionsBeforeTwoSpaceDecision = list(directions)
	
	# Don't go within 2 spaces of another snakes
	
	if directions == []:
		directions = directionsBeforeTwoSpaceDecision
	
	if is_snake(data, leftleft):
		directions = dont_go(directions, LEFT)
	if is_snake (data, rightright):
		directions = dont_go(directions, RIGHT)
	if is_snake (data, downdown):
		directions = dont_go(directions, DOWN)
	if is_snake(data, upup)
		directions = dont_go(directions, UP)
		




	"""
	 _  _   _ _____
	| \| | /_\_   _|
	| .` |/ _ \| |
	|_|\_/_/ \_\_|

	"""

	move = random.choice(directions)

	return {
		"move": move
	}



application = bottle.default_app()

if __name__ == '__main__':
	bottle.run(
		application,
		host=os.getenv('IP', '0.0.0.0'),
		port=os.getenv('PORT', '8080'),
		debug=os.getenv('DEBUG', True)
	)
