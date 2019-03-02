import json
import os
import random
import bottle

from app.api import left_space, right_space, top_space, bottom_space, is_snake, is_wall, get_head, dont_go

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
    return HTTPResponse(
        status=200
    )

@bottle.post('/start')
def start():
    return {
		"color": '#AA22AA',
		"taunt": "My first program, go nice"
	}

@bottle.post('/end')
def end():
    return HTTPResponse(
        status=200
    )




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

    """



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
